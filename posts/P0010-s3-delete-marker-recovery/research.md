# P0010 研究底稿

原期号：P10。原研究核查日期：2026-10-17；归档与中文补写日期：2026-11-02。

原材料：[P10-s3-delete-marker-recovery-2026-10-17.md](https://chatgpt.com/library?file_id=libfile_4e77819da1588191b380887661648133&account_id=personal)。来源字节指纹见 metadata.yaml。原文中的“本次”“当前”等表述属于原研究日期，不代表本次归档重新验证了产品政策、价格或研究结果。

英文处理：仅补齐正文串帖序号；原英文词句和段落保持原样。 中文发布稿为本次独立改写。两种语言均为待审草稿。

## 原稿编辑信息

**研究主题：** 产品如何给用户保留反悔、退出和恢复的机会？  
**本篇类型：** 短观察  
**读者价值：** 区分软删除、版本历史与不可篡改保留，帮助产品和工程团队在事故发生前选择合适的恢复承诺。

## 中文审稿摘要

- 核心判断：恢复能力主要由事故前的存储策略决定，不能在数据已被永久删除后靠一个 Undo 补上。
- S3 开启 Versioning 后，普通删除写入 delete marker；移除 marker 可让上一版本重新成为当前版本。
- Versioning 默认关闭，而且每个版本按完整对象存储和计费；保留恢复机会会持续产生成本。
- Versioning 不等于不可篡改：显式删除版本或生命周期规则仍能永久移除历史；Object Lock 对应的是更强的保留承诺。
- 限制：官方资料只支持机制与费用规则，没有公开实验能证明该配置适合所有 SaaS 或能降低多少事故成本。

## 中文研究底稿

### 研究问题

产品应把“删除”实现为立即擦除，还是写入一个可撤销的新状态？合理选项互相冲突：立即删除成本低且满足清除意图；版本化删除支持恢复但增加存储、权限和保留管理；不可篡改保留能抵抗更强风险，却降低运营灵活性。

### 方案比较

| 方案 | 删除后的状态 | 能解决的问题 | 主要代价与失败条件 |
| --- | --- | --- | --- |
| 未开启 Versioning | 按对象 key 删除会永久移除对象 | 简单清理、明确清除 | 误删后没有内建历史可恢复 |
| Versioning + delete marker | 对象表现为已删除，旧版本仍存在 | 误删、误覆盖、应用错误 | 默认关闭；完整版本计费；有权限者与生命周期规则仍可永久删除 |
| Versioning + Object Lock | 指定版本在保留期或 legal hold 下不能被删除或覆盖 | 合规、恶意或高权限误删风险 | 约束更强；只保护指定版本；仍可新增版本和 delete marker |

### 已核查事实与来源

- **事实：** S3 Versioning 默认关闭，需显式启用。开启后，普通删除不会永久移除对象，而是插入 delete marker；每个对象版本都是完整对象而非差异，分别计费。  
  [AWS：Retaining multiple versions of objects with S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)[^source01]

- **事实：** 未启用版本控制的 bucket 中，按 key 删除对象会永久删除；在已启用版本控制的 bucket 中，不指定 version ID 的删除会写入 marker。删除该 marker 后，对象会重新出现。  
  [AWS：Deleting Amazon S3 objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjects.html)[^source02]  
  [AWS：Managing delete markers](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ManagingDelMarkers.html)[^source03]

- **事实：** 指定 version ID 可永久删除版本，不能撤销；NoncurrentVersionExpiration 也可永久移除非当前版本。  
  [AWS：Deleting object versions from a versioning-enabled bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjectVersions.html)[^source04]

- **事实：** Object Lock 依赖 Versioning，可通过 retention period 或 legal hold 保护指定版本；它不阻止创建新版本或在其上增加 delete marker。  
  [AWS：Locking objects with Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)[^source05]

以上均于 **2026-10-17** 实际打开核查。

### 解释、反证与边界

- **推断：** delete marker 把“用户暂时看不到对象”和“底层字节已被擦除”分成两个状态。对产品设计而言，删除文案必须说明自己承诺的是隐藏、可恢复移除还是永久擦除。
- **反证：** 保留所有历史并不总是更好。它会增加费用，也可能违背隐私删除、最小化保留或数据生命周期要求；这时需要受控的永久删除，而不是无限期软删除。
- **威胁模型：** Versioning主要应对普通误操作和覆盖。若具有永久删除权限的账号被滥用，仅有版本历史不足；权限隔离、Object Lock 或独立副本对应更强的风险。
- **适用边界：** 本篇讨论当前 S3 通用 bucket 机制，不把基础设施结论直接等同于面向消费者的回收站体验。
- **实际体验：** 本次未创建真实 bucket 或执行删除；所有功能事实来自官方文档，不写作亲身测试。

### 可检验假设

对保存用户上传内容的 SaaS，启用 Versioning 并给非当前版本设置有限保留期，可能降低误删和覆盖事故的恢复时间，但会增加存储成本。应同时观察：

- 可恢复事故数量与平均恢复耗时；
- 非当前版本占用与月度成本；
- 因生命周期规则过早到期而无法恢复的比例；
- 拥有永久删除权限的主体数量；
- 隐私删除请求是否在约定期限内真正清除所有版本。

如果恢复事件极少、版本成本显著，或删除承诺要求即时擦除，就应缩短保留期或缩小版本化范围。

### 本次新增认识

P07 说明恢复单位要匹配事故范围，P08 说明提交前撤销与提交后补偿不同，P09 增加了再激活入口风险。P10 再增加一个前置条件：

> **恢复不是事后按钮，而是事故发生前已经付费保存的状态。**

同时，可恢复历史与不可篡改历史是两种不同承诺，必须根据权限与攻击者能力分别设计。

## 发稿前检查

- **熟悉产品的读者新增什么？** delete marker 不是“另一个回收站”而已，它显示恢复能力由预先保留的状态、权限和生命周期共同决定。
- **核心判断如何被推翻？** 若业务数据表明事后仍能从其他权威系统无损重建对象，S3 内部版本历史的重要性会下降。
- **比较是否公平？** 已按事故恢复、永久删除和对抗性保留三个不同任务比较，没有把 Object Lock 当作 Versioning 的直接升级按钮。
- **读者可做什么决定？** 在实现删除前明确：是否保存历史、保留多久、谁能永久删除、成本由谁承担，以及删除承诺何时真正完成。

## 核查来源

原始来源与对应关系保留在上文。本节仅整理可点击的链接索引；原研究核查日期为 2026-10-17。

1. [AWS：Retaining multiple versions of objects with S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)
2. [AWS：Deleting Amazon S3 objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjects.html)
3. [AWS：Managing delete markers](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ManagingDelMarkers.html)
4. [AWS：Deleting object versions from a versioning-enabled bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjectVersions.html)
5. [AWS：Locking objects with Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)

## 归档格式检查

本次使用官方 twitter-text 3.1.0 重新计数；不以原稿的手工计数作为最终结果。

英文加权长度：257 / 258 / 247 / 248 / 262。

中文加权长度：139 / 202 / 166 / 152。

格式检查不代表人工批准或平台发布。

[^source01]: [AWS：Retaining multiple versions of objects with S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source02]: [AWS：Deleting Amazon S3 objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjects.html)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source03]: [AWS：Managing delete markers](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ManagingDelMarkers.html)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source04]: [AWS：Deleting object versions from a versioning-enabled bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjectVersions.html)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
[^source05]: [AWS：Locking objects with Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)。来源沿用原稿，支持范围及证据限制见原研究论证；本次未重新核查。
