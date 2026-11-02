# P0024｜已读回执：当状态提示变成回复义务

**日期：** 2026-10-31（Asia/Shanghai）  
**研究主题：** 习惯设计的收益与副作用；P20–P26 研究周期  
**内容类型：** 案例对照  
**稿件状态：** 中英文均为草稿，待人工审稿

帮助产品经理、设计师与独立开发者，把已读回执看成一份社交权限契约，选择互惠、单方控制或不显示，并识别“回复加快”背后的阅读回避。

## 核心判断

1. 产品只知道消息被打开，关系规范却可能把它解读为“现在能回复”或“承诺回复”。这几种状态应分开表达。
2. Signal 的双方启用与 iMessage 的接收者控制，代表不同的信息交换契约。互惠可能损失隐私，也可能被认为公平、简单。
3. 高时效协调可以使用“seen”；异步协作应考虑明确的确认或稍后回复动作，并同时测量打开时间、关闭率、任务解决与主观压力。

## 阅读入口

| 材料 | 用途 |
|---|---|
| [研究底稿](research.md) | 中文摘要、规则对照、研究依据与可检验判断 |
| [中文发布稿](publish-zh.md) | 本次补写的 4 条独立中文串帖 |
| [英文发布稿](publish-en.md) | 保留原正文的 4 条英文串帖 |
| [结构化元数据](metadata.yaml) | 编号、日期、来源指纹与状态 |

## 适用边界与参考资料

现有证据主要是调查和质性研究，不能声称已读回执必然造成焦虑或提高回复率。关系、文化与时效差异需要单独检验；本期未核查产品默认开关，也未做真实账号实验。

- [Signal 已读回执规则](https://support.signal.org/hc/en-us/articles/360007059812-Read-Receipts)
- [Apple 已读回执设置](https://support.apple.com/guide/iphone/turn-read-receipts-on-or-off-iph5e713a045/ios)
- [Hoyle 等：消息阅读与信号](https://www.research.ed.ac.uk/en/publications/was-my-message-read-privacy-and-signaling-on-facebook-messenger/)
- [Chou 等：已读未回的解释与策略](https://doi.org/10.1145/3491102.3517496)
- [Malkin 等：互惠访问控制](https://www.usenix.org/conference/soups2025/presentation/malkin)

原研究核查日期：2026-10-31。本次于 2026-11-02 回填并补写中文稿，未重新核查全部研究原文。
