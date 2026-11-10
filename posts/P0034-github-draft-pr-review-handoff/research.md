# P0034 研究底稿

核查日期：2026-11-10（北京时间）。P34–P40 周期问题：多人协作中，产品怎样让下一棒知道该做什么？本篇聚焦还没完成的工作何时应该进入评审。

## 中文审稿摘要

- GitHub 草稿 PR 让团队先看到改动；草稿不能合并，也不会自动向相关代码负责人发出评审请求。转为可评审会触发相应请求，合并仍需符合仓库要求。
- 同一次结账改动，如果只卡在老购物车价格规则，可以用草稿把问题交给能拍板的人；如果整份改动已值得评审，马上发正式请求可能比等全部打磨完更合适。
- 草稿不应屏蔽所有反馈。GitLab 的草稿合并请求默认照常跑流水线，说明自动反馈和人工接手可以分开。
- 评估两笔账：评审者在已计划重写的改动上花了多少时间，作者又因等关键决策耽误多久。现有证据支持产品规则，没有证明哪种流程普遍更高效。

## 中文研究底稿

**研究问题。** 工程师改结账流程，一处业务决策还没定，其他部分已可分享。协作者既可能提供早期反馈，也可能是完整评审的负责人。应该先展示进展并定向求助，还是立即启动完整评审？比较固定同一版本、同一任务与相同人员，避免把不同阶段的改动拿来比较。

**事实与对应来源。** 在 GitHub，草稿 PR 不能合并，草稿阶段不会自动请求代码负责人评审；标为可评审才会向适用的负责人发出自动请求。自动路由依赖目标分支的 CODEOWNERS 和路径匹配，审批要求另由仓库配置决定。转回草稿也不会取消现有订阅。[^gh][^stage][^owners][^protection] GitLab 的草稿合并请求也不能合并，默认和标为就绪的请求运行相同流水线；项目可以配置跳过。GitLab 文档适用 GitLab.com、Self-Managed 和 Dedicated；这不代表 GitHub 的工作流采用同样规则。[^gl]

| 同一改动的处理方式 | 可能收益 | 代价或失败条件 |
|---|---|---|
| 草稿先共享，指名请一人决定旧购物车是否保留原价 | 先解决会改写较多代码的一项问题，其他人可先看进度 | 若没人接到明确请求，关键决定可能拖延；作者仍要记得启动正式评审 |
| 直接启动完整评审 | 整体反馈较早进入工作流，适合大部分改动已稳定且反馈本来就有时效的情形 | 若决定一改就要重写较多内容，部分评审时间可能花在即将作废的改动上 |

**反例与解释。** GitLab 草稿照跑流水线，反驳的是「草稿应当等到就绪才接收反馈」。自动测试可让作者继续推进，与整份改动需不需要同事现在评审是不同问题。反过来，测试开销很大时可以另设运行策略；已有订阅和其他通知也不能用 GitHub 的草稿标识一概推断。以上是机制对照，不能据此判定某平台或流程更快。

**本次新增判断与适用边界。** [P24 已读回执](../P0024-read-receipts-response-pressure/research.md)分开了「看见」和「应回复」；[P33 隐私默认值综合](../P0033-privacy-defaults-boundary-review/research.md)要求从接收方核对结果。本期把两点转成协作评审方法：在同一份改动上分别检查谁能看到、谁现在需要给意见、谁的批准才允许合并。若只需一个决定，给作者一个点名、写问题、注明时限的动作；若整体反馈已可用，允许直接走正式评审。对于固定两人协作且两种请求常常是同一人同一动作的场景，多个状态可能徒增步骤。

**待验证。** 未进行真实仓库体验或用户试验。可用同一组改动和相同的交付时限测试「直接完整评审」与「先草稿、可定向求助」，记录已计划重写部分的评审分钟数、关键决定等待时间、未响应的请求及完成完整评审所需时间。若草稿流程只延后决定、没有节省评审时间，或导致本该启动的评审被遗漏，就应缩小适用范围或保留直接评审入口。没有账号运营数据可据此评估发布表现。

## 核查来源

以下官方文档均于 2026-11-10 重新打开核查。它们支持功能与配置条件，不提供流程效率的对照数据。

[^gh]: GitHub Docs，《Pull requests》：草稿的可合并性和评审请求。https://docs.github.com/en/pull-requests/reference/pull-requests
[^stage]: GitHub Docs，《Changing the stage of a pull request》：草稿与可评审的转换、权限及订阅限制。https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/changing-the-stage-of-a-pull-request
[^owners]: GitHub Docs，《About code owners》：相关代码负责人、适用计划与目标分支条件。https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
[^protection]: GitHub Docs，《About protected branches》：可配置的合并前审批和状态检查。https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
[^gl]: GitLab Docs，《Draft merge requests》：草稿合并限制和默认流水线行为。https://docs.gitlab.com/user/project/merge_requests/drafts/

## 发稿前检查

- 新认识：让团队看见未完工作、让某个人现在作决定、让整份改动进入正式评审，可以分别设计。
- 公平比较：同一改动同一目标；用 GitLab 的实际流水线规则检验「草稿就该等反馈」的过强推论，保留应直接评审的情形。
- 判断依据：看实际由谁收到什么请求，再同时测返工上的评审时间和关键决策等待。
- 官方 twitter-text 3.1.0 加权长度（含序号及随帖 URL）：英文 177 / 213 / 227 / 225 / 249；中文 125 / 157 / 160 / 131 / 186。各条均不超过 280。
