# P0005 研究底稿

原期号：P05。原研究核查日期：2026-10-12；归档与中文补写日期：2026-11-02。

原材料：[P05-Signal-usernames-research-2026-10-12.md](https://chatgpt.com/library?file_id=libfile_16777d2bcd9881919ca25ef4b982406d&account_id=personal)。来源字节指纹见 metadata.yaml。原文中的“本次”“当前”等表述属于原研究日期，不代表本次归档重新验证了产品政策、价格或研究结果。

英文处理：正文词句和段落保持原样；移除写作块包装与标题中的字符统计。 中文发布稿为本次独立改写。两种语言均为待审草稿。

## 原稿编辑信息

核查日期：2026-10-12（北京时间）
账号：@azeashu / Ashu | Product Notes
研究主题：把账号注册、被发现、对外展示与身份验证拆成不同机制。
读者价值：帮助产品经理、设计师与独立开发者判断何时应减少单一标识符承担的职责，以及分层后新增了哪些隐私收益、发现摩擦与恢复风险。
状态：可供复制发布；未自动发布。本次仅核查公开资料，没有注册或操作 Signal 账号。

## 中文审稿摘要

- Signal username 的主要作用是建立首次联系，不是登录名、聊天中的公开 handle 或身份凭证；接受消息请求后，界面转而显示 profile name。
- 默认设置体现了两种不同隐私：手机号默认不向尚未保存它的人显示，但“可通过手机号找到我”默认仍为 Everybody。想只通过 username 建立新联系，需要另行关闭手机号发现，因此隐私增强会带来可达性下降。
- username 可更换或删除，QR code/URL 还能独立重置；这些操作阻止旧地址开启新联系，但不会切断已经建立的聊天。它更像可撤销的“介绍地址”，不是撤回既有关系。
- 2024 博文及当前常规帮助仍把手机号描述为标准注册条件；但截至 2026-10-12，Signal 官方已在 Android beta 8.28+ 测试付费的无手机号 Signal Login。正文明确写成 beta 例外，不能再声称所有版本都必须以手机号注册。
- 资料仅证明功能与官方解释，没有用户研究或实验支持“用户名降低骚扰”“提高采用率”或“beta 方案更安全”等效果判断。

## 中文研究底稿

### 1. 研究问题与使用情境

用户情境：一个人希望让同事、活动参与者或临时合作对象在 Signal 上联系自己，但不愿把手机号作为长期、可复用的联系标识公开出去。

冲突选择：

1. **用手机号注册并允许手机号发现**：熟人更容易知道彼此在使用 Signal；手机号同时承担注册和发现工作。
2. **用手机号注册，但只分享 username／QR code／URL**：降低首次联系时暴露手机号的必要性，但新联系人必须获得准确地址。
3. **让 username 成为公开、永久的身份 handle**：发现简单、跨场景一致，但更容易把不同情境中的活动关联起来，也增加抢注、仿冒与长期暴露。
4. **Android beta 的无手机号 Signal Login**：进一步拆开账号与手机号，但把恢复责任转移到密钥保存，并引入一次性付费及 beta 可用性边界。
5. **把身份验证也交给 username**：界面更简单，却会让“知道地址”被误解成“对方确实是那个人”。

核心问题不是“手机号和用户名谁更好”，而是同一个标识符是否应该同时承担账号所有权、发现、展示和验证。

### 2. 当前事实与证据对应

| 编号 | 已确认事实 | 来源与适用边界 |
|---|---|---|
| S1 | username 是可选的，用于在不分享手机号的情况下发起联系；它不是 profile name。需要准确 username，Signal 没有可搜索的 username 目录。 | Signal Support《Phone Number Privacy and Usernames》。当前常规帮助；2026-10-12 打开正文核查。 |
| S2 | 发起方使用 username 发送 message request；接受后显示 profile name，而非继续把 username 当作聊天身份。现有手机号对话与 username 请求可能合并，使对方知道二者属于同一人。 | 同 S1。该机制说明 username 不能保证不同联系路径永不关联。 |
| S3 | 手机号默认不向没有预先保存号码的人显示；但“Who can find me by my number”默认是 Everybody。设为 Nobody 后，新联系人需要 exact username；发现会更困难。 | Signal Support《Phone Number Privacy and Usernames: Deeper Dive》，适用于 Signal 7.0+ 的当前帮助说明。 |
| S4 | username 可更改或删除，既有聊天不受影响；只能同时拥有一个 username。QR code 和 URL 可以在不改 username 的情况下重置。 | S1、S3 及 2024 Signal 官方博文。更改地址阻止旧地址发起新聊天，不等于撤销既有联系人。 |
| S5 | username 不是永久 handle，也不是身份验证。Signal 建议比较 safety numbers，最好通过线下或第二渠道核对。 | S3；支持页明确将 verification tools 与 username discovery 分开。 |
| S6 | 2024 官方博文和当前常规帮助把手机号描述为标准注册条件。 | Signal 2024 博文与 S1/S3。它们描述常规 username 流程，不能覆盖下面的 Android beta 例外。 |
| S7 | Android beta 8.28+ 提供可选的无手机号注册：一次性付费后生成 32 字符 Account ID 和 64 字符 Recovery Key；丢失两者时没有手机号 fallback。username 仍可选；不创建 username 时，其他用户无法找到或联系该账号。 | Signal Support《Phone Numberless Registration for Android beta》。2026-10-12 打开；标题和正文均明确为 Android beta，不外推到稳定版、iOS 或全部用户。 |
| S8 | phone-numberless Signal Login 可使用 TOTP 和／或 passkeys 作为额外保护，Signal 不保管可恢复这些第二因素的 recovery codes。 | Signal Support《Two factor authentication and TOTP》。这是 beta 新账号体系的安全与恢复说明，不用于比较实际攻击率。 |

### 3. 分层比较

| 层 | Signal 当前采用的标识 | 主要任务 | 收益 | 代价与失败条件 |
|---|---|---|---|---|
| 账号创建／所有权 | 常规流程使用手机号；Android beta 可用 Account ID + Recovery Key | 建立和恢复账号 | 标准流程便于联系人发现与反垃圾；beta 可完全避开手机号 | 手机号暴露和号码生命周期问题；beta 密钥丢失没有手机号 fallback |
| 发现／首次联系 | 手机号搜索，或 exact username／QR code／URL | 让新联系人定位账号 | username 可按情境分享，减少提供手机号 | 无目录、需准确转交；关闭手机号发现后熟人更难找到你 |
| 聊天中的展示 | profile name、头像 | 在对话中表达“我是谁” | 不把临时 username 固化成公共身份 | profile name 不必唯一，不能单独证明身份 |
| 身份验证 | safety number、第二渠道核对、共同群组等线索 | 判断对方是不是声称的那个人 | 把地址知识与身份真实性分开 | 增加核对成本；很多用户可能跳过，官方没有公开使用率 |
| 撤销新入口 | 更改／删除 username，重置 QR code 或 URL | 阻止旧地址继续带来新请求 | 可在活动、交易等情境结束后收回入口 | 不会切断已经存在的聊天；旧关系仍可继续发消息 |

### 4. 分析、竞争解释与反例

**本账号的分析：**
Signal 把 username 设计成建立联系时使用的短期地址，而不是整个产品中的统一身份。这样可以让一个人按情境分享入口，同时保留不同的展示名和验证机制。它降低的是“为了开始聊天而披露手机号”的必要性，不等于匿名，也不保证两个已有联系路径永不合并。

**竞争解释：**
username 的设计也可能首先是为了降低抢注、仿冒、垃圾信息和全站搜索带来的风险，而不只是为了“可撤销”。2024 官方博文称末尾数字规则旨在保持用户名平等并减少 spoofing；公开资料没有给出各目标的权重或实验结果，因此正文只讨论机制后果，不声称唯一设计动机。

**改变结论的反例与边界：**

- **手机号仍可能参与发现。** 用户仅创建 username，并不会自动关闭“Who can find me by my number”。隐私效果取决于另一项设置。
- **既有关系不会被 username 撤销。** 更改或删除 username 后，已建立的聊天仍在；所以它只能撤回新入口。
- **历史路径可能合并。** 已经通过手机号聊过的人再通过 username 建立联系时，对话会合并，对方会知道两种地址指向同一人。
- **地址不等于身份证明。** 精确知道 username 只说明消息被路由到对应账号；Signal 仍建议使用 safety numbers 或第二渠道。
- **当前注册规则已有 beta 例外。** “Signal 仍需手机号注册”只适用于常规 username 流程，不能作为 2026-10-12 的无条件陈述。
- **更少被发现未必总是更好。** 对亲友网络或需要快速可达的服务场景，关闭手机号发现可能显著增加协调成本。

### 5. 暂定判断与可检验假设

设计标识体系时，应分别回答：

1. 什么证明用户拥有账号？
2. 别人通过什么入口找到这个账号？
3. 建立关系后，对方看到什么身份？
4. 如何核验对方确实是其所声称的人？
5. 改变或撤销某个入口，会不会影响既有关系与账号恢复？

只有在用户确实重视简便发现、且披露与跨情境关联的代价足够低时，才适合让一个稳定标识同时承担多个任务。

**可检验假设：**

- 若把 username 定位为临时的介绍地址，用户应更愿意在短期或半公开场景分享它；需用真实分享率、消息请求质量和骚扰报告验证。
- 若手机号可见性与手机号可发现性分别设置，用户可能误以为隐藏手机号也关闭了手机号搜索；需用设置理解测试验证。
- 若精确 username 加无目录显著降低无关请求，但同时明显降低成功建立联系的比例，就需要按场景权衡，而不是把“更少请求”直接视为成功。
- beta 无手机号注册是否优于手机号注册，必须同时观察注册完成率、账号恢复成功、密钥丢失、垃圾账号成本与跨平台可用性；目前官方功能文档没有这些结果。

能改变当前判断的证据：若用户研究显示绝大多数人能正确区分注册、发现、显示和验证，设置误解不是主要风险，则“分层增加认知成本”的担忧应减弱；若更换 username 后既有联系人骚扰仍是主要问题，则产品还需要单独的 blocking 或关系撤销机制，不能把 username 轮换当成充分解法。

### 6. 未解决问题

- Android beta 的无手机号注册何时、是否进入稳定版和其他平台？
- $2.99 一次性付费对注册完成率、垃圾账号创建和地区可及性的实际影响是什么？
- 用户是否理解“隐藏手机号”与“禁止通过手机号发现”是两个不同设置？
- username、QR code 与 URL 分别在什么场景中被使用，重置入口是否容易被发现？
- 有多少用户把 exact username 当作身份真实性证明，从而跳过 safety number 核验？
- 关闭手机号发现后，成功建立新联系与误联系／骚扰的净变化如何？

### 7. 本次新增认识与研究衔接

已读取 P04《iPhone Offload App 与 Delete App》的完整底稿。P04 说明“保留数据”与“保留可用恢复路径”不同；P05 将这一思路扩展到身份系统：保留或替换一个联系地址，与保留账号、已有关系和身份真实性是四件不同的事。

本期最重要的新证据是 Android beta 的无手机号 Signal Login。它迫使结论从“username 只改变发现，注册始终依赖手机号”收窄为：“在当前标准 username 流程中，手机号仍承担注册；Signal 已开始用独立 beta 测试另一套账号所有权与恢复机制。”

## 实际打开核查的来源

核查日期均为 2026-10-12。

- S1/S2/S4 — Signal Support, Phone Number Privacy and Usernames  
  [来源 1](https://support.signal.org/hc/en-us/articles/6712070553754-Phone-Number-Privacy-and-Usernames)[^source01]
- S3/S4/S5/S6 — Signal Support, Phone Number Privacy and Usernames: Deeper Dive  
  [来源 2](https://support.signal.org/hc/en-us/articles/6829998083994-Phone-Number-Privacy-and-Usernames-Deeper-Dive)[^source02]
- S4/S6 — Signal Blog, Keep your phone number private with Signal usernames（2024-02-20；历史发布背景）  
  [来源 3](https://signal.org/blog/phone-number-privacy-usernames/)[^source03]
- S7 — Signal Support, Phone Numberless Registration for Android beta（本次访问时要求 beta 8.28+）  
  [来源 4](https://support.signal.org/hc/en-us/articles/11197884108826-Phone-Numberless-Registration-for-Android-beta)[^source04]
- S8 — Signal Support, Two factor authentication and TOTP  
  [来源 5](https://support.signal.org/hc/en-us/articles/11228705649690-Two-factor-authentication-and-TOTP-Time-based-One-Time-Password)[^source05]

证据性质：全部为 Signal 官方功能、帮助或历史团队文章；没有独立用户研究、公开实验数据或本次实际产品操作。因此发布稿只提出有条件的产品判断，不宣称因果效果。

## 核查来源

原始来源与对应关系保留在上文。本节仅整理可点击的链接索引；原研究核查日期为 2026-10-12。

1. [来源 1](https://support.signal.org/hc/en-us/articles/6712070553754-Phone-Number-Privacy-and-Usernames)
2. [来源 2](https://support.signal.org/hc/en-us/articles/6829998083994-Phone-Number-Privacy-and-Usernames-Deeper-Dive)
3. [来源 3](https://signal.org/blog/phone-number-privacy-usernames/)
4. [来源 4](https://support.signal.org/hc/en-us/articles/11197884108826-Phone-Numberless-Registration-for-Android-beta)
5. [来源 5](https://support.signal.org/hc/en-us/articles/11228705649690-Two-factor-authentication-and-TOTP-Time-based-One-Time-Password)

## 发稿前检查

本节为归档阶段整理。稿件结构、正文长度和引用交由检查工具核对；事实、推断与反例仍以原研究为据。人工审稿待完成，未记录平台发布。


## 归档格式检查

本次使用官方 twitter-text 3.1.0 重新计数；不以原稿的手工计数作为最终结果。

英文加权长度：262 / 268 / 265 / 267 / 255 / 255。

中文加权长度：160 / 211 / 177 / 182。

格式检查不代表人工批准或平台发布。

[^source01]: [来源 1](https://support.signal.org/hc/en-us/articles/6712070553754-Phone-Number-Privacy-and-Usernames)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source02]: [来源 2](https://support.signal.org/hc/en-us/articles/6829998083994-Phone-Number-Privacy-and-Usernames-Deeper-Dive)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source03]: [来源 3](https://signal.org/blog/phone-number-privacy-usernames/)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source04]: [来源 4](https://support.signal.org/hc/en-us/articles/11197884108826-Phone-Numberless-Registration-for-Android-beta)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source05]: [来源 5](https://support.signal.org/hc/en-us/articles/11228705649690-Two-factor-authentication-and-TOTP-Time-based-One-Time-Password)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
