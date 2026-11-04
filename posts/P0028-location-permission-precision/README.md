# P28｜定位权限：把精确位置留给真正需要它的一步

2026-11-04 · P0028 · 隐私与默认设置（P27–P33）

**读者价值：** 用附近浏览和逐向导航的差异，决定何时请求精确数据，以及拒绝后还应保留哪些功能。

**判断：** 把精度匹配到当前任务。浏览先支持低精度或手动输入；逐向导航确实依赖精度时再提出明确请求。验收要看任务完成和暴露范围，不能只看同意率。

**证据边界：** 平台文档说明权限能力；Apple Maps 为 iOS 14 时期的团队案例，研究为历史观察数据。本期无设备实测，不估计现版产品效果。

- [中文研究底稿](research.md)
- [中文发布稿](publish-zh.md)
- [英文发布稿](publish-en.md)
- [元数据](metadata.yaml)

关键参考：[Android 开发文档](https://developer.android.com/develop/sensors-and-location/location/permissions/runtime) · [Apple Maps 设计分享](https://developer.apple.com/videos/play/wwdc2020/10162/) · [USENIX 现场研究](https://www.usenix.org/system/files/sec21-cao-weicheng.pdf)
