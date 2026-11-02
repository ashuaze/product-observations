# P0008｜Stripe Cancel vs Refund：真正的 Undo 发生在提交之前

**日期：** 2026-10-15（Asia/Shanghai）  
**研究主题：** 反悔、退出与恢复  
**稿件状态：** 中英文均为草稿，待人工审稿

区分提交前取消与提交后补偿，设计状态、失败处理与沟通。

## 观点总结

- **核心判断：** Cancel 停止尚未完成的支付；Refund 是支付成功后新增的一条资金返还流程。相同的净结果，不代表相同的系统语义。
- **关键机制：** Stripe manual capture 先授权并占用额度，PaymentIntent 停在 `requires_capture`；商家之后可 capture 或 cancel。
- **成本与边界：** 保留可撤销状态会占用客户额度、受授权有效期限制，而且只有部分支付方式支持；部分发卡行界面也不清楚区分授权和已结算付款。
- **反例修正：** 某些退款在短时间内仍能取消，较早退款也可能表现为 reversal。因此提交后的操作不是一律不可逆，但已进入一个依赖余额、支付网络和银行处理的新流程。
- **证据限制：** Stripe 文档支持状态与流程事实；没有公开实验说明 manual capture 一定减少损失、提高信任或适合所有业务。

## 阅读入口

| 材料 | 用途 |
|---|---|
| [研究底稿](research.md) | 原审稿摘要、研究论证、反例、边界与完整来源 |
| [中文发布稿](publish-zh.md) | 本次补写的 4 条独立中文串帖 |
| [英文发布稿](publish-en.md) | 保留原有词句的 5 条英文串帖 |
| [结构化元数据](metadata.yaml) | 稳定期号、来源指纹与稿件状态 |

## 参考资料与边界

- [参考资料 1](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)
- [参考资料 2](https://docs.stripe.com/api/payment_intents/cancel)
- [参考资料 3](https://docs.stripe.com/refunds)
- [参考资料 4](https://docs.stripe.com/api/refunds/cancel)

原研究核查日期：2026-10-15。以上为原稿的历史研究结论，完整支持范围、限制和待体验项见研究底稿。2026-11-02 的回填只整理既有资料并补写中文稿，未重新核查全部来源，也未执行原稿中标为待完成的体验。
