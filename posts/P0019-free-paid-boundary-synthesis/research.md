# P0019 研究底稿

原期号：P19。原研究核查日期：2026-10-26；归档与中文补写日期：2026-11-02。

原材料：[P19-free-paid-boundary-synthesis-2026-10-26.md](https://chatgpt.com/library?file_id=libfile_f1369d58c7108191af1ba6dd6475e3ea&account_id=personal)。来源字节指纹见 metadata.yaml。原文中的“本次”“当前”等表述属于原研究日期，不代表本次归档重新验证了产品政策、价格或研究结果。

英文处理：仅补齐正文串帖序号；原英文词句和段落保持原样。 中文发布稿为本次独立改写。两种语言均为待审草稿。

## 原稿编辑信息

研究主题：P13–P19「免费与付费边界」周期综合。读者价值：用“信号、时点、责任主体、故障范围与证据”评审免费方案，减少错误分类和任务中断。

## 中文审稿摘要

- 免费层是一套分类规则：产品通过模板数、公开性、时长、共享额度、协作身份或商业目的，选择让哪类使用先遇到付费边界。
- 一个可计量的信号未必能准确预测服务成本、用户价值或支付意愿；还要说明免费使用是否为平台创造了值得补贴的外部价值。
- 边界的质量还取决于触发时点、控制权益的人和承担后果的人是否一致，以及失败是否扩散到相邻任务。
- 评估不能只看升级率；任务完成、绕过行为、支持请求、留存、外部贡献和单位成本都可能推翻当前设计。

## 中文研究底稿

### 研究问题

产品如何选择免费与付费之间的计量信号，并让限制以用户能理解、能应对、影响范围可控的方式出现？

### 六个案例形成的判断框架

| 案例 | 计量信号 | 免费层在筛选什么 | 主要反例或失败条件 |
|---|---|---|---|
| P13 Calendly | 可复用 Event Type 数量 | 持续存在的多流程需求 | One-off Meeting 已能覆盖偶发例外；模板数未必预测支付意愿 |
| P14 GitHub Actions | 仓库公开性与 runner 类型 | 可能为生态创造公共价值的使用 | 保密需求无法用公开性换取免费；publicness 不等于支付能力 |
| P15 Zoom / Meet | 会议时长与参与人数 | 长时间同步或持续多人协调 | 限制在任务中途出现，权益由主持人控制，后果由全体参与者承担 |
| P16 iCloud / Google | 跨产品共享存储量 | 账户级容量需求 | 一个产品的用量会阻断邮件、备份或同步等其他任务 |
| P17 Notion | 成员身份与块数量 | 工作区级协作范围 | 页面级访客可能已完成任务；成员边界也可能制造权限碎片 |
| P18 Vercel / Cloudflare | 商业目的或资源消耗 | 经济价值获取，或实际基础设施成本 | 用途难判断；用量可测但未必对应支付能力 |

### 综合判断

**一、信号要能解释。** 免费限制首先是一项分类假设：“X 行为比其他行为更能预测成本、获得的价值或支付意愿。”模板数量、成员身份和商业目的都可能成立，但便利计数本身不是证据。

**二、补贴与分层要分开。** GitHub 的公开仓库规则说明，免费额度也可以奖励为平台带来外部价值的行为。此时应同时验证生态收益和资源成本，不能把公开性直接当作支付能力。

**三、限制时点与责任主体要匹配。** Zoom 和 Meet 的时长边界会在共同任务中触发；主持人控制套餐，所有参与者承担中断。对协作任务，应在承诺前或足够早地预警，并让能采取行动的人看到选择。

**四、故障范围应与计量范围相称。** iCloud 与 Google 的共享池提供容量分配灵活性，但满额会影响多个产品。共享资源并非问题本身；关键是用户能否预见哪个任务将先失败，以及能否在不误删重要内容的情况下恢复。

**五、免费替代路径需要验收。** Calendly One-off、Notion Guest、重新开会或清理存储都可能是有意保留的低频路径，也可能成为重复劳动。应判断它是否真正完成用户任务、是否只是绕过收费，以及额外成本由谁承担。

### 可用于评审的最小表述

在上线边界前，团队应能完成以下陈述：

> 我们计量 **X**，因为它预计能预测 **成本、用户价值或支付意愿 Y**。  
> 在任务 **Z** 失败之前，主体 **A** 能看到并采取行动。  
> 不升级的用户仍能通过 **F** 安全完成范围较小的任务。  
> 我们将同时观察升级、任务完成、绕过、支持、留存、外部贡献与单位成本。  
> 如果出现 **E**，我们会调整计量信号、阈值、时点或失败方式。

### 反证与可推翻条件

- 若在控制真实用量后，模板数、成员数或商业标签不能预测购买，应换用更接近任务或成本的信号。
- 若用户频繁重开会议、重复建链接、把成员改成访客或危险清理数据，说明免费路径可能在制造忙碌而不是合理分层。
- 若限制显著影响无权购买的人、关键任务或相邻产品，应改变触发时点、责任主体或故障范围。
- 若公共免费使用产生的复用、贡献或获客价值超过成本，扩大补贴可能比收紧限额更合理。
- 相反，如果任务在边界前已经完整完成、替代路径成本低且单位经济恶化，收紧限额可能有依据。

### 证据边界与本次新增认识

本周期公开材料支持功能、套餐和政策事实，没有各公司内部的转化、利润、留存、违规或实验数据。因此，关于商业动机和效果的内容均为可检验分析。

本次新增的综合认识是：免费层需要同时通过三类检验——经济上能预测，任务上可理解，故障上可控制。任何一项缺失，都可能把升级信号变成错误分类或任务事故。

本次没有获得 @azeashu 的真实曝光、具体回复、重复读者或关注变化数据，因此不评价账号表现，也不把结果归因于英文运营。

## 来源清单（重新核查日期：2026-10-26）

1. Calendly Pricing — [来源 1](https://calendly.com/pricing)[^source01]
   - 核实 Free 一个 Event Type、Standard 无限 Event Types。
2. Calendly, “How to create a One-off Meeting” — [来源 2](https://calendly.com/help/how-to-create-a-one-off-meeting)[^source02]
   - 核实一次性链接、自定义时段、用后失效与不可改期。
3. GitHub, “GitHub Actions billing” — [来源 3](https://docs.github.com/en/billing/concepts/product-billing/github-actions)[^source03]
   - 核实公共仓库标准托管 runner 免费、私有仓库按计划获得额度。
4. Zoom, “Understanding time limits for Zoom Meetings” — [来源 4](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0067966)[^source04]
   - 核实 Basic 几乎所有会议 40 分钟、付费许可证通常 30 小时。
5. Google Meet access requirements — [来源 5](https://support.google.com/meet/answer/7317473?hl=en)[^source05]
   - 核实无订阅账户双人会议最长 24 小时、三人及以上 60 分钟，并在第 50 分钟提醒。
6. Apple, “Manage your iCloud storage” — [来源 6](https://support.apple.com/en-us/108922)[^source06]
   - 核实 5 GB 免费共享空间及满额后备份、照片、Drive、应用同步和邮件影响。
7. Google, “Manage your storage in Drive, Gmail & Photos” — [来源 7](https://support.google.com/drive/answer/6374270?hl=en)[^source07]
   - 核实最多 15 GB 共享空间及满额后 Drive、Photos、Gmail 的影响。
8. Notion, “Understanding block usage” — [来源 8](https://www.notion.com/help/understanding-block-usage)[^source08]
   - 核实单人免费工作区不限块、多人工作区 1,000 块、三天宽限及 Guest 替代路径。
9. Vercel, “Fair Use Guidelines” — [来源 9](https://vercel.com/docs/limits/fair-use-guidelines)[^source09]
   - 核实 Hobby 的个人非商业限制和商业用途定义；页面更新于 2026-09-14。
10. Cloudflare Workers Pricing — [来源 10](https://developers.cloudflare.com/workers/platform/pricing/)[^source10]
    - 核实 Free 请求量和 CPU 时间规则；页面更新于 2026-10-02。

## 核查来源

原始来源与对应关系保留在上文。本节仅整理可点击的链接索引；原研究核查日期为 2026-10-26。

1. [来源 1](https://calendly.com/pricing)
2. [来源 2](https://calendly.com/help/how-to-create-a-one-off-meeting)
3. [来源 3](https://docs.github.com/en/billing/concepts/product-billing/github-actions)
4. [来源 4](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0067966)
5. [来源 5](https://support.google.com/meet/answer/7317473?hl=en)
6. [来源 6](https://support.apple.com/en-us/108922)
7. [来源 7](https://support.google.com/drive/answer/6374270?hl=en)
8. [来源 8](https://www.notion.com/help/understanding-block-usage)
9. [来源 9](https://vercel.com/docs/limits/fair-use-guidelines)
10. [来源 10](https://developers.cloudflare.com/workers/platform/pricing/)

## 发稿前检查

本节为归档阶段整理。稿件结构、正文长度和引用交由检查工具核对；事实、推断与反例仍以原研究为据。人工审稿待完成，未记录平台发布。


## 归档格式检查

本次使用官方 twitter-text 3.1.0 重新计数；不以原稿的手工计数作为最终结果。

英文加权长度：265 / 275 / 276 / 272 / 280 / 267。

中文加权长度：150 / 188 / 154 / 150 / 166。

格式检查不代表人工批准或平台发布。

[^source01]: [来源 1](https://calendly.com/pricing)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source02]: [来源 2](https://calendly.com/help/how-to-create-a-one-off-meeting)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source03]: [来源 3](https://docs.github.com/en/billing/concepts/product-billing/github-actions)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source04]: [来源 4](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0067966)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source05]: [来源 5](https://support.google.com/meet/answer/7317473?hl=en)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source06]: [来源 6](https://support.apple.com/en-us/108922)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source07]: [来源 7](https://support.google.com/drive/answer/6374270?hl=en)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source08]: [来源 8](https://www.notion.com/help/understanding-block-usage)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source09]: [来源 9](https://vercel.com/docs/limits/fair-use-guidelines)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source10]: [来源 10](https://developers.cloudflare.com/workers/platform/pricing/)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
