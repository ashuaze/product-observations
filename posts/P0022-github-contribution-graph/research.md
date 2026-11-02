# P0022 研究底稿

原期号：P22。原研究核查日期：2026-10-29；归档与中文补写日期：2026-11-02。

原材料：[P22_GitHub_contribution_graph.md](https://chatgpt.com/library?file_id=libfile_c14756a1a598819182651fc3b6ec47a7&account_id=personal)。来源字节指纹见 metadata.yaml。原文中的“本次”“当前”等表述属于原研究日期，不代表本次归档重新验证了产品政策、价格或研究结果。

英文处理：仅补齐正文串帖序号；原英文词句和段落保持原样。 中文发布稿为本次独立改写。两种语言均为待审草稿。

## 原稿编辑信息

研究主题：习惯设计的收益与副作用。读者价值：帮助产品经理、设计师与独立开发者判断，日活跃度可视化是在支持有效重复，还是诱导用户维护分数。

## 中文审稿摘要

- 核心判断：日活跃度指标既是反馈，也是对“什么算进步”的定义；它能促进重复，也会诱导用户优化可见信号。
- 当前 GitHub 绿格子只统计满足特定条件的活动；因此它适合作为活动痕迹，不足以单独代表生产力。
- 2016 年移除公开连胜计数器后，一项自然实验观察到长连胜、周末活动和“仅一次贡献日”下降，说明显性奖励确实改变行为。
- 反证与限制：论文没有测量工作质量，不能断言下降的活动全是无效劳动；部分参与者在没有计数器后仍完成个人目标。
- 可用判断：上线计数型习惯反馈时，应同时观察目标任务完成、协作质量、仅一次行为日、非工作时段活动与自报压力。

## 中文研究底稿

**研究问题**

当产品把每日活动公开计数时，它是在帮助用户形成有效习惯，还是把注意力移向可计数行为？合理选项包括原始活动热图、显性连胜计数、基于结果的里程碑，以及不显示持续性分数。冲突在于即时反馈与社会信号有激励价值，但指标覆盖不完整，也可能带来补格子、周末劳动和自我比较压力。

**关键事实**

1. GitHub 当前文档把建仓库、fork 列为始终计入；issue、PR、review、discussion、answer、commit 只在满足条件时计入。commit 需要关联账号的邮箱、非 fork 仓库、默认分支或 `gh-pages` 分支，并满足协作者、组织成员、fork、issue 或 PR 关系中的至少一项。私有贡献可选择只公开每日数量，不公开细节。
2. GitHub 在 2016-05-19 的产品更新中移除了 code streaks，并公开表述为让界面关注工作本身，而非活动持续时长。这是团队陈述的设计意图，不是效果证据。
3. Moldon、Strohmaier 与 Wachs 的 ICSE 2021 论文以计数器突然移除为自然实验，样本为 433,138 名可推断地理位置、至少 100 次 commit 的开发者，包含超过 2.9 亿次有效贡献。移除后长连胜、周末贡献占比和仅一次贡献日下降；部分参与“100 Days”项目的人停止连胜。
4. 论文限制包括样本只含可推断位置的用户、连胜计算对缺失数据敏感、commit 时间可被修改，以及只观察移除而未观察引入。论文没有直接测量代码质量、任务价值或健康状态。
5. GitHub 2025 年官方资源也认为代码行数会激励错误行为，且绿格子不能呈现开发者一天中的全部工作；这是企业团队观点，可支持问题定义，不能替代独立因果证据。

**解释、反证与边界**

- 证据支持“显性计数器改变行为”，但不支持“所有下降的活动都是无效劳动”。周末活动减少可以解释为压力下降，也可能意味着失去有用动力。
- 部分 100 天挑战参与者在计数器移除后仍达到目标，说明个人承诺、日志和社群也能维持习惯；显性平台计数并非唯一机制。
- 当前贡献热图仍存在，因此研究比较的是“有无公开连胜计数器”，不是“有无任何活动可视化”。
- 本判断适用于学习、创作与协作类产品的频次指标；若某项高频行为本身就是经过验证的目标结果，计数可能更可靠。

**本次新增认识**

进度界面同时是一套纳入与排除规则。产品若没有验证活动次数与目标结果的关系，应把它定位为 activity trace，而不是 productivity score。可证伪假设是：显性计数若能提高有意义的任务完成与长期回访，同时不集中增加仅一次行为日和非工作时段活动，才算与目标对齐。

**未解决问题**

缺少将绿格子暴露程度与代码质量、协作成果、长期留存和主观压力连接起来的实验。更强的产品验证应比较活动热图、连胜计数与结果里程碑，并同时记录这些结果指标和副作用指标。

## 来源清单（核查日期：2026-10-29）

1. GitHub Docs, Profile contributions reference（当前计入规则与私有贡献展示）：[来源 1](https://docs.github.com/en/account-and-profile/reference/profile-contributions-reference)[^source01]
2. GitHub Blog, More contributions on your profile（2016 年移除 code streaks 与官方设计表述）：[来源 2](https://github.blog/news-insights/product-news/more-contributions-on-your-profile/)[^source02]
3. Moldon, Strohmaier & Wachs, ICSE 2021（自然实验、样本、结果与限制）：[来源 3](https://doi.org/10.1109/ICSE43902.2021.00058)[^source03]
4. 论文开放版本：[来源 4](https://d-nb.info/1240689934/34)[^source04]
5. GitHub, Beyond green squares: Effectively driving productivity（2025 年官方团队观点）：[来源 5](https://github.com/resources/insights/effectively-driving-productivity)[^source05]

## 长度核验

按 X 普通帖加权规则估算（URL 计 23）：1/5 262；2/5 247；3/5 264；4/5 266；5/5 272。均不超过 280。

## 核查来源

原始来源与对应关系保留在上文。本节仅整理可点击的链接索引；原研究核查日期为 2026-10-29。

1. [来源 1](https://docs.github.com/en/account-and-profile/reference/profile-contributions-reference)
2. [来源 2](https://github.blog/news-insights/product-news/more-contributions-on-your-profile/)
3. [来源 3](https://doi.org/10.1109/ICSE43902.2021.00058)
4. [来源 4](https://d-nb.info/1240689934/34)
5. [来源 5](https://github.com/resources/insights/effectively-driving-productivity)

## 发稿前检查

本节为归档阶段整理。稿件结构、正文长度和引用交由检查工具核对；事实、推断与反例仍以原研究为据。人工审稿待完成，未记录平台发布。


## 归档格式检查

本次使用官方 twitter-text 3.1.0 重新计数；不以原稿的手工计数作为最终结果。

英文加权长度：262 / 247 / 264 / 266 / 272。

中文加权长度：143 / 174 / 157 / 180。

格式检查不代表人工批准或平台发布。

[^source01]: [来源 1](https://docs.github.com/en/account-and-profile/reference/profile-contributions-reference)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source02]: [来源 2](https://github.blog/news-insights/product-news/more-contributions-on-your-profile/)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source03]: [来源 3](https://doi.org/10.1109/ICSE43902.2021.00058)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source04]: [来源 4](https://d-nb.info/1240689934/34)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source05]: [来源 5](https://github.com/resources/insights/effectively-driving-productivity)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
