# P0010｜S3 Delete Marker：恢复能力必须先于错误存在

**日期：** 2026-10-17（Asia/Shanghai）  
**研究主题：** 反悔、退出与恢复  
**稿件状态：** 中英文均为草稿，待人工审稿

区分软删除、历史与不可篡改保留，明确事故前的恢复承诺。

## 观点总结

- 核心判断：恢复能力主要由事故前的存储策略决定，不能在数据已被永久删除后靠一个 Undo 补上。
- S3 开启 Versioning 后，普通删除写入 delete marker；移除 marker 可让上一版本重新成为当前版本。
- Versioning 默认关闭，而且每个版本按完整对象存储和计费；保留恢复机会会持续产生成本。
- Versioning 不等于不可篡改：显式删除版本或生命周期规则仍能永久移除历史；Object Lock 对应的是更强的保留承诺。
- 限制：官方资料只支持机制与费用规则，没有公开实验能证明该配置适合所有 SaaS 或能降低多少事故成本。

## 阅读入口

| 材料 | 用途 |
|---|---|
| [研究底稿](research.md) | 原审稿摘要、研究论证、反例、边界与完整来源 |
| [中文发布稿](publish-zh.md) | 本次补写的 4 条独立中文串帖 |
| [英文发布稿](publish-en.md) | 保留原有词句的 5 条英文串帖 |
| [结构化元数据](metadata.yaml) | 稳定期号、来源指纹与稿件状态 |

## 参考资料与边界

- [参考资料 1](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)
- [参考资料 2](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjects.html)
- [参考资料 3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ManagingDelMarkers.html)
- [参考资料 4](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjectVersions.html)
- [参考资料 5](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)

原研究核查日期：2026-10-17。以上为原稿的历史研究结论，完整支持范围、限制和待体验项见研究底稿。2026-11-02 的回填只整理既有资料并补写中文稿，未重新核查全部来源，也未执行原稿中标为待完成的体验。
