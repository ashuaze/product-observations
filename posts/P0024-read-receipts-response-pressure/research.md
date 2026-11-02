# P0024 研究底稿

原期号：P24。原研究核查日期：2026-10-31；归档与中文补写日期：2026-11-02。

原材料：[P24-read-receipts-response-pressure-2026-10-31.md](https://chatgpt.com/library?file_id=libfile_299aefdf101481918c7905cea629d368&account_id=personal)。来源 SHA-256 见 metadata.yaml。本次保留原研究内容并补充可移植引用；原文中的“本次”沿用原研究语境。本次归档没有重新核查全部产品规则或论文。

英文处理：英文发布正文保持原样，仅将标题中的字符检查说明移出发布文件。 中文发布稿为本次根据原研究材料独立改写。两种语言均为草稿，待人工审稿。

## 中文审稿摘要

- 核心判断：已读回执不只是状态反馈；它会把“已阅读”压缩成“可回复、应回复”的社会信号，可能加快回应，也可能诱发延迟打开。
- 产品对照：Signal 采用双方都开启才互相可见的互惠契约；iMessage 由接收者决定是否向所有人或单个联系人发送回执。
- 证据边界：调查与访谈支持“猜测、压力和策略性行为”存在，但不能证明回执必然提高回复率或导致焦虑。
- 反证：2025 年美国调查发现，强制互惠虽有隐私损失，许多参与者仍认为它公平、简单，并总体偏好互惠设置。
- 可用判断：高时效协调可以保留“seen”；异步协作更适合把“已读”和“已确认/稍后回复”拆开，并同时观察延迟打开与关闭率。

## 中文研究底稿

### 研究问题

产品怎样利用社交责任降低消息不确定性，同时避免把私人注意力变成未声明的回复义务？合理选项包括：不显示回执、由每位接收者单独控制，以及要求双方互惠后才显示。

### 关键事实与证据

1. **事实｜Signal 的权限契约。** Signal 将已读回执定义为可选功能；双方都开启时，才会显示已读状态。它把“获取对方状态”和“暴露自己的状态”绑定为互惠交换。来源：[Signal Support — Read Receipts](https://support.signal.org/hc/en-us/articles/360007059812-Read-Receipts)[^signal]。

2. **事实｜iMessage 的权限契约。** Apple 允许用户为所有对话开启或关闭“Send Read Receipts”，也可对单个联系人单独设置；用户只能决定自己是否发送，不能替对方开启。来源：[Apple Support — Turn read receipts on or off in Messages on iPhone](https://support.apple.com/guide/iphone/turn-read-receipts-on-or-off-iph5e713a045/ios)[^apple]。

3. **行为证据｜可见状态会改变解释与行为。** 2017 年 CHI 研究分别调查 402 名发送者和 316 名接收者；发送者会对未读或已读未回产生多种情绪，接收者也会利用回复或延迟回复传递信号。该证据来自自报调查，支持“行为与解释会改变”，不支持强因果。来源：[Hoyle et al., 2017 — Was my message read?](https://www.research.ed.ac.uk/en/publications/was-my-message-read-privacy-and-signaling-on-facebook-messenger/)[^hoyle]；DOI 10.1145/3025453.3025925。

4. **行为证据｜发送者推测与接收者原因会错位。** 2022 年 CHI 扎根理论研究整理出已读未回的多类推测、原因与后续策略，并指出双方解释不匹配会制造沟通摩擦。结论强调情境、关系、互动、对话和个人差异，因此不宜把一种规范套给所有关系。来源：[Chou et al., 2022 — Why Did You/I Read but Not Reply?](https://doi.org/10.1145/3491102.3517496)[^chou]。

5. **反证与替代解释｜互惠也可能被视为公平。** SOUPS 2025 对 802 名美国参与者调查三类人际访问控制；强制互惠造成隐私损失，但许多人认为它公平、简单，整体更偏好互惠设置。它反驳了“选项越多越好”和“互惠只有副作用”两种简单结论。来源：[Malkin et al., 2025 — Do You See If I See?](https://www.usenix.org/conference/soups2025/presentation/malkin)[^malkin]。

### 解释、收益与失败条件

- **本账号推断：** 回执把三个不同状态压成一个社会信号：看见消息、现在有能力回复、承诺回复。产品只观测第一个状态，关系规范却可能把它解释成后两个。
- **收益：** 在接送、现场协作、值班或高时效小团队中，“seen”能降低发送者的不确定性，避免重复催促；互惠还可能被理解为双方规则对等。
- **代价：** 在闲聊和异步工作中，用户可能延迟打开、依赖通知预览、关闭回执，或把未回复解释为忽视。此时产品没有消除等待，只把等待前移到“是否打开”。
- **失败条件：** 若任务并不要求即时协调、关系权力不对等，或用户无法轻易控制披露，回执更可能成为隐性监控。跨文化、关系与场景差异很大，现有材料不足以给出统一默认值。

### 产品判断与可检验假设

- 高时效协调：可显示“seen”，但不要把它当作完成或同意；必要时另设明确的确认动作。
- 异步协作：将“已读”“已确认”和“稍后回复”拆开，给接收者一个真实表达可用性的轻量入口。
- 闲聊或隐私敏感关系：优先给予接收者控制；若采用互惠，应清楚说明查看对方状态会同时暴露自己的状态。
- **可检验假设：** 与只有“seen”相比，增加轻量“I’ll reply later”会减少延迟打开和重复催促，同时不降低关键消息的确认率。应同时测量首次打开时间、确认时间、回执关闭率、未解决任务率和主观压力；只看回复速度会遗漏回避行为。
- **能改变当前判断的证据：** 若随机实验显示，显示回执能持续降低不确定性与未解决任务，且没有增加延迟打开、关闭率或主观压力，那么“回执把摩擦前移”的判断需要收窄。

### 未解决问题与本次新增认识

- 尚无本账号的真实回复率、回执关闭率或用户访谈，不能评价增长或习惯效果。
- 本次没有实际账号实验，也未核查 Signal 或 iMessage 的默认开关状态，因此正文只描述可配置规则。
- 新增认识：已读回执的关键设计变量不是图标本身，而是信息交换契约——互惠、单方披露或不披露。评价它时要把“回复变快”和“阅读被推迟”放在同一指标组中。

## 核查来源

**原研究核查日期：2026-10-31。** 本节从原底稿中的内联来源整理，未在本次归档中重新核查。

1. [Signal Support：Read Receipts](https://support.signal.org/hc/en-us/articles/360007059812-Read-Receipts)：支持双方启用才显示的功能规则，未核查默认开关。
2. [Apple Support：Turn read receipts on or off](https://support.apple.com/guide/iphone/turn-read-receipts-on-or-off-iph5e713a045/ios)：支持用户控制自己发送的回执及按联系人设置，未核查默认开关。
3. [Hoyle et al., 2017：Was my message read?](https://www.research.ed.ac.uk/en/publications/was-my-message-read-privacy-and-signaling-on-facebook-messenger/)：402 名发送者与 316 名接收者自报调查，不支持强因果。
4. [Chou et al., 2022：Why Did You/I Read but Not Reply?](https://doi.org/10.1145/3491102.3517496)：质性研究支持情境与双方解释错位，不能估算普遍效果。
5. [Malkin et al., 2025：Do You See If I See?](https://www.usenix.org/conference/soups2025/presentation/malkin)：802 名美国参与者对互惠访问控制的态度调查，非真实行为实验。

## 发稿前检查

- 熟悉功能的读者新增认识：把 read receipt 从状态组件重构为社交访问控制与责任机制。
- 核心判断支持：两份官方规则、两项 CHI 行为研究及一项 SOUPS 反证；未声称因果。
- 比较公平：同时呈现互惠的隐私代价、规则公平与简化收益，并保留高时效协调反例。
- 可执行决定：按任务时效选择契约，并用延迟打开、关闭率和确认率共同验证。

## 归档格式检查

英文 X 加权长度：245 / 234 / 227 / 248。

中文 X 加权长度：160 / 184 / 189 / 197。

以上长度为本次归档重新计算；原文件中的人工计数记录不作为校验结果。格式检查不代表人工审定或平台发布。


[^signal]: Signal Support：Read Receipts：https://support.signal.org/hc/en-us/articles/360007059812-Read-Receipts 。支持双方启用才显示的功能规则，未核查默认开关。
[^apple]: Apple Support：Turn read receipts on or off：https://support.apple.com/guide/iphone/turn-read-receipts-on-or-off-iph5e713a045/ios 。支持用户控制自己发送的回执及按联系人设置，未核查默认开关。
[^hoyle]: Hoyle et al., 2017：Was my message read?：https://www.research.ed.ac.uk/en/publications/was-my-message-read-privacy-and-signaling-on-facebook-messenger/ 。402 名发送者与 316 名接收者自报调查，不支持强因果。
[^chou]: Chou et al., 2022：Why Did You/I Read but Not Reply?：https://doi.org/10.1145/3491102.3517496 。质性研究支持情境与双方解释错位，不能估算普遍效果。
[^malkin]: Malkin et al., 2025：Do You See If I See?：https://www.usenix.org/conference/soups2025/presentation/malkin 。802 名美国参与者对互惠访问控制的态度调查，非真实行为实验。
