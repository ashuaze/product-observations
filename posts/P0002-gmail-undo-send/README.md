# P0002｜Gmail Undo Send：纠错机会应该放在哪里？

**日期：** 2026-10-09（Asia/Shanghai）  
**研究主题：** 纠错与可逆选择  
**稿件状态：** 中英文均为草稿，待人工审稿

按错误发现时机、等待成本和权限，选择合适的纠错机会。

## 观点总结

- 核心问题是把纠错机会放在哪个阶段。发送前确认、延迟发送、送达后撤回依赖不同条件，不能用同一个“可撤销”标签概括。
- Gmail 当前网页版的取消窗口可选 5、10、20、30 秒；不应描述成可以收回收件人已收到或读过的 Gmail 邮件。
- 对比是机制分析，不是跨平台效果实验。Gmail Android 可开启发送确认；它与网页版取消发送的比较，不能证明任何一种更能降低错误。
- 反例缩小了结论：Exchange Online 支持符合条件的送达后撤回。现行规则还支持收件组织明确允许的跨租户撤回，不能沿用“所有跨组织邮件都不能撤回”的笼统说法。
- 未找到或引用能确定最佳延迟、错误率下降幅度或留存收益的实验数据。“纠错窗口应按错误发现时间和等待代价选择”属于待验证的产品判断。

## 阅读入口

| 材料 | 用途 |
|---|---|
| [研究底稿](research.md) | 原审稿摘要、研究论证、反例、边界与完整来源 |
| [中文发布稿](publish-zh.md) | 本次补写的 4 条独立中文串帖 |
| [英文发布稿](publish-en.md) | 保留原有词句的 6 条英文串帖 |
| [结构化元数据](metadata.yaml) | 稳定期号、来源指纹与稿件状态 |

## 参考资料与边界

- [参考资料 1](https://support.google.com/mail/answer/2819488?hl=en)
- [参考资料 2](https://support.google.com/mail/answer/6562?co=GENIE.Platform%3DAndroid&hl=en)
- [参考资料 3](https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/work-with-cloud-based-message-recall)
- [参考资料 4](https://blog.google/products-and-platforms/products/gmail/how-to-unsend-email-gmail/)

原研究核查日期：2026-10-09。以上为原稿的历史研究结论，完整支持范围、限制和待体验项见研究底稿。2026-11-02 的回填只整理既有资料并补写中文稿，未重新核查全部来源，也未执行原稿中标为待完成的体验。
