# 归档与同步约定

## 目录与文件职责

每期使用 `posts/P0000-slug/`。`README.md` 提供介绍和导航；`research.md` 保存审稿摘要、研究论证及完整来源；`publish-zh.md` 和 `publish-en.md` 只存发布正文；`metadata.yaml` 保存稳定身份、来源和状态。X 串帖以 `### 1/6` 等标题分隔，正文中保留实际发布的顺序号；标题本身不计入发布长度。

## 身份与时间

- 历史 P26 映射为 P0026；`legacy_id` 保留原期号。
- 沿用当前每日任务的日期规则：北京时间 2026-10-09 对应 P02，每过一个自然日加一。同日重跑复用编号；不使用最大目录编号加一。
- 目录 slug 一旦归档保持稳定，标题修改不触发路径重命名。
- `date` 为原期刊日期，`archived_at` 为归档日期，`source.checked_at` 为原研究核查日期。
- 历史稿的补写时间另记，不将归档或补写伪装为当时已经完成的工作。

## 研究与语言

事实、团队陈述、作者推断、假设与限制明确区分。核查日期不会随格式迁移刷新。英文沿用时保留正文指纹；新增中文稿标记为改写稿和待审稿，不把审稿摘要当作发布稿。

来源使用完整 URL 和 Markdown 脚注，记录支持的事实及限制；不保留聊天专用引用标记。发布正文保留随帖链接，字符核验、编者说明及状态放在研究底稿或元数据。

## 状态

`review_status` 与各语言的稿件状态、发布时间和链接分开记录。本期两种语言均为 `draft`，人工审稿为 `pending`。内容检查通过只表示结构和长度合格，不等同于人工批准或平台发布。

## 每次同步

1. 读取目标仓库的当前分支、HEAD、本期期号目录及索引。只处理本期和索引生成区。
2. 生成文件后执行 `python3 scripts/check_archive.py --write-index`。失败时不提交，保留已生成稿件。
3. 对比文件内容；完全相同则跳过提交，同日重跑不新建一期。
4. 将本期文件与总索引作为同一提交；更新分支时校验预期 HEAD。不要强制推送。
5. 如果发现远端变化，重新读取并比较。存在人工审稿变更时保留远端版本，另开分支处理差异；不自动覆盖。
6. 提交后检查 commit 的文件列表，并读取远端关键文件核对。只有取得可验证的 commit 链接才报告同步成功。
7. 同步失败重试复用原期号、slug 和生成材料；不重复生成无关内容。

归档目标为 [ashuaze/product-observations](https://github.com/ashuaze/product-observations)，默认分支为 `main`。首次试跑仅迁移 P26；每日定时任务的自动同步尚未接入。

## 检查工具的范围

`scripts/check_archive.py` 检查目录与元数据对应、期号唯一性、必要文件、相对链接、脚注定义、聊天标记清理、串帖顺序、加权长度、正文指纹和索引一致性。

字符计数使用 NFC 归一化及 twitter-text v3 的 Unicode 权重，显式 HTTP(S) URL 计 23；本期没有 emoji 或复杂 URL。工具会拒绝包含复杂 emoji、隐藏格式字符和未覆盖链接形式的正文，要求另用官方 twitter-text 校验后扩展工具，避免给出错误的通过结果。它不是任意输入下官方解析器的完整替代品。

规则来源：

- [twitter-text v3 配置](https://github.com/twitter/twitter-text/blob/master/config/v3.json)
- [twitter-text 配置说明](https://github.com/twitter/twitter-text/blob/master/config/README.md)
- [GitHub Markdown 脚注](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#footnotes)
