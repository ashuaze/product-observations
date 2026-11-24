# P48｜OneDrive 释放空间：云端还在，离线还能打开吗？

- 原期号：P48；稳定 ID：P0048。
- 日期：2026-11-24（Asia/Shanghai）。
- 研究主题：产品如何让用户分清本机副本、同步内容与独立备份？P48–P54 周期首篇。
- 本篇读者价值：把文件保留的位置、同步删除范围与访问条件分开判断，给清理存储的产品流程定义更完整的成功标准。

## 观点总结

OneDrive Windows 的按需文件中，Free up space 将文件改为仅联机，保留云端文件；删除已同步文件会影响云端和其他同步设备。文件仍出现在资源管理器，也可能已经不能离线打开。

保留云端内容可以避免把设备侧清理变成同步删除，但仍需考虑下一次任务的网络条件。始终在本机保留可支持离线访问，代价是磁盘容量和下载。可以测试在清理选择旁说明保留位置和联网要求，并同时检验空间回收与后续访问。

## 证据边界

功能事实限于 Windows 中启用 OneDrive Files On-Demand 的同步文件，假设目标文件已成功同步。未保证各地区、账号、策略和设备界面一致，不外推 macOS 或其他云盘。删除可能有回收站恢复路径，不描述成必然立即永久丢失。文中的结果文案属于提案；没有测试其效果，也未进行账号实测或截图。

## 周期衔接

已读取 [P47 综合底稿](../P0047-recommendation-control-success-criteria/research.md)。本篇延续“检查用户仍想完成的任务”的验收思路，转向文件系统中“可见、保留、可打开”的区别。后续将按实际证据研究副本、同步及备份的其他边界，不将本篇机械拆分发布。

## 关键参考资料

- [Microsoft：Windows 按需文件说明](https://support.microsoft.com/en-us/onedrive/save-disk-space-with-onedrive-files-on-demand-for-windows)
- [Microsoft：在资源管理器使用同步文件](https://support.microsoft.com/en-us/sharepoint/sync/work-with-synced-files-in-file-explorer)
- [Microsoft：电脑与 OneDrive 的同步规则](https://support.microsoft.com/en-us/onedrive/sync-your-computer-s-files-and-folders-with-onedrive)

## 文件

- [中文审稿摘要与研究底稿](research.md)
- [英文发布稿](publish-en.md)
- [独立中文发布稿](publish-zh.md)
- [元数据与指纹](metadata.yaml)

本期为 pending / draft，归档不代表人工批准或已在 X 发布。
