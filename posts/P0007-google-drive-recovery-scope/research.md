# P0007 研究底稿

原期号：P07。原研究核查日期：2026-10-14；归档与中文补写日期：2026-11-02。

原材料：[P07-google-drive-recovery-scope-2026-10-14.md](https://chatgpt.com/library?file_id=libfile_ce0f31d398bc8191a391a6a8fc034f51&account_id=personal)。来源字节指纹见 metadata.yaml。原文中的“本次”“当前”等表述属于原研究日期，不代表本次归档重新验证了产品政策、价格或研究结果。

英文处理：正文词句和段落保持原样；移除写作块包装与标题中的字符统计。 中文发布稿为本次独立改写。两种语言均为待审草稿。

## 原稿编辑信息

**研究主题：** 产品如何给用户保留反悔、退出和恢复的机会？  
**本篇读者价值：** 帮助产品经理、设计师与独立开发者按照错误的类型和影响范围选择 Undo、版本历史、批量回滚或 Trash，而不是把所有恢复需求塞进一个入口。

## 中文审稿摘要

- **核心判断：** 恢复机制不仅需要足够长的时间窗口，还要让恢复单位与事故范围匹配：一次动作、一个文件、多文件事故和删除分别需要不同工具。
- **关键证据：** Google 文档可恢复或复制单个旧版本；普通 Drive 文件的旧版本可能在 30 天后或出现 100 个更新版本后被删除，除非选择 Keep forever。
- **新案例：** Google Drive 当前 Beta 批量恢复可处理最近 25 天内的多文件变化，但不能逐文件选择，且不适用于 Google 原生文档。
- **反例修正：** 大范围回滚会覆盖仍然正确的新编辑；Google 通过把旧副本设为新的当前版本、保留既有版本，为“撤销恢复”留下路径，但仍会增加逐文件检查成本。
- **证据限制：** 官方资料说明功能，不证明 25 或 30 天是最佳窗口，也没有公开误操作率、恢复成功率或 Beta 的完整账号覆盖情况。

## 中文研究底稿

### 研究问题

当错误可能只影响一次动作、一个文件或成百上千个文件时，产品应该让用户恢复什么单位？恢复操作本身是否也应该可以反悔？

### 可比机制

| 机制 | 针对的错误 | 恢复单位 | 主要代价或失败条件 |
|---|---|---|---|
| Undo | 刚完成且仍在当前交互上下文中的动作 | 一次动作 | 窗口短；跨设备或延迟发现时通常无能为力 |
| Google Docs 版本历史 | 已知某个原生文档被错误修改 | 单个文件或其副本 | 需要编辑权限；恢复旧版可能覆盖当前状态；部分修订可能合并 |
| Drive 普通文件版本 | PDF、图片等非 Google 文件被覆盖 | 单个文件 | 旧版可能在 30 天后或 100 个更新版本后删除；需主动 Keep forever |
| Drive 批量恢复 Beta | 同步错误、勒索软件等造成多文件变化 | 某个时间点涉及的多个文件 | 最近 25 天；不能逐文件选择；Google 原生文件不在其中 |
| Drive Trash | 文件被删除 | 一个或多个已删除对象 | 30 天后永久删除；它不解决内容被覆盖的问题 |

### 关键事实及对应来源

1. **事实：** 有编辑权限的用户可以查看 Google Docs、Sheets、Slides 或 Vids 的早期版本，查看修改者，恢复旧版本或把旧版本复制为新文件。恢复较早的 Spreadsheet 会清除恢复点之前的逐单元格编辑历史；如需保留该诊断信息，官方建议制作副本。部分修订可能被合并。  
   **来源：** Google Docs Editors Help, [Find what's changed in a file](https://support.google.com/docs/answer/190843?hl=en)[^source01]，核查于 2026-10-14。

2. **事实：** 对 PDF、图片等普通 Drive 文件，旧版本可能在 30 天后或出现 100 个更新版本后被永久删除；用户可选择 Keep forever，并可下载版本。Google 原生文档采用另一套版本历史。  
   **来源：** Google Drive Help, [Check activity & file versions](https://support.google.com/drive/answer/2409045?hl=en)[^source02]，核查于 2026-10-14。

3. **事实：** Google Drive 的 Restore file versions 当前标注为 Beta，可回滚多个文件，并保留最近 25 天的修订。用户不能逐个选择文件；旧版本会被复制并成为新的当前版本，既有版本不会被删除。Google Docs、Slides 等原生文件不会出现在此工具中；删除文件需要走单独的恢复流程。  
   **来源：** Google Drive Help, [Restore files in bulk with Google Drive](https://support.google.com/drive/answer/16482799?hl=en)[^source03]，核查于 2026-10-14。

4. **事实：** Drive Trash 中的文件保留 30 天，此后永久删除；在期限内可以恢复。所有者把共享文件移入 Trash 后，其他人仍可访问，直到该文件被永久删除。  
   **来源：** Google Drive Help, [Recover a deleted file](https://support.google.com/drive/answer/1716222?hl=en)[^source04]；[Learn what happens when you delete a file](https://support.google.com/drive/answer/14933051?hl=en)[^source05]，核查于 2026-10-14。

### 解释、反证与边界

- **推断：** 恢复能力至少有三个维度：错误类型、影响范围和可用时间。只延长时间窗口，不能解决用户找不到受损文件或数百个文件需要逐一恢复的问题。
- **推断：** “复制旧版本”与“把旧版本设为当前版本”应是不同选择。前者适合原因仍不确定、需要比较或保留当前工作的情境；后者适合目标状态已经明确。
- **反证检查：** 批量恢复减少逐文件操作，却可能把事故之后的正常编辑一起回滚。当前机制以追加新当前版本、保留旧版本来降低二次损失，但用户仍需识别和修正不该回滚的文件。
- **相反取舍：** 更长的版本保留能提高恢复机会，也会延长历史内容的存在时间、占用存储，并可能与主动删除历史的需求冲突。Google 文档允许所有者永久删除版本历史，说明恢复与彻底移除并非同一目标。
- **产品与版本边界：** 批量恢复页面明确标为 Beta；页面未明确列出所有账号、地区或套餐的可用范围，因此不能假定每个用户都已看到入口。
- **证据限制：** 本次为官方功能文档核查，没有 Google 的用户研究、事故数据或对照实验。不能声称这些层级已被证明能降低损失。
- **实际体验：** 本次未在真实 Drive 上执行批量恢复，未把帮助文档行为描述为亲身体验。由于该工具不能逐文件选择，不建议为了验证文章而在存有真实资料的账号上尝试。

### 可检验假设及会改变判断的证据

- 假设：当一次事故影响大量文件时，按时间点批量恢复会比逐文件恢复减少操作时间与漏项；需要真实事故的完成时间、遗漏率和二次修复量验证。
- 假设：恢复后保留被替换版本，会降低错误回滚造成的最终损失；若用户实际上无法发现或理解这些保留版本，这种技术可逆性不一定转化为可用的恢复能力。
- 如果日志显示绝大多数恢复只涉及单文件，而且批量恢复经常带来大量不必要回滚，则应缩小其推荐范围，优先改进筛选和预览。

### 未解决问题

- Beta 的具体账号、地区与套餐覆盖范围，当前帮助页未明确说明。
- 批量恢复界面是否充分显示受影响文件数量、例外和预计结果，公开文档不足以判断。
- 没有公开数据说明用户通常在事故发生多久后发现问题，因而无法判断 25 天与 30 天是否贴合真实发现周期。

### 本次新增认识

P06 的新增认识是“恢复对象不等于恢复其关系”；P07 再增加一层：**恢复单位必须匹配事故的影响单位，而且恢复动作本身也应尽量采用追加状态，而不是销毁现有状态。**

### 发布前检查

- **熟悉产品的人新增什么？** Google Drive 已有一个当前标为 Beta 的 25 天批量恢复层；它与单文件历史和 30 天 Trash 处理的是不同失败模式。
- **核心判断由什么支持？** 三套官方版本与删除文档；“匹配事故范围”是基于机制差异的产品分析，不冒充 Google 的公开设计意图。
- **什么能推翻判断？** 实际事故范围、发现时间、批量恢复误伤率及用户理解数据。
- **读者可做什么更好的决定？** 为每类错误同时定义恢复对象、时间窗、预览范围，以及“恢复错了以后怎么办”。

## 核查来源

原始来源与对应关系保留在上文。本节仅整理可点击的链接索引；原研究核查日期为 2026-10-14。

1. [Find what's changed in a file](https://support.google.com/docs/answer/190843?hl=en)
2. [Check activity & file versions](https://support.google.com/drive/answer/2409045?hl=en)
3. [Restore files in bulk with Google Drive](https://support.google.com/drive/answer/16482799?hl=en)
4. [Recover a deleted file](https://support.google.com/drive/answer/1716222?hl=en)
5. [Learn what happens when you delete a file](https://support.google.com/drive/answer/14933051?hl=en)

## 发稿前检查

本节为归档阶段整理。稿件结构、正文长度和引用交由检查工具核对；事实、推断与反例仍以原研究为据。人工审稿待完成，未记录平台发布。


## 归档格式检查

本次使用官方 twitter-text 3.1.0 重新计数；不以原稿的手工计数作为最终结果。

英文加权长度：262 / 263 / 268 / 268 / 275。

中文加权长度：144 / 203 / 178 / 169。

格式检查不代表人工批准或平台发布。

[^source01]: [Find what's changed in a file](https://support.google.com/docs/answer/190843?hl=en)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source02]: [Check activity & file versions](https://support.google.com/drive/answer/2409045?hl=en)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source03]: [Restore files in bulk with Google Drive](https://support.google.com/drive/answer/16482799?hl=en)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source04]: [Recover a deleted file](https://support.google.com/drive/answer/1716222?hl=en)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source05]: [Learn what happens when you delete a file](https://support.google.com/drive/answer/14933051?hl=en)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
