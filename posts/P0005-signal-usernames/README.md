# P0005｜Signal usernames：一个标识符，不必承担所有身份工作

**日期：** 2026-10-12（Asia/Shanghai）  
**研究主题：** 身份与隐私  
**稿件状态：** 中英文均为草稿，待人工审稿

拆开注册、发现、展示和身份验证，比较隐私与可达性的取舍。

## 观点总结

- Signal username 的主要作用是建立首次联系，不是登录名、聊天中的公开 handle 或身份凭证；接受消息请求后，界面转而显示 profile name。
- 默认设置体现了两种不同隐私：手机号默认不向尚未保存它的人显示，但“可通过手机号找到我”默认仍为 Everybody。想只通过 username 建立新联系，需要另行关闭手机号发现，因此隐私增强会带来可达性下降。
- username 可更换或删除，QR code/URL 还能独立重置；这些操作阻止旧地址开启新联系，但不会切断已经建立的聊天。它更像可撤销的“介绍地址”，不是撤回既有关系。
- 2024 博文及当前常规帮助仍把手机号描述为标准注册条件；但截至 2026-10-12，Signal 官方已在 Android beta 8.28+ 测试付费的无手机号 Signal Login。正文明确写成 beta 例外，不能再声称所有版本都必须以手机号注册。
- 资料仅证明功能与官方解释，没有用户研究或实验支持“用户名降低骚扰”“提高采用率”或“beta 方案更安全”等效果判断。

## 阅读入口

| 材料 | 用途 |
|---|---|
| [研究底稿](research.md) | 原审稿摘要、研究论证、反例、边界与完整来源 |
| [中文发布稿](publish-zh.md) | 本次补写的 4 条独立中文串帖 |
| [英文发布稿](publish-en.md) | 保留原有词句的 6 条英文串帖 |
| [结构化元数据](metadata.yaml) | 稳定期号、来源指纹与稿件状态 |

## 参考资料与边界

- [参考资料 1](https://support.signal.org/hc/en-us/articles/6712070553754-Phone-Number-Privacy-and-Usernames)
- [参考资料 2](https://support.signal.org/hc/en-us/articles/6829998083994-Phone-Number-Privacy-and-Usernames-Deeper-Dive)
- [参考资料 3](https://signal.org/blog/phone-number-privacy-usernames/)
- [参考资料 4](https://support.signal.org/hc/en-us/articles/11197884108826-Phone-Numberless-Registration-for-Android-beta)
- [参考资料 5](https://support.signal.org/hc/en-us/articles/11228705649690-Two-factor-authentication-and-TOTP-Time-based-One-Time-Password)

原研究核查日期：2026-10-12。以上为原稿的历史研究结论，完整支持范围、限制和待体验项见研究底稿。2026-11-02 的回填只整理既有资料并补写中文稿，未重新核查全部来源，也未执行原稿中标为待完成的体验。
