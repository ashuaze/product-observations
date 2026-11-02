# P0012 研究底稿

原期号：P12。原研究核查日期：2026-10-19；归档与中文补写日期：2026-11-02。

原材料：[P12-recovery-contract-synthesis-2026-10-19.md](https://chatgpt.com/library?file_id=libfile_adc4fbe630d08191a77a2afa46972b3a&account_id=personal)。来源字节指纹见 metadata.yaml。原文中的“本次”“当前”等表述属于原研究日期，不代表本次归档重新验证了产品政策、价格或研究结果。

英文处理：正文词句和段落保持原样；移除写作块包装与标题中的字符统计。 中文发布稿为本次独立改写。两种语言均为待审草稿。

## 原稿编辑信息

日期：2026-10-19  
研究主题：P06–P12「产品如何给用户保留反悔、退出和恢复的机会？」周期综合。  
读者价值：把“有恢复功能”改写成可验证的任务承诺，区分恢复期限不足、备用路径失效和结果不完整。

## 中文审稿摘要

- 新判断：先检查恢复路径能否在事故中保留，再检查恢复后用户能否完成原任务；延长期限不能替代这两项检查。
- Apple 的密钥保管警告与 S3 的永久删除权限，分别揭示“备用凭据一起不可访问”和“历史一起被销毁”的风险。
- GitHub 恢复仓库不恢复团队权限；验收应看当前获准的团队能否继续工作，不应默认重新授予一切旧权限。
- Stripe 是重要反例：完整回滚并非总是目标。退款可以通过新流程修复经济结果，但发起退款不等于钱已退回。
- 这是跨案例的设计推断，不是经实验验证的通用最优方案；没有本账号或这些产品的真实恢复率数据。

## 中文研究底稿

### 问题、比较与证据边界

在用户误删、遗失设备/凭据或发起退款后，产品团队应优先延长期限，还是修补恢复路径的依赖与结果缺口？

合理选项包括：
1. 延长保留期：适合错误发现太迟；增加历史数据与存储成本，但不解决恢复凭据不可用。
2. 隔离恢复依赖和破坏权限：针对同一事故影响正常入口与备用入口；增加保管、授权和运维负担。
3. 保留受控的补偿/人工修复流程：适合无法或不宜回到完全相同旧状态；增加等待、核验和修复工作。

只比较它们面对具体失败的适配性，不把账户解锁、对象恢复和资金补偿当作同一机制排名。功能文档证明规则，不证明方案的实际效果或企业内部意图。

连续性依据：本次可读到的 P06–P11 交付文本；没有假设额外旧底稿或账号反馈。下表使用的规则均在 2026-10-19 重新打开官方原文核查；LinkedIn 等未重新打开的材料不纳入本次事实综合。

| 周期材料 | 当前核实的事实 | 本篇提炼的评审问题 |
|---|---|---|
| P06 GitHub [S1] | 符合条件的仓库可在 90 天内恢复；团队权限不恢复，fork network 等限制仍存在 | “对象恢复”后，当前获准的人能否继续任务？ |
| P07 Drive [S2] | 批量恢复仍标 Beta，覆盖最近 25 天版本，不能逐文件选择；旧版变为新当前版，已有版本保留 | 恢复范围是否匹配事故，正常新编辑能否找回？ |
| P08 Stripe [S3] | 成功的 PaymentIntent 不能取消；退款可能 pending/failed | 真正验收的是请求受理，还是资金返还？ |
| P09 X [S4] | 30 天内可重新激活；当前网页/官方 App 流程要求显式确认 | 恢复入口是否表达当下意愿，而不只是识别到登录凭据？ |
| P10 S3 [S5–S7] | Versioning 默认关闭；正常删除保留旧版，但指定版本删除与生命周期仍可移除历史 | 恢复状态是否预先存在；谁能毁掉它？ |
| P11 Apple [S8] | 官方不建议将 Recovery Key 放在 Apple Passwords、iCloud Photos、Notes 或 Drive | 账户不可访问时，备用密钥是否也一起不可访问？ |

### 本次新证据与研究限制

本次打开 USENIX Security 2024 恢复码研究全文 [S9]，不仅沿用摘要。正文记录两名 Reddit 发帖者报告因密码管理器问题而失去恢复码访问；这提供了“备用路径也可能不可访问”的真实报告，但不是受控实验或总体失败率。

研究样本具有自报和选择偏差，来自 Tuta，不是 Apple。作者包括 Tuta CEO，披露其参与研究动机、问题与设计，但未参与数据分析以及结果、讨论、结论写作。因此改称“有服务商参与的学术研究”，不笼统称“独立研究”。

摘要写 197 条支持请求，正文 Results 与 Conclusion 写 196 个 Reddit 线程，且并非所有线程都是支持请求。后续不沿用 197 这个精确数，保留原文口径差异，而不自行解释原因。

### 反例如何改变结论

- 不以恢复越完整越好为目标：旧权限可能已经不适用于当前成员；自动恢复所有权限未必安全。这是评审情境推断，不是 GitHub 公开陈述的动机。
- Stripe 退款表明：恢复用户可接受的结果可以通过补偿实现，无需把系统状态抹回原样。发起后仍需等待和处理失败；部分早期退款会表现为 reversal，不应概括为一律独立入账。
- 延长历史保留确实有助于迟发现错误，但不能补救从未保存或已永久销毁的版本。保留更多内容也可能违背用户明确擦除的目标。
- 把密钥另放一处同样有丢失、泄露与保管成本；本篇不倡议所有用户都选择个人密钥，也不把纸张、密码管理器或联系人排出统一优劣名次。
- 因此将结论收窄为：对所承诺的特定事故，测试仍可用的恢复路径与可接受的最终结果，而非保证任何事故均可恢复。

### 本轮复核修正

1. P09：不再把“一登录就必然自动恢复”作为通用事实。当前官方步骤明确有重新激活确认；本次可读的第三方应用及停用页面不足以证明所有第三方连接都会自动激活，故不沿用该结论。[S4, S10, S11]
2. P10：Object Lock 不是无条件“任何人都不能删”。Governance 模式允许拥有特殊权限并满足请求条件者绕过；Compliance 模式的权限约束更强。此差别不应省略。[S6]
3. P11：补充研究合作关系，以及摘要/正文的样本数口径差异，避免“独立研究、197 个支持请求”不加限定地继续传播。[S9]

### 可检验假设与改变判断的证据

假设：相比只提供恢复期限说明，在测试环境中按实际失败条件限制可用设备、凭据或管理权限，并按最终任务验收，更能发现恢复设计缺口。

建议比较两种评审方法在同一组模拟事故中发现的未识别失败数量、完成任务时间、未授权恢复风险及人工修复工作量；上线后再看真实结果，不以按钮点击率代替恢复率。

如果事故记录表明主要失败来自发现过晚，而路径与结果都可靠，应优先延长窗口，而非增加用户保管负担。如果隔离恢复路径增加锁定/弃用，却没有改善恢复结果，则应缩小隔离范围或改进备用方案。这是待检验假设，没有已完成演练或实验数据。

### 新增认识与适用边界

此前分别讨论“保留什么、保留多久、恢复多大范围、谁有权恢复”。本篇新增跨案例关系：**这些条件不是互相替代的福利；它们必须在同一场事故发生后仍能共同成立。最终目标是可接受的任务结果，而不是原状态的完全复制。**

适合含持久数据、协作权限、账户身份或外部资金副作用的产品评审。对本地、即时、低后果且已验证的单步 Undo，不必套用整套流程。

未解决：缺少各产品可比较的事故发生率、恢复成功率、接管率和成本，不能估计最优保留期限或优先级的普遍数值。没有本账号真实曝光、回复或重复读者数据，不能评价英文运营表现。

实际体验：本次只进行了公开资料核查与字符计算；未更改真实账户、仓库、存储权限或支付状态，无截图或亲身实验声明。

## 来源清单

均于 2026-10-19 实际打开核查。网页未标更新日的不自行推定发布日期。

- [S1 GitHub：Restoring a deleted repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/restoring-a-deleted-repository)[^source01] — 官方功能规则；90 天、权限、fork network 条件。
- [S2 Google Drive：Restore files in bulk](https://support.google.com/drive/answer/16482799?hl=en)[^source02] — 官方功能规则；仍标 Beta，不假定全部地区/账号已开放。
- [S3 Stripe：Refund and cancel payments](https://docs.stripe.com/refunds)[^source03] — 官方状态、余额、失败及 reversal 说明；支付方式/银行/地区可能影响具体处理，不作资金时效保证。
- [S4 X：How to reactivate your account](https://help.x.com/en/managing-your-account/how-to-reactivate-x-account)[^source04] — 官方网页与 iOS/Android 流程的显式确认。
- [S5 AWS：Deleting object versions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjectVersions.html)[^source05] — 官方版本删除与生命周期行为；对象锁可增加约束。
- [S6 AWS：Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)[^source06] — 官方 governance/compliance 与绕过权限边界。
- [S7 AWS：S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)[^source07] — 默认关闭、完整对象版本计费。
- [S8 Apple：Set up a recovery key](https://support.apple.com/en-us/109345)[^source08] — 英文美区支持页，标注 2026-09-14；密钥保管及账户恢复规则，不外推 ADP 在所有地区可用。
- [S9 USENIX Security 2024：Recovery Codes Study，全文](https://www.usenix.org/system/files/usenixsecurity24-holtervennhoff.pdf)[^source09] — 2024-08 会议论文，重点核查 §4.4、§5.2、§6.3–6.4 与 Financial Conflicts；历史研究而非当前产品政策。
- [S9a 会议摘要](https://www.usenix.org/conference/usenixsecurity24/presentation/h%C3%B6ltervennhoff)[^source10] — 与正文的样本数口径存在差异，未自行消解。
- [S10 X：Third-party apps and login sessions](https://help.x.com/en/managing-your-account/connect-or-revoke-access-to-third-party-apps)[^source11] — 权限与撤销授权说明，不足以支撑所有连接自动激活。
- [S11 X：Deactivate your account](https://help.x.com/en/managing-your-account/how-to-deactivate-x-account)[^source12] — 30 天停用规则；本次读取中自动重激活 FAQ 正文未呈现。

## 发稿前检查

- 新增认识：把分散案例串成“事故后仍可用的路径＋可接受的结果”，而非重复功能盘点。
- 支持/推翻：官方规则支持具体限制；是否优先修补路径或延长窗口，取决于真实事故结构。
- 公平性：不同产品只比较失败条件与验收目标，不按天数、隐私或复杂度排名。
- 可用决定：为一个具体事故指定恢复者、幸存凭据/副本、结果标准、排除项、时限与代价。
- 发布授权：仅生成供发布的文本；没有发布、回复、私信或修改账号。

下一周期 P13–P19 研究“免费与付费边界”；具体案例届时以新证据决定，避免重复 P03 的同一功能。

## 核查来源

原始来源与对应关系保留在上文。本节仅整理可点击的链接索引；原研究核查日期为 2026-10-19。

1. [S1 GitHub：Restoring a deleted repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/restoring-a-deleted-repository)
2. [S2 Google Drive：Restore files in bulk](https://support.google.com/drive/answer/16482799?hl=en)
3. [S3 Stripe：Refund and cancel payments](https://docs.stripe.com/refunds)
4. [S4 X：How to reactivate your account](https://help.x.com/en/managing-your-account/how-to-reactivate-x-account)
5. [S5 AWS：Deleting object versions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjectVersions.html)
6. [S6 AWS：Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)
7. [S7 AWS：S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)
8. [S8 Apple：Set up a recovery key](https://support.apple.com/en-us/109345)
9. [S9 USENIX Security 2024：Recovery Codes Study，全文](https://www.usenix.org/system/files/usenixsecurity24-holtervennhoff.pdf)
10. [S9a 会议摘要](https://www.usenix.org/conference/usenixsecurity24/presentation/h%C3%B6ltervennhoff)
11. [S10 X：Third-party apps and login sessions](https://help.x.com/en/managing-your-account/connect-or-revoke-access-to-third-party-apps)
12. [S11 X：Deactivate your account](https://help.x.com/en/managing-your-account/how-to-deactivate-x-account)

## 归档格式检查

本次使用官方 twitter-text 3.1.0 重新计数；不以原稿的手工计数作为最终结果。

英文加权长度：241 / 251 / 265 / 227 / 251 / 257。

中文加权长度：150 / 168 / 151 / 176 / 158。

格式检查不代表人工批准或平台发布。

[^source01]: [S1 GitHub：Restoring a deleted repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/restoring-a-deleted-repository)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source02]: [S2 Google Drive：Restore files in bulk](https://support.google.com/drive/answer/16482799?hl=en)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source03]: [S3 Stripe：Refund and cancel payments](https://docs.stripe.com/refunds)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source04]: [S4 X：How to reactivate your account](https://help.x.com/en/managing-your-account/how-to-reactivate-x-account)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source05]: [S5 AWS：Deleting object versions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjectVersions.html)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source06]: [S6 AWS：Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source07]: [S7 AWS：S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source08]: [S8 Apple：Set up a recovery key](https://support.apple.com/en-us/109345)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source09]: [S9 USENIX Security 2024：Recovery Codes Study，全文](https://www.usenix.org/system/files/usenixsecurity24-holtervennhoff.pdf)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source10]: [S9a 会议摘要](https://www.usenix.org/conference/usenixsecurity24/presentation/h%C3%B6ltervennhoff)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source11]: [S10 X：Third-party apps and login sessions](https://help.x.com/en/managing-your-account/connect-or-revoke-access-to-third-party-apps)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source12]: [S11 X：Deactivate your account](https://help.x.com/en/managing-your-account/how-to-deactivate-x-account)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
