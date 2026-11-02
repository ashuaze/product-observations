# P0021 研究底稿

原期号：P21。原研究核查日期：2026-10-28；归档与中文补写日期：2026-11-02。

原材料：[P21-notification-batching-cadence-2026-10-28.md](https://chatgpt.com/library?file_id=libfile_fc9677d2ed148191b7cbf6ea542ddb67&account_id=personal)。来源字节指纹见 metadata.yaml。原文中的“本次”“当前”等表述属于原研究日期，不代表本次归档重新验证了产品政策、价格或研究结果。

英文处理：正文词句和段落保持原样；移除写作块包装与标题中的字符统计。 中文发布稿为本次独立改写。两种语言均为待审草稿。

## 原稿编辑信息

**研究主题：** 习惯设计的收益与副作用  
**读者价值：** 把通知从“开或关”的二元设置，重构为即时、延迟与关闭三种节奏选择，并避免用打开率代替用户注意力质量。

## 中文审稿摘要

- 通知不仅是信息载体，也是回访触发器；设计变量不只有数量，还有到达节奏、紧急例外与用户控制权。
- iPhone 的 Scheduled Summary 允许选择应用和摘要时间；应用可选择即时或摘要发送，Time Sensitive 通知保持即时。
- 一项两周随机实验发现，每天三批通知比正常即时到达减少解锁，并改善参与者自报的专注、控制感和生产力；每小时一批则几乎没有差异。
- 完全不发送通知虽减少打扰，却增加通知相关 FoMO 和焦虑，且没有改善注意力；但另一项一天的工作情境实验得到“关闭通知有益”的结果，说明控制权、时间长度和任务场景会改变结论。
- 当前公开证据不能证明 Apple 的 Scheduled Summary 会复制实验结果，也不能证明任何平台采用通知机制的商业动机。

## 中文研究底稿

### 研究问题

对需要让用户及时知情、又不希望持续打断任务的产品，通知应该即时送达、固定批次送达，还是完全关闭？三种方案分别优化响应速度、注意力连续性和打扰最小化，但它们可能引发不同的自查、错过焦虑与紧急信息损失。

### 当前产品事实

Apple 当前 iPhone 用户指南说明：

- Scheduled Summary 允许用户选择纳入摘要的应用和送达时间；可以添加多个摘要时点。
- 摘要会个性化排序，把系统判断更相关的通知放在上方。
- 单个应用可以选择 Immediate Delivery 或 Scheduled Summary。
- Apple 将 Time Sensitive 定义为需要立即关注和行动的信息，并说明该类通知始终即时送达。

这形成了三个通道：即时、延迟摘要、关闭。它比统一静音多了一层任务分类，但排序和紧急标记也可能误判。

### 效果证据

Fitz 等人在 2019 年发表的随机现场实验招募 237 位居住在印度的 Android 用户。所有参与者先经历一周基线，随后两周被分配至四组：正常通知、每小时一批、每天三批（9:00、15:00、21:00）或不发送系统通知；消息仍可通过主动打开应用查看。

- **每天三批：** 相比正常通知，参与者解锁次数更少，自报的控制感、专注与生产力更高，压力更低；部分通知相关 FoMO 仍然上升。
- **每小时一批：** 除“感觉被通知打断”这一单项指标外，与正常通知大多没有差异。固定时点本身不够，间隔可能必须足以形成真正的专注窗口。
- **不发送通知：** 感觉被打断更少，但没有改善不专注或集中程度，并增加了通知相关 FoMO、错过重要通知的感觉和焦虑。

研究的主要结果多数来自自报；可靠行为数据有限，实验仅两周，样本来自一个国家，且采用统一批处理，无法代表按应用、任务或紧急程度分类的真实产品。中介分析也不能证明“注意力或 FoMO 导致了后续结果”。

### 相反证据与竞争解释

2023 年另一项随机现场实验让 247 位参与者中的实验组在一个工作日尽可能关闭通信通知，但允许保留重要通知。该研究发现，减少通知打断与更好的自报绩效、较低压力相关；绩效收益在 FoMO 较低或工作回复压力较高的人群中更明显。

两项实验并不直接冲突：前者使用两周、由应用强制执行的“完全不发通知”；后者只有一天、保留紧急例外并允许参与者自行配置。控制权、实验长度、任务类型和社会回复规范都可能改变效果。后一项研究同样依赖自报，并只有一天，不能证明长期结果。

### 解释、边界与判断

- **推断：** 通知设计的关键不是一味减少数量，而是让延迟成本与打断成本匹配。固定节奏可以把反应式查看变成计划式回顾。
- **反例：** 安全告警、交易确认、接送变化、实时协作或限时操作会因延迟失去价值，应保留即时通道。
- **失败条件：** 摘要若导致用户更频繁主动刷新、错过关键任务，或把大量通知堆成难以处理的批次，就只是把打扰换成积压。
- **商业边界：** 即时通知可能提高短期打开率，但现有材料不能证明即时、批量或关闭哪一种带来更高长期留存、满意度或收入。

建议按任务将通知分为：

1. **即时：** 延迟会显著降低行动价值或增加风险。
2. **批量：** 用户需要知情，但处理时间可以由用户选择。
3. **关闭或产品内收件箱：** 即使回顾，信息价值也很低。

同时观察通知造成的任务中断、设备解锁、主动自查、摘要清空率、紧急事件漏达、设置退出、次日回访和用户报告的错过焦虑。若批处理只降低通知展示，却提高自查和漏达，应调整批次间隔、紧急分类或让用户恢复控制。

本次没有在真实设备上启用 Scheduled Summary，因此未验证摘要界面、排序结果或实际漏达情况。

## 核查来源

均于 **2026-10-28** 实际打开核查：

1. [Apple iPhone User Guide：View and respond to notifications](https://support.apple.com/guide/iphone/view-and-respond-to-notifications-iph6534c01bc/ios)[^source01]——摘要时间、应用选择与排序说明。
2. [Apple iPhone User Guide：Change notification settings](https://support.apple.com/guide/iphone/change-notification-settings-iph7c3d96bab/ios)[^source02]——单个应用的即时或摘要发送选择。
3. [Apple Developer：Time Sensitive Notifications](https://developer.apple.com/help/glossary/time-sensitive-notifications/)[^source03]——即时送达定义。
4. [Fitz et al. (2019), *Batching smartphone notifications can improve well-being*](https://doi.org/10.1016/j.chb.2019.07.016)[^source04]——四组随机实验、结果与限制。
5. [Ohly & Bastin (2023), *Effects of task interruptions caused by notifications from communication applications on strain and performance*](https://doi.org/10.1002/1348-9585.12408)[^source05]——一天关闭通知的相反证据及 FoMO、工作回复压力边界。

## 发稿前检查

本节为归档阶段整理。稿件结构、正文长度和引用交由检查工具核对；事实、推断与反例仍以原研究为据。人工审稿待完成，未记录平台发布。


## 归档格式检查

本次使用官方 twitter-text 3.1.0 重新计数；不以原稿的手工计数作为最终结果。

英文加权长度：244 / 251 / 270 / 250 / 262。

中文加权长度：138 / 192 / 162 / 158。

格式检查不代表人工批准或平台发布。

[^source01]: [Apple iPhone User Guide：View and respond to notifications](https://support.apple.com/guide/iphone/view-and-respond-to-notifications-iph6534c01bc/ios)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source02]: [Apple iPhone User Guide：Change notification settings](https://support.apple.com/guide/iphone/change-notification-settings-iph7c3d96bab/ios)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source03]: [Apple Developer：Time Sensitive Notifications](https://developer.apple.com/help/glossary/time-sensitive-notifications/)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source04]: [Fitz et al. (2019), *Batching smartphone notifications can improve well-being*](https://doi.org/10.1016/j.chb.2019.07.016)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source05]: [Ohly & Bastin (2023), *Effects of task interruptions caused by notifications from communication applications on strain and performance*](https://doi.org/10.1002/1348-9585.12408)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
