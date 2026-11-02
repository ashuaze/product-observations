# P0006 研究底稿

原期号：P06。原研究核查日期：2026-10-13；归档与中文补写日期：2026-11-02。

原材料：[P06-github-repository-exit-states.md](https://chatgpt.com/library?file_id=libfile_12fe461b07188191adb1c90f496a6389&account_id=personal)。来源字节指纹见 metadata.yaml。原文中的“本次”“当前”等表述属于原研究日期，不代表本次归档重新验证了产品政策、价格或研究结果。

英文处理：正文词句和段落保持原样；移除写作块包装与标题中的字符统计。 中文发布稿为本次独立改写。两种语言均为待审草稿。

## 原稿编辑信息

**研究主题：** 产品如何给用户保留反悔、退出和恢复的机会？  
**本篇读者价值：** 帮助产品经理、设计师与独立开发者把“退出”拆成暂停、移交、移除与恢复四个不同任务，避免用一个危险操作承载互相冲突的用户意图。

## 中文审稿摘要

- 核心判断：产品不应把“离开”压成一个动作。停止维护、移交责任、移除可见性和误删恢复，是四个不同任务。
- 关键证据：Archive 可撤销且保留可搜索的只读资料；Transfer 延续项目，但 Pages 链接、权限和套餐能力并非全量无损迁移。
- 重要边界：Delete 的影响取决于仓库关系和可见性——公共仓库的 fork 保留，私有仓库的 fork 会随之删除。
- 反例修正：90 天恢复窗口并不等于完整回滚；非空 fork network 可能阻止自助恢复，团队权限也不会恢复。
- 给产品团队的判断依据：先问用户想得到什么结果，再决定动作；确认弹窗只能确认选择，不能纠正选错的任务模型。

## 中文研究底稿

### 研究问题

维护者说“我不再做这个项目了”时，真实任务可能是什么？产品应该如何在历史参考、持续维护、内容移除和误操作恢复之间取舍？

### 可比选项

| 选项 | 主要任务 | 保留什么 | 关键代价或失败条件 |
|---|---|---|---|
| Archive | 停止新活动，保留参考 | 仓库内容、讨论与搜索入口；之后可取消归档 | 内容仍可见；需要修改时必须先取消归档；它不是独立备份 |
| Transfer | 移交责任，项目继续 | 代码、issues、PR、wiki、stars、watchers 等；旧仓库链接重定向 | GitHub Pages URL 不重定向；权限与套餐能力可能变化；旧位置被重新占用会永久破坏重定向 |
| Delete | 移除仓库 | 仅有条件地保留 90 天恢复机会 | 公私仓库对 forks 的影响不同；团队权限永久丢失；部分 fork network 无法自助恢复 |
| Backup | 独立保存或灾难恢复 | 取决于备份方法；mirror clone 可保留 Git 文件与修订历史 | wiki、LFS、讨论、packages 等可能需单独处理；migration archive 不是可完整回灌 GitHub 的保证 |

### 关键事实与对应来源

1. **事实：** 归档后仓库对所有用户只读，仍可搜索；用户仍可 fork 和 star；之后可取消归档。  
   **来源：** GitHub Docs, [Archiving repositories](https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories)[^source01]，核查于 2026-10-13。

2. **事实：** Transfer 会转移 issues、PR、wiki、stars、watchers 等，并让旧仓库链接及 Git 操作重定向；GitHub Pages URL 不重定向。目标归属、可见性和套餐变化还可能改变权限或功能。  
   **来源：** GitHub Docs, [Transferring a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository)[^source02]，核查于 2026-10-13。

3. **事实：** 删除公共仓库不会删除其 forks；删除私有仓库会删除其所有 forks；团队权限永久删除。  
   **来源：** GitHub Docs, [Deleting a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository)[^source03]，核查于 2026-10-13。

4. **事实：** 部分已删除仓库可在 90 天内恢复；属于非空 fork network 的仓库不满足普通自助恢复条件。恢复后的仓库不会恢复团队权限；相关恢复通过支持渠道处理时还存在付费套餐条件。  
   **来源：** GitHub Docs, [Restoring a deleted repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/restoring-a-deleted-repository)[^source04]，核查于 2026-10-13。

5. **事实：** Git mirror clone 可备份文件与修订历史；wiki 与 LFS 需额外处理。GitHub 的 migration archives 不包含全部仓库数据（例如 LFS、discussions、packages），且没有官方文档支持的 GitHub 恢复路径。  
   **来源：** GitHub Docs, [Backing up a repository](https://docs.github.com/en/repositories/archiving-a-github-repository/backing-up-a-repository)[^source05]，核查于 2026-10-13。

### 解释、反证与边界

- **推断：** GitHub 的三个动作体现了三种产品语义：暂停状态、变更责任主体、移除对象。把它们并列不是多余复杂度，而是在保护不同用户目标。
- **推断：** “能恢复”应按组件检查，而非给对象贴一个可逆标签。代码、链接、forks、团队权限和套餐能力的恢复程度不同。
- **反证检查：** Archive 虽可撤销，却不适合“内容必须不再可用”的目标；Transfer 虽保留项目连续性，也不是零损迁移；Delete 虽有 90 天窗口，也不是完整撤销。三个动作均不能单独覆盖所有退出需求。
- **公平比较边界：** 这里比较的是 GitHub.com 当前仓库生命周期文档，不代表 GitLab、Bitbucket 或企业自托管实例采用相同规则。GitHub 的 legacy per-repository billing、组织权限、fork network 与计划等级均可能改变结果。
- **证据限制：** 本次只有官方功能文档，没有 GitHub 的内部设计意图、误删率、恢复成功率或用户研究。因此不能声称该设计已被实验验证能减少错误。
- **实际体验：** 本次未执行真实仓库的归档、转移或删除；没有把文档行为写成亲身体验。考虑到删除与转移可能影响真实协作者和链接，本篇不要求为发稿而做破坏性测试。

### 可检验假设与会改变判断的证据

- 假设：在危险区先让用户选择“暂停维护 / 移交维护 / 移除项目”，再映射到具体动作，会比只展示动作名称和确认弹窗减少误删。需要受控实验或误删、恢复数据验证。
- 假设：恢复质量应按代码、权限、链接、fork 关系等维度衡量，而不是只统计仓库是否重新出现。若 GitHub 的实测恢复能完整还原这些维度，本篇对“部分可逆”的判断应相应上调。
- 若用户研究显示大多数维护者明确理解三种动作，且选错率极低，则“按目标引导”的额外界面可能不值得其复杂度。

### 本次新增认识

P05 将注册、发现、展示与验证拆成不同身份层；P06 把同一方法延伸到生命周期：暂停、移交、删除与恢复也不应被“退出”一个词合并。更进一步，可逆性不是对象级布尔值，而是其依赖关系逐项恢复的结果。

### 发布前检查

- **熟悉产品的人新增什么？** 90 天恢复并不代表完整回滚；fork 拓扑、团队权限、Pages URL 与套餐能力会让可逆性分裂。
- **核心判断由什么支持？** GitHub 五份当前官方文档支持功能边界；“按目标拆分任务”是基于这些边界的产品分析，不伪装成官方意图。
- **什么能推翻判断？** 真实误操作、恢复完整度和目标式界面的对照实验。
- **读者可做什么更好的决定？** 在设计 destructive actions 前，先列出用户要停止、移交、移除和恢复的分别是什么，再定义每个依赖对象的后果。

## 核查来源

原始来源与对应关系保留在上文。本节仅整理可点击的链接索引；原研究核查日期为 2026-10-13。

1. [Archiving repositories](https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories)
2. [Transferring a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository)
3. [Deleting a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository)
4. [Restoring a deleted repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/restoring-a-deleted-repository)
5. [Backing up a repository](https://docs.github.com/en/repositories/archiving-a-github-repository/backing-up-a-repository)

## 发稿前检查

本节为归档阶段整理。稿件结构、正文长度和引用交由检查工具核对；事实、推断与反例仍以原研究为据。人工审稿待完成，未记录平台发布。


## 归档格式检查

本次使用官方 twitter-text 3.1.0 重新计数；不以原稿的手工计数作为最终结果。

英文加权长度：248 / 260 / 264 / 253 / 272 / 256。

中文加权长度：160 / 188 / 163 / 142。

格式检查不代表人工批准或平台发布。

[^source01]: [Archiving repositories](https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source02]: [Transferring a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source03]: [Deleting a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source04]: [Restoring a deleted repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/restoring-a-deleted-repository)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source05]: [Backing up a repository](https://docs.github.com/en/repositories/archiving-a-github-repository/backing-up-a-repository)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
