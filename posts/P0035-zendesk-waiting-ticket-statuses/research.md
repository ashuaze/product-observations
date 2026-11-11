# P0035 研究底稿

核查日期：2026-11-11（北京时间）。P34–P40 周期问题：多人协作中，产品怎样让下一棒知道该做什么？

## 中文审稿摘要

- 同一宗丢件，客服可能等客户给订单号，也可能等承运商查件。两种情况都暂时不能结案，但客户该做的事不同。
- Zendesk 的标准状态中，Pending 是等请求者；启用后的 On-hold 是等其他人。客户门户分别显示 Awaiting your reply 和 Open。
- 对已配置且适用的 SLA，Agent Work Time 在两种等待下都暂停；Requester Wait Time 只在 Pending 暂停。Total Resolution Time 则把两类等待都算进去。
- 单一「等待中」标签也可以成立，只要另有可靠字段说明谁要行动，以及哪个时限继续计算。此判断是设计建议，未实测效率。

## 中文研究底稿

**研究问题。** 同一个客服工单暂停推进时，界面是否应该为等待客户和等待合作方使用不同状态？比较同一宗丢件、同一个客服与客户，只改变谁能提供下一项必要信息。客户要知道是否需要回复；客服即使不掌握承运商的行动，也仍可承担跟进和更新的责任。

**事实与对应来源。** Zendesk 的标准 Pending 表示等请求者补资料；其回复新增评论时工单自动回到 Open。On-hold 是可由管理员启用的内部状态，表示等待请求者以外的人处理。标准客户门户显示 Pending 为 Awaiting your reply、On-hold 为 Open。定制状态可显示不同名称，旧自定义主题可能需要更新以使用新版请求列表。[^life][^portal]

**计时边界。** 对已经匹配政策、具有系统优先级且设置了相应目标的工单，Agent Work Time 在 Pending 和 On-hold 都暂停，Requester Wait Time 在 Pending 暂停、在 On-hold 累计。Total Resolution Time 在两类等待都累计；计算可按营业或自然时间配置，已解决后重开另有规则。Agent Work Time 是按状态累计的 SLA 指标，不能当作人工实际工作量。[^sla]

| 同一工单的设计选项 | 收益 | 代价或失败条件 |
|---|---|---|
| 等客户和等承运商使用不同状态，按角色显示下一步 | 状态本身就能区分客户要不要回复，也可驱动不同计时 | 状态多了会选错；把等承运商误记为 Pending 会让客户以为要回复，并暂停请求者等待指标 |
| 统一显示「等待中」，另记录等待对象、客户需做的事和时限 | 列表更简洁；同一条端到端承诺可跨等待原因延续 | 如果独立字段缺失、过期或与计时不一致，简单标签就会掩盖下一步 |

**反例与新增认识。** 有些承诺就是从受理到解决，无论在等谁都应继续计。Zendesk 的 Total Resolution Time 是现实反例，说明「改变等待对象」不必带来「暂停时限」。另一方面，只用端到端时间无法区分客服何时可以继续处理。回读 [P34](../P0034-github-draft-pr-review-handoff/research.md)：上一篇区分看见和接手；本篇再把当前阻塞方、仍需跟进的人、按承诺计入的时间分开。

**待验证。** 用两张除等待对象外相同的模拟工单，对比双状态和单状态加字段。让客服和客户各自判断下一步，再核对同一时间线里的目标是否按承诺累计。记录误催客户、漏跟进承运商、错停时限及维护字段的时间；若单一标签同样准确且维护成本更低，就不必新增状态。未使用真实工单或测试账号，文档不能证明某方案改善服务效率。

## 核查来源

均于 2026-11-11 打开核查。

[^life]: Zendesk，《About the ticket lifecycle and ticket statuses》：标准状态、回复后的转换、On-hold 可选。https://support.zendesk.com/hc/en-us/articles/8263915942938-About-the-ticket-lifecycle-and-ticket-statuses
[^portal]: Zendesk，《What are the customer portal ticket statuses?》：客服端与客户门户状态映射、主题及定制边界。https://support.zendesk.com/hc/en-us/articles/4408825864858-What-are-the-customer-portal-ticket-statuses
[^sla]: Zendesk，《Defining SLA policies》：三种解决时间指标、计时条件及适用规则。https://support.zendesk.com/hc/en-us/articles/4408829459866-Defining-SLA-policies

## 发稿前检查

- 对同一宗丢件只更换等待对象；比较状态拆分和字段拆分，检查双方能否正确说出下一步。
- 用 Total Resolution Time 检查「等待就停表」的反例；只把官方文档用于规则，未推断实际提效。
- 读者可先写清下一步、跟进责任和时限，再决定是否需要新增状态。
- 官方 twitter-text 3.1.0 加权长度（含序号及随帖 URL）：英文 205 / 193 / 208 / 241；中文 128 / 139 / 136 / 170。各条均不超过 280。
