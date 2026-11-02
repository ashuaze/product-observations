#!/usr/bin/env python3
"""Validate the archive and optionally rebuild only the README index region."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
START, END = '<!-- ARCHIVE:START -->', '<!-- ARCHIVE:END -->'
REQUIRED = ('README.md', 'research.md', 'publish-zh.md', 'publish-en.md', 'metadata.yaml')
URL = re.compile(r'https?://[A-Za-z0-9./_%?=&:#~+\-]+')


def ensure(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def split_posts(text: str) -> list[str]:
    headers = list(re.finditer(r'^### ([1-9]\d*)/([1-9]\d*)\s*$', text, re.M))
    ensure(bool(headers), 'No post boundaries')
    ensure(not text[:headers[0].start()].strip(), 'Editorial content before first post')
    count = len(headers)
    posts = []
    for i, header in enumerate(headers):
        ensure((int(header[1]), int(header[2])) == (i + 1, count), 'Thread headers out of order')
        end = headers[i + 1].start() if i + 1 < count else len(text)
        post = text[header.end():end].strip()
        ensure(bool(re.match(rf'{i + 1}/{count}\s', post)), 'Missing published post number')
        posts.append(post)
    return posts


def weighted_length(post: str) -> int:
    normalized = unicodedata.normalize('NFC', post)
    # Deliberately narrow supported inputs; never silently claim full twitter-text parity.
    for char in normalized:
        cp = ord(char)
        ensure(cp not in (0x200D, 0x20E3) and not 0xFE00 <= cp <= 0xFE0F
               and not 0x1F000 <= cp <= 0x1FAFF and not 0x2600 <= cp <= 0x27BF,
               'Emoji input requires the official twitter-text parser')
        ensure(unicodedata.category(char) != 'Cf', 'Hidden format character needs manual review')
    spans = list(URL.finditer(normalized))
    for match in spans:
        ensure(match[0][-1] not in '.,:;!?', 'Ambiguous trailing URL punctuation')
    plain = URL.sub('', normalized)
    ensure('http' not in plain and 'www.' not in plain, 'Uncovered URL syntax')
    ensure(not re.search(r'\b[a-zA-Z0-9-]+\.(?:com|org|net|io|dev|app|co)\b', plain),
           'Bare domains require official URL extraction')
    def weight(char: str) -> int:
        cp = ord(char)
        return 1 if (cp <= 0x10FF or 0x2000 <= cp <= 0x200D
                     or 0x2010 <= cp <= 0x201F or 0x2032 <= cp <= 0x2037) else 2
    return 23 * len(spans) + sum(weight(char) for char in plain)


def body_hash(posts: list[str]) -> str:
    return hashlib.sha256(json.dumps(posts, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()


def check_links(path: Path) -> None:
    text = path.read_text(encoding='utf-8')
    ensure(not any(marker in text for marker in ('genui', ':::writing', 'turn0search', 'turn1search')),
           f'{path.name}: chat-only marker')
    definitions = re.findall(r'^\[\^([^\]]+)\]:', text, re.M)
    uses = re.findall(r'\[\^([^\]]+)\](?!:)', text)
    ensure(len(definitions) == len(set(definitions)), f'{path.name}: duplicate footnote definition')
    ensure(set(uses) == set(definitions), f'{path.name}: missing or unused footnotes')
    for target in re.findall(r'(?<!!)\[[^\]\n]*\]\(([^\s)]+)\)', text):
        if re.match(r'https?://|mailto:|#', target):
            continue
        resolved = (path.parent / target.split('#')[0]).resolve()
        ensure(resolved.is_relative_to(ROOT), f'{path.name}: link outside archive')
        ensure(resolved.exists(), f'{path.name}: missing relative link {target}')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-index', action='store_true')
    args = parser.parse_args()
    entries, ids, results = [], set(), []
    for directory in sorted((ROOT / 'posts').iterdir()):
        if not directory.is_dir():
            continue
        for name in REQUIRED:
            ensure((directory / name).is_file(), f'{directory.name}: missing {name}')
        meta = yaml.safe_load((directory / 'metadata.yaml').read_text(encoding='utf-8'))
        issue = meta['id']
        ensure(re.fullmatch(r'P\d{4}', issue) is not None, 'Invalid issue ID')
        ensure(issue not in ids, f'Duplicate ID: {issue}')
        ids.add(issue)
        ensure(directory.name == f"{issue}-{meta['slug']}", 'Directory / metadata mismatch')
        ensure(meta['timezone'] == 'Asia/Shanghai', 'Unexpected publication timezone')
        ensure(meta['review_status'] in ('pending', 'approved', 'changes_requested'), 'Invalid review status')
        ensure(re.fullmatch(r'[0-9a-f]{64}', meta['source']['sha256']) is not None, 'Invalid source fingerprint')
        thread_results = {}
        for lang in ('zh', 'en'):
            language = meta['languages'][lang]
            ensure(language['file'] == f'publish-{lang}.md', 'Unexpected publish path')
            ensure(language['status'] in ('draft', 'ready', 'published'), 'Invalid language status')
            if language['status'] == 'published':
                ensure(bool(language['published_at'] and language['published_url']), 'Missing publication record')
            else:
                ensure(language['published_at'] is None and language['published_url'] is None,
                       'Draft has a publication record')
            posts = split_posts((directory / language['file']).read_text(encoding='utf-8'))
            lengths = [weighted_length(post) for post in posts]
            ensure(all(length <= 280 for length in lengths), f'{issue}/{lang}: X weighted length > 280: {lengths}')
            ensure(body_hash(posts) == language['body_sha256'], f'{issue}/{lang}: body changed; review/update fingerprint')
            ensure(len(posts) == language['post_count'], 'Post count mismatch')
            thread_results[lang] = lengths
        research = (directory / 'research.md').read_text(encoding='utf-8')
        for heading in ('## 中文审稿摘要', '## 中文研究底稿', '## 核查来源', '## 发稿前检查'):
            ensure(heading in research, f'Missing research section: {heading}')
        for md in directory.glob('*.md'):
            check_links(md)
        rel = directory.relative_to(ROOT).as_posix()
        title = meta['title_zh'].replace('|', '\\|')
        labels = {'draft': '草稿', 'ready': '待发布', 'published': '已发布'}
        zh_label = labels[meta['languages']['zh']['status']]
        en_label = labels[meta['languages']['en']['status']]
        entries.append(f"| {issue} | {meta['date']} | [{title}]({rel}/README.md) | {meta['theme']['title']} | [{zh_label}]({rel}/publish-zh.md) | [{en_label}]({rel}/publish-en.md) |")
        results.append({'id': issue, 'weighted_lengths': thread_results})
    ensure(bool(entries), 'Archive contains no issues')
    index = '\n'.join(['| 期号 | 日期 | 标题 | 主题 | 中文稿 | 英文稿 |',
                       '|---|---|---|---|---|---|', *entries])
    readme = ROOT / 'README.md'
    content = readme.read_text(encoding='utf-8')
    ensure(content.count(START) == content.count(END) == 1, 'Missing/duplicate index boundaries')
    ensure(content.index(START) < content.index(END), 'Reversed index boundaries')
    before, rest = content.split(START)
    _, after = rest.split(END)
    updated = before + START + '\n' + index + '\n' + END + after
    changed = content != updated
    if args.write_index and changed:
        readme.write_text(updated, encoding='utf-8')
    else:
        ensure(not changed, 'Index is stale; run --write-index')
    for md in ROOT.glob('*.md'):
        check_links(md)
    print(json.dumps({'ok': True, 'issues': len(entries), 'index_changed': args.write_index and changed,
                      'results': results}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, OSError, yaml.YAMLError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        raise SystemExit(1)
