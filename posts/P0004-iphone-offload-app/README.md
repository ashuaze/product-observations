# P0004｜iPhone Offload App 与 Delete App：保留数据，怎样才算保留退路？

**日期：** 2026-10-11（Asia/Shanghai）  
**研究主题：** 退出与恢复  
**稿件状态：** 中英文均为草稿，待人工审稿

把保留数据与恢复任务分开，评价临时退出是否真正可逆。

## 观点总结

- Offload 将 App 本体与用户文稿、数据分开：释放前者占用，同时保留后者。Delete 移除 App 及其相关本地数据；不能扩大为删除所有云端数据。
- 选择取决于空间构成及恢复条件。文稿与数据占大头时，Offload 对这部分占用无能为力；重新下载不适合当下无法联网、又需要立即使用的情境。
- Apple 明确说明，保存在 iCloud 的 App 数据不会随 App 删除。删除后仍可能有云端恢复路径，因此不能把 Offload/ Delete 简单写成“可逆/绝对不可逆”。
- 删除本地 App、删除账号、结束订阅是不同范围的操作。降低回来的成本，也应让真正退出的路径清楚。
- 本篇只有功能与规则证据，没有 Apple 的相关实验或用户行为数据。不会宣称 Offload 提高留存、减少误删或提升订阅收入。

## 阅读入口

| 材料 | 用途 |
|---|---|
| [研究底稿](research.md) | 原审稿摘要、研究论证、反例、边界与完整来源 |
| [中文发布稿](publish-zh.md) | 本次补写的 4 条独立中文串帖 |
| [英文发布稿](publish-en.md) | 保留原有词句的 6 条英文串帖 |
| [结构化元数据](metadata.yaml) | 稳定期号、来源指纹与稿件状态 |

## 参考资料与边界

- [参考资料 1](https://support.apple.com/en-us/108429)
- [参考资料 2](https://support.apple.com/en-ie/guide/iphone/iph47c931112/ios)
- [参考资料 3](https://support.apple.com/en-au/guide/iphone/iph248b543ca/27/ios/27)
- [参考资料 4](https://support.apple.com/en-us/101550)
- [参考资料 5](https://developer.apple.com/help/app-review/guideline-reference/5-1-1-account-deletion/)

原研究核查日期：2026-10-11。以上为原稿的历史研究结论，完整支持范围、限制和待体验项见研究底稿。2026-11-02 的回填只整理既有资料并补写中文稿，未重新核查全部来源，也未执行原稿中标为待完成的体验。
