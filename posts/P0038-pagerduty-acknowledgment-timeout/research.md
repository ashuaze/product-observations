# P0038 研究底稿

核查日期：2026-11-14（北京时间）。P34–P40 研究问题：多人协作中，产品怎样让下一棒知道该做什么？

## 中文审稿摘要

- PagerDuty 的确认接手会停止当前升级，事件仍未解决。
- 两种计时分别应对无人接手和接手后仍未解决；后者是可选的服务设置，官方当前文档写明默认关闭。
- 重新呼叫可以覆盖接手后失联，也可能打断有人持续处理的慢故障。应看后备何时有用。
- 核查的是文档规则；未进行真实呼叫或故障演练。

## 中文研究底稿

**研究问题。** 同一次夜间收银故障，第一位值班人已确认接手。系统应该保持安静直到解决，还是到点重新呼叫？两种方案固定故障、人员和首轮升级策略，仅改变接手后的重新触发规则。

**事实与边界。** 按配置执行升级的事件，第一层先收到通知；若无人确认、解决或改派，达到升级超时可转下一层（如有配置）。确认接手暂停当前升级，不能替代解决状态。[^esc][^incident] 服务可启用确认超时，默认关闭；启用后未解决事件可重新触发，已分配人员再次收到通知，轮班已经交替时也会通知当前值班者。重新触发不等于直接跳至下一层。已确认事件还可以由响应者主动暂缓呼叫，超时未解决则按通知规则重新通知；加派响应者等操作另有规则。[^settings][^snooze]

**比较与反例。** 不设确认超时：允许正在排障的人持续工作，避免无助于修复的重复呼叫；若对方误触确认、失联或换班后无人跟进，可能长期停留在已确认。设确认超时：为无人继续处理提供兜底，但系统看的是未解决状态，不观察进展。反例是响应者正等待正在执行的数据恢复，有人持续监控，此时再呼叫更多人未必有帮助。亦可用主动暂缓或人工检查点作为补充，但依赖有人执行。这里比较方案，不推断厂商采用默认值的动机或效果。

**新增认识与验证。** [P35](../P0035-zendesk-waiting-ticket-statuses/research.md) 区分等待谁和哪条时限继续走；[P37](../P0037-google-docs-task-handoff/research.md) 区分派发与承诺；本期补上「接手后谁来确认进展没有中断」。做两种桌面模拟：接手后失联、确认后持续排查但慢恢复。比较实际无人处理的时长、无新增帮助的分页次数和恢复用时。若重呼叫没有缩短失联空档却增加无效打断，优先改成更晚或人工确认的检查点。未实测，阈值和行为效果待定。

## 核查来源

均于 2026-11-14 打开核查。

[^esc]: PagerDuty Docs，Escalation Policy Basics：首轮通知、升级超时和确认后的停止规则。https://docs.pagerduty.com/incident-management/schedules/escalation-policies
[^settings]: PagerDuty Docs，Configurable Service Settings：确认超时默认值、重触发与轮班通知。https://docs.pagerduty.com/incident-management/services/configurable-service-settings
[^snooze]: PagerDuty Docs，Edit Incidents：已确认事件的主动暂缓及其例外。https://docs.pagerduty.com/incident-management/incidents/edit-incidents
[^incident]: PagerDuty Docs，Incidents Overview：确认接手和解决的状态区别。https://docs.pagerduty.com/incident-management/incidents/overview

## 发稿前检查

- 对同一次故障只切换接手后的处理方案；把同时有人处理的慢恢复保留为反例。
- 文档支持状态和通知条件；是否缩短无人处理时间需另测。
- 产品决策：分别定义无人接手与接手后失联的处理动作，并用两场演练验收。
- 官方 twitter-text 3.1.0 加权长度：英文 [198, 254, 253, 229]；中文 [110, 138, 138, 132]。均不超过 280。
