# P45｜Facebook Keyword Snooze：一次拒绝，多久到期？

- 原期号：P45；稳定 ID：P0045。
- 日期：2026-11-21（Asia/Shanghai）。
- 研究主题：推荐系统如何判断一次行为是否应该影响未来推荐？P41–P47 周期中的短观察。
- 本篇读者价值：把负反馈的对象与持续时间分开判断，避免用暂停的采用量直接决定到期日。

## 观点总结

Facebook 在 2018 年的 Keyword Snooze 实验中先使用 30 天暂停，团队看到部分使用高峰后又试了 7 天。这提供了检查反馈时效性的案例，但不能证明较短的暂停更合适。新增暂停的时间分布，不等于同一批用户希望恢复内容的时间分布。

短暂停可能增加续期操作，长暂停可能错过后来有用的内容。可借鉴的判断是为临时需求提供可理解的到期时间，同时让持续偏好有持续生效的选择。实际比较应检查恢复后的不想要内容与仍有价值的发现。

## 证据边界

这是已结束的历史实验：官方在 2021-01-13 的更新中明确说明实验已结束。两篇被核查的团队文章没有报告 7 天对 30 天的效果比较，没有支持某个时长获胜或解释结束原因。本次没有登录体验或独立行为实验，不推断关键词暂停对推荐模型训练的具体影响，也不将它混同为对人、主页或群组的普通 Snooze。

## 关键参考资料

- [Facebook 团队：Keyword Snooze: People Turn Down the Noise（2018）](https://about.fb.com/news/2018/08/inside-feed-keyword-snooze-people-turn-down-the-noise/)
- [Facebook 实验公告及 2021 年结束更新](https://about.fb.com/news/2018/06/keyword-snooze-a-new-way-to-help-control-your-news-feed/)

## 文件

- [中文审稿摘要与研究底稿](research.md)
- [英文发布稿](publish-en.md)
- [中文发布稿](publish-zh.md)
- [元数据与正文指纹](metadata.yaml)

归档保留为 pending / draft，不代表人工批准或已在 X 发布。
