# P0011｜Apple 账户恢复：恢复权应该交给谁？

**日期：** 2026-10-18（Asia/Shanghai）  
**研究主题：** 反悔、退出与恢复  
**稿件状态：** 中英文均为草稿，待人工审稿

比较平台、联系人与个人密钥的恢复权和失败条件。

## 观点总结

- 核心判断：更强的隐私保护会改变“谁有能力恢复账户”；恢复机制必须明确权力归属和永久失败条件。
- 标准 iCloud 保护让 Apple 保存部分数据类别的密钥并协助恢复；Advanced Data Protection 将大多数密钥留在可信设备，并要求用户先配置替代恢复方法。
- Recovery Contact 只能提供六位恢复码，不能访问账户或数据；它把协助能力与直接访问权分开。
- Recovery Key 将控制权交给用户，同时关闭 Apple 标准账户恢复；密钥丢失可能造成永久锁定。
- 独立研究支持“个人恢复码存在实际可用性问题”，但研究对象不是 Apple，不能据此判断 Apple 三种方案的真实成功率。

## 阅读入口

| 材料 | 用途 |
|---|---|
| [研究底稿](research.md) | 原审稿摘要、研究论证、反例、边界与完整来源 |
| [中文发布稿](publish-zh.md) | 本次补写的 4 条独立中文串帖 |
| [英文发布稿](publish-en.md) | 保留原有词句的 6 条英文串帖 |
| [结构化元数据](metadata.yaml) | 稳定期号、来源指纹与稿件状态 |

## 参考资料与边界

- [参考资料 1](https://support.apple.com/en-us/102651)
- [参考资料 2](https://support.apple.com/en-us/108756)
- [参考资料 3](https://support.apple.com/en-us/102641)
- [参考资料 4](https://support.apple.com/en-us/109345)
- [参考资料 5](https://support.apple.com/en-us/118574)
- [参考资料 6](https://www.usenix.org/conference/usenixsecurity24/presentation/h%C3%B6ltervennhoff)

原研究核查日期：2026-10-18。以上为原稿的历史研究结论，完整支持范围、限制和待体验项见研究底稿。2026-11-02 的回填只整理既有资料并补写中文稿，未重新核查全部来源，也未执行原稿中标为待完成的体验。
