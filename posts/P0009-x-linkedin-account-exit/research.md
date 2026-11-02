# P0009 研究底稿

原期号：P09。原研究核查日期：2026-10-16；归档与中文补写日期：2026-11-02。

原材料：[P09-x-linkedin-account-exit-2026-10-16.md](https://chatgpt.com/library?file_id=libfile_61fb5763f3a081919deafd8099f65680&account_id=personal)。来源字节指纹见 metadata.yaml。原文中的“本次”“当前”等表述属于原研究日期，不代表本次归档重新验证了产品政策、价格或研究结果。

英文处理：仅补齐正文串帖序号；原英文词句和段落保持原样。 中文发布稿为本次独立改写。两种语言均为待审草稿。

## 原稿编辑信息

**研究主题：** 产品如何给用户保留反悔、退出和恢复的机会？  
**本篇类型：** 案例对照  
**读者价值：** 把“软删除”拆成公开可见性、保留期限、再激活入口、恢复范围与外部残留五个可设计变量，避免只比较撤销窗口长短。

## 中文审稿摘要

- 核心判断：可逆退出不是一个倒计时，而是一份“退出契约”；必须同时说明隐藏、保留、再激活、恢复范围和外部残留。
- X 把停用作为永久删除前的 30 天状态；登录可触发恢复。第三方应用入口使“容易回来”同时成为意外撤销退出的风险。
- LinkedIn 把临时休眠与关闭分开，但关闭后即使在 14 天内重新开启，部分关系数据仍无法恢复。
- “更长撤销期更好”没有证据支持；窗口长度只是一个变量，入口控制与恢复完整性同样重要。
- 限制：本篇依据官方规则比较产品状态，不声称这些规则降低了后悔、客服量或流失；未发现两家公司公开的因果实验。

## 中文研究底稿

### 研究问题

当用户说“我想消失”时，产品应当提供立即删除、带宽限期的删除，还是独立的临时隐藏？冲突在于：事故恢复需要保留，明确退出需要确定性，网络型产品还必须处理关系数据与外部副本。

### 关键事实与对应来源

| 对象 | 已核事实 | 证据范围 |
| --- | --- | --- |
| X 停用 | 停用是永久删除的第一步，持续 30 天；期间未访问则账户删除。30 天内登录并确认可重新激活，帖子、关注者、点赞等可能需要时间恢复。 | X 官方帮助，仅支持当前功能规则。 |
| X 再激活入口 | X 官方提示登录会重新激活，并要求停用前撤销第三方应用访问；第三方应用可按权限使用账户。 | X 官方帮助，支持入口与权限事实；不证明意外再激活的发生率。 |
| LinkedIn 休眠 | 休眠后资料对所有人不可见；帖子、评论、消息及给他人的推荐/认可仍保留，但以“A LinkedIn member”显示。24 小时后可登录恢复。 | LinkedIn 官方帮助，仅支持当前功能规则。 |
| LinkedIn 关闭 | 多数情况下，关闭少于 14 天可重新开启；认可、推荐、忽略或待处理邀请、关注项、群组成员资格无法恢复。搜索引擎可能暂时保留资料。 | LinkedIn 官方帮助，支持恢复范围与外部缓存边界。 |

### 解释、比较与反证

- **推断：** X 用一个中间状态同时承载“短暂离开”和“走向删除”，流程短，但意图较混合；LinkedIn 另设休眠，语义更清楚，但增加了一个需要理解的选择。
- **推断：** 再激活并非只有期限，还包括入口。只要登录或集成仍可触发恢复，产品就应把触发器、确认步骤和撤销方式纳入退出设计。
- **反例：** 立即删除能给有安全或隐私动机的用户更强确定性；30 天宽限期并非天然更“用户友好”。反过来，完全无宽限期也会放大误操作成本。
- **公平性边界：** X 停用会进入删除倒计时，LinkedIn 休眠本身不是删除；两者不是一对一同功能。因此本篇比较的是“退出状态如何拆分”，不是评判哪家窗口更优。

### 适用边界

适用于社交、协作、创作者与市场型产品，尤其是恢复对象包含关系、声誉或成员资格时。若法律、合规、安全事件或用户明确要求需要即时不可逆删除，宽限期与可再激活入口应服从这些更高优先级约束。

### 未解决问题与可检验假设

- 未找到公开实验说明 14 天或 30 天哪个窗口能更好平衡误删与退出确定性。
- 可检验假设：在退出确认页列出“所有可再激活入口”和“不会恢复的对象”，并要求任何入口再次显式确认，会减少意外恢复与相关支持请求。
- 可推翻条件：若日志显示第三方入口没有造成非意图恢复，或恢复清单不改善用户对结果的预测，上述判断应减弱。

### 本次新增认识

在此前“恢复对象要匹配故障对象”和“提交前撤销、提交后补偿”的基础上，本篇新增两点：**恢复也有入口风险**；**可逆退出需要对象清单，而不只是截止时间**。

## 来源清单

均于 **2026-10-16** 实际打开核查：

1. [X Help — How to deactivate your account](https://help.x.com/en/managing-your-account/how-to-deactivate-x-account)[^source01] — 30 天停用期、删除、订阅与私信边界。
2. [X Help — How to reactivate your account](https://help.x.com/en/managing-your-account/how-to-reactivate-x-account)[^source02] — 30 天内恢复、登录确认、恢复延迟。
3. [X Help — About third-party apps and log in sessions](https://help.x.com/en/managing-your-account/connect-or-revoke-access-to-third-party-apps)[^source03] — 第三方应用权限与撤销入口。
4. [LinkedIn Help — Hibernate your LinkedIn account](https://www.linkedin.com/help/linkedin/answer/a1336653)[^source04] — 休眠后的可见性、保留对象与 24 小时限制。
5. [LinkedIn Help — Close and delete your LinkedIn account](https://www.linkedin.com/help/linkedin/answer/a1379064)[^source05] — 14 天重新开启、不可恢复项目、搜索引擎缓存边界。

## 发稿前检查

- **熟悉功能的读者新增什么？** 从比较宽限期，转向检查“退出状态 × 再激活入口 × 恢复对象”的完整契约。
- **哪些证据支持或推翻判断？** 官方规则支持状态与边界；真实误恢复率、重新开启成功率和用户预测准确率可验证推断。
- **比较是否公平？** 已明确休眠与停用并非同一动作，只比较状态拆分，不做总体优劣排名。
- **读者可据此做什么？** 在设计删除／停用流程时，用五项清单评审：立即隐藏什么、保留什么多久、谁能再激活、能恢复什么、系统外还留下什么。

## 核查来源

原始来源与对应关系保留在上文。本节仅整理可点击的链接索引；原研究核查日期为 2026-10-16。

1. [X Help — How to deactivate your account](https://help.x.com/en/managing-your-account/how-to-deactivate-x-account)
2. [X Help — How to reactivate your account](https://help.x.com/en/managing-your-account/how-to-reactivate-x-account)
3. [X Help — About third-party apps and log in sessions](https://help.x.com/en/managing-your-account/connect-or-revoke-access-to-third-party-apps)
4. [LinkedIn Help — Hibernate your LinkedIn account](https://www.linkedin.com/help/linkedin/answer/a1336653)
5. [LinkedIn Help — Close and delete your LinkedIn account](https://www.linkedin.com/help/linkedin/answer/a1379064)

## 归档格式检查

本次使用官方 twitter-text 3.1.0 重新计数；不以原稿的手工计数作为最终结果。

英文加权长度：212 / 267 / 263 / 279 / 257。

中文加权长度：168 / 168 / 143 / 170。

格式检查不代表人工批准或平台发布。

[^source01]: [X Help — How to deactivate your account](https://help.x.com/en/managing-your-account/how-to-deactivate-x-account)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source02]: [X Help — How to reactivate your account](https://help.x.com/en/managing-your-account/how-to-reactivate-x-account)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source03]: [X Help — About third-party apps and log in sessions](https://help.x.com/en/managing-your-account/connect-or-revoke-access-to-third-party-apps)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source04]: [LinkedIn Help — Hibernate your LinkedIn account](https://www.linkedin.com/help/linkedin/answer/a1336653)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source05]: [LinkedIn Help — Close and delete your LinkedIn account](https://www.linkedin.com/help/linkedin/answer/a1379064)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
