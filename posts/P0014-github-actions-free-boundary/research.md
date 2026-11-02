# P0014 研究底稿

原期号：P14。原研究核查日期：2026-10-21；归档与中文补写日期：2026-11-02。

原材料：[P14_GitHub_Actions_free_boundary.md](https://chatgpt.com/library?file_id=libfile_c89075f2311081919a7f8427cf852fef&account_id=personal)。来源字节指纹见 metadata.yaml。原文中的“本次”“当前”等表述属于原研究日期，不代表本次归档重新验证了产品政策、价格或研究结果。

英文处理：仅补齐正文串帖序号；原英文词句和段落保持原样。 中文发布稿为本次独立改写。两种语言均为待审草稿。

## 原稿编辑信息

- 研究主题：免费与付费边界
- 本篇形式：短观察（4 条串帖）
- 目标读者价值：把免费层从“给多少额度”改写为“平台愿意补贴什么行为”，并区分补贴、容量计费与成本转移。
- 核查日期：2026-10-21

## 中文审稿摘要

- GitHub Actions 的免费边界不只按用量划分，也按仓库公开性划分：公共仓库的标准托管 runner 免费，私有仓库先消耗套餐额度。
- “补贴公开代码以换取生态价值”是本账号的定价分析，不是 GitHub 公开陈述的动机。
- 两个对照揭示真实成本：大型托管 runner 在公共仓库也收费；自托管虽不收 Actions 使用费，但把机器与维护成本转给用户。
- 适用判断：可用免费层奖励能给网络带来价值的公开产出，但不能把公开性当作普遍的付费能力代理；机密代码无法用公开换折扣。

## 中文研究底稿

### 研究问题

当相同类型的 CI 任务既能发生在公共仓库，也能发生在私有仓库时，免费层应该只按资源消耗划线，还是也可以按产出是否为平台生态创造外部价值划线？

### 使用情境与合理选项

1. 公共仓库 + 标准 GitHub-hosted runner：平台承担基础算力，降低开源项目持续集成门槛。
2. 私有仓库 + 标准 GitHub-hosted runner：套餐包含一定额度，超额计费；保密需求不能通过“公开”来换取免费。
3. 公共或私有仓库 + larger runner：性能和稀缺容量单独计费，不被公共属性覆盖。
4. 自托管 runner：GitHub Actions 侧免费，但算力、维护、更新与安全责任转移给用户。

### 关键事实及对应来源

- 事实：GitHub Actions 对自托管 runner 免费；公共仓库使用标准 GitHub-hosted runner 免费。私有仓库按套餐获得免费分钟与存储额度；启用付费用量后超额计费，未配置有效付款方式时用尽额度会被阻止。  
  来源：[GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions)[^source01]
- 事实：当前文档列出的私有仓库标准 runner 月度分钟额度因套餐而异；本篇不写具体数字，因为数字本身不改变分析结论，也更容易随套餐更新。
- 事实：larger runners 即使在公共仓库也收费，且套餐包含的分钟不能抵扣 larger runner 使用。  
  来源：[Actions runner pricing](https://docs.github.com/en/billing/reference/actions-runner-pricing)[^source02]
- 事实：自托管 runner 在 GitHub Actions 中免费，但用户负责机器维护成本，并负责更新操作系统及其他软件。  
  来源：[Self-hosted runners](https://docs.github.com/en/actions/concepts/runners/self-hosted-runners)[^source03]
- 事实/安全边界：GitHub 建议自托管 runner 只用于私有仓库，因为公共仓库的 fork 可能通过 pull request 在 runner 上执行危险代码。  
  来源：[Adding self-hosted runners](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/add-runners)[^source04]

### 解释、反证与竞争解释

- 解释（本账号推断）：把公共仓库的标准算力设为免费，可能是在补贴能带来贡献者、可复用工作流和生态活动的公开产出。
- 证据边界：官方文档只说明计费规则，没有说明商业动机；因此正文使用 “One plausible reading”，不把推断写成 GitHub 的公开意图。
- 反例 1：公共属性并不覆盖稀缺容量。larger runner 在公共仓库仍计费，说明“奖励公开”之外还存在资源成本护栏。
- 反例 2：自托管不是无成本替代，只是从平台账单转移到基础设施、维护与安全账单。
- 反例 3：对必须保密的团队，公开性不是可交易变量，因此不能把“是否公开”当作普遍公平的付费能力代理。
- 竞争解释：公共仓库免费也可能主要服务开发者获取、开源支持或降低计费复杂度；目前没有公开实验可区分这些解释。

### 可用判断与失败条件

- 可借鉴：当用户产出会被他人发现、复用或贡献，平台可以考虑补贴基础使用，再对稀缺容量或高级控制收费。
- 不适用：当公开会暴露机密、客户数据或商业代码时，公开性不是合理的免费门槛。
- 失败条件：若补贴带来的生态贡献无法抵消算力、滥用和支持成本，或免费用户并未产生可复用价值，这一边界就需要调整。
- 可检验假设：与单纯按次数发放免费额度相比，“公共产出免费、稀缺容量计费”应提高公开项目的持续使用与生态复用，同时不显著恶化单位算力成本或滥用率。需要平台侧 cohort、成本与滥用数据才能验证。

### 本次新增认识

免费层不一定只是产品试用期；它也可以是一项补贴政策。设计时应把三个问题拆开：希望奖励什么行为、哪些稀缺资源必须计费、哪些“免费”只是把成本转给用户。

### 未解决问题

- GitHub 未公开说明公共仓库免费分钟的目标函数与效果数据。
- 没有独立数据可判断这项政策对开源贡献、Actions 生态增长或付费转化的净影响。
- 本次未进行账号内账单或 runner 实测；正文仅使用公开文档支持功能事实。

## 发稿前检查

- 熟悉功能者的新认识：免费层可以按生态贡献划分，而不只按使用量划分。
- 核心判断的支持：官方计费差异、自托管成本归属和大型 runner 例外。
- 可推翻证据：若公开仓库免费主要由低管理成本解释，或没有带来可测的生态外部价值，则“补贴公开产出”的解释应弱化。
- 比较公平性：比较的是同一 CI 任务在不同可见性和 runner 供给方式下的收费边界，并明确了保密与安全差异。
- 决策用途：帮助产品团队判断免费层应奖励贡献行为、覆盖基础容量，还是只承担试用获客。
- X 加权长度核验：1/4 为 253；2/4 为 258；3/4 为 251；4/4 为 252。所有帖子均不超过 280；URL 按 23 字符计。

## 核查来源

原始来源与对应关系保留在上文。本节仅整理可点击的链接索引；原研究核查日期为 2026-10-21。

1. [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions)
2. [Actions runner pricing](https://docs.github.com/en/billing/reference/actions-runner-pricing)
3. [Self-hosted runners](https://docs.github.com/en/actions/concepts/runners/self-hosted-runners)
4. [Adding self-hosted runners](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/add-runners)

## 归档格式检查

本次使用官方 twitter-text 3.1.0 重新计数；不以原稿的手工计数作为最终结果。

英文加权长度：253 / 258 / 251 / 252。

中文加权长度：143 / 166 / 149 / 160。

格式检查不代表人工批准或平台发布。

[^source01]: [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source02]: [Actions runner pricing](https://docs.github.com/en/billing/reference/actions-runner-pricing)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source03]: [Self-hosted runners](https://docs.github.com/en/actions/concepts/runners/self-hosted-runners)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source04]: [Adding self-hosted runners](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/add-runners)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
