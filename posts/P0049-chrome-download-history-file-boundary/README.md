# P49｜Chrome 下载记录：列表清空后，文件还在吗？

- 原期号：P49；稳定 ID：P0049。
- 日期：2026-11-25（Asia/Shanghai）。
- 研究主题：产品如何让用户分清本机副本、同步内容与独立备份？P48–P54 周期短观察。
- 本篇读者价值：区分下载活动记录与已保存文件，为整理列表和回收文件空间选择不同的动作范围。

## 观点总结

桌面版 Chrome 从下载历史移除记录、或清空下载历史，都不会删除电脑上已经保存的下载文件。Show in folder 可提供从记录找到文件的路径。

整理最近活动同时保留资料，是一个合理目标；回收下载文件占用的空间，则需要处理文件本身。产品应说明动作修改记录、文件，还是两者。本文不把更空的列表当作文件已删除或对应空间已回收的证据，也不主张清理记录必须同时删除资料。

## 证据边界

功能事实限于官方 Computer 帮助页所述桌面 Chrome，不套用手机端规则。API 文档用于交叉核对历史对象与文件操作的区别，不证明原生下载页在所有版本中的刷新细节。没有实际删除文件、清理历史、截图或用户测试；对命名和任务匹配的建议属于分析。

## 周期衔接

已读取 [P48 底稿](../P0048-onedrive-free-space-offline-access/research.md)。P48 区分可见、保留与离线可用，本篇增加活动记录与实际保存内容的区别，不重复 OneDrive 按需文件功能。

## 关键参考资料

- [Chrome Help：下载文件、移除历史记录与定位文件](https://support.google.com/chrome/answer/95759?hl=en&co=GENIE.Platform%3DDesktop)
- [Chrome Help：清除浏览数据的作用范围](https://support.google.com/chrome/answer/2392709?hl=en&co=GENIE.Platform%3DDesktop)
- [Chrome Developers：下载 API 的历史与文件操作](https://developer.chrome.com/docs/extensions/reference/api/downloads)

## 文件

- [中文审稿摘要与研究底稿](research.md)
- [英文发布稿](publish-en.md)
- [独立中文发布稿](publish-zh.md)
- [元数据与正文指纹](metadata.yaml)

本期为 pending / draft，归档不代表人工批准或已在 X 发布。
