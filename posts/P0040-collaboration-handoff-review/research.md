# P0040 研究底稿

核查日期：2026-11-16（北京时间）。P34–P40「协作交接与责任」周期综合。

## 中文审稿摘要

- 只有当状态差异会改变下一步行动、验收对象或兜底规则时，才值得在界面上拆开。
- 草稿可见并不等于启动评审；版本看似未变也不代表关键共享值未变；确认接手不代表事件已解决。
- 两队追踪同一套截图时，共享完成状态有价值。邮件单独验收时应有自己的任务；起草无需等待最终截图。
- 建议用同一次上线的正常路径与变更路径检验两种设计。本期只有文档规则与设计推断，无行为效果数据。

## 中文研究底稿

**问题。** 多人推进同一次上线，团队何时应共享一个状态，何时该拆成独立信号？固定参与者、交付和截止时间，比较共享总项与按行动拆分。

| 交接环节 | 已核查的事实 | 可用于评审的判断 |
|---|---|---|
| 启动 | GitHub 草稿 PR 不会自动向相关代码负责人请求评审。Zendesk 标准客户门户区分等待请求者回复与 Open；可选内部 On-hold 对客户仍显示 Open。[^gh][^zd] | 分开谁能看见与谁现在要动作；不必对客户暴露无须其处理的内部状态。 |
| 依据与变更 | Figma 图层已绑定变量改值不触发 Changed；Google Docs 只删清单行，已创建的任务仍可留在接手者列表。[^fg][^gd] | 验收接手方实际看见的版本和承诺；删来源和取消工作可有不同结果。 |
| 接手与结束 | PagerDuty 确认接手暂停升级但不解决事件；服务可选确认超时，默认关闭。Asana 同一任务关联多个项目时，共享完成状态。[^pd][^timer][^as] | 接手与解决分别记录；只在确实是同一交付时共用完成状态。 |

**反例与取舍。** 同一套最终截图供两队追踪时，拆成两条独立完成项会增加同步工作；但截图和邮件各自验收时，一个完成勾选可能掩盖没发的邮件。若发送需要截图而起草不需要，只约束发送。对较轻且频繁的交接，可先使用一条共享总项和明确下一步说明；对误执行代价高、跨班次或跨团队的步骤，优先把接手条件与完成条件写明，仅在需要驱动不同操作时另设状态。

**新增认识与待验证。** 回读 [P0034](../P0034-github-draft-pr-review-handoff/research.md)、[P0035](../P0035-zendesk-waiting-ticket-statuses/research.md)、[P0036](../P0036-figma-dev-mode-handoff-version/research.md)、[P0037](../P0037-google-docs-task-handoff/research.md)、[P0038](../P0038-pagerduty-acknowledgment-timeout/research.md)、[P0039](../P0039-asana-shared-task-completion/research.md)。本期增加一个取舍标准：把标签先当作对接手人的指令，只有两种情形会导致不同动作，且文案或字段不足以传达时，再加状态。用同一个上线场景做配对模拟：一场如期完成，一场中途重做截图或取消邮件。比较共享总项和独立状态下，接手者能否正确判断下一步、所据版本、完成条件；记录漏做、误发及新增确认次数。若轻量方案同样准确而确认更少，保留单一状态；若多人依然误发，可能还需要明确的发送前核对，而非继续增加标签。未实测产品或团队行为，结论不用于判断账号运营效果。

## 核查来源

以下官方文档于 2026-11-16 打开核查；只支持表内功能规则。Zendesk 用标准门户映射，Figma 与 Google Docs 功能受席位或账号条件限制，Asana 的项目可见性取决于权限。

[^gh]: GitHub Docs，Pull requests。https://docs.github.com/en/pull-requests/reference/pull-requests
[^zd]: Zendesk Help，What are the customer portal ticket statuses? https://support.zendesk.com/hc/en-us/articles/4408825864858-What-are-the-customer-portal-ticket-statuses
[^fg]: Figma Learn，Dev Mode statuses and notifications。https://help.figma.com/hc/en-us/articles/26781702258583-Dev-Mode-statuses-and-notifications
[^gd]: Google Docs Editors Help，Assign tasks from Google Docs。https://support.google.com/docs/answer/12048749?hl=en
[^pd]: PagerDuty Docs，Escalation Policy Basics。https://docs.pagerduty.com/incident-management/schedules/escalation-policies
[^timer]: PagerDuty Docs，Configurable Service Settings。https://docs.pagerduty.com/incident-management/services/configurable-service-settings
[^as]: Asana Help Center，Task fields。https://help.asana.com/s/article/task-fields

## 发稿前检查

- 以同一次上线对照两种状态设计；共享同一套截图是反例，限制了「拆得越多越好」的推断。
- 新判断是从接手者的动作决定是否增加状态；漏做、误发与确认成本可以推翻建议。
- 官方 twitter-text 3.1.0 加权长度：英文 [228, 252, 265, 241, 256]；中文 [148, 157, 144, 128, 148]。均不超过 280。
