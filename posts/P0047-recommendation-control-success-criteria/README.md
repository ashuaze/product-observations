# P47｜推荐控制：先定义纠正成功的条件

- 原期号：P47；稳定 ID：P0047。
- 日期：2026-11-23（Asia/Shanghai）。
- 研究主题：推荐系统如何判断一次行为是否应该影响未来推荐？P41–P47 周期综合。
- 本篇读者价值：定义用户要纠正的推断和仍要保留的任务，避免把相似内容减少直接当作控制成功。

## 观点总结

推荐控制的验收需要同时检查不想要的后续内容、仍有价值的体验和纠正成本。Spotify 的播放控制与信号排除、YouTube 首页与下一条的不同主要依据，说明相同内容可在不同任务中有不同价值。

本次新增分析落在验收标签：Mozilla 的历史研究以相似度衡量坏推荐，其方法也承认一次拒绝未必要求排除整个话题。应保留可量化指标，并补充用户当时意图、仍有用的发现及操作成本。若整个主题或整套偏好已不合适，广泛调整仍可能合理，不把范围小作为通用最优。

## 证据边界

当前功能事实重新核查官方帮助页；历史实验保持 2021–2022 年数据背景，历史公开方案保持原年份，不外推当代效果。官方机制说明不证明满意度提升；研究方法的限制也不表示报告中的重复推荐都符合用户意图。未进行登录体验、行为实验或账号表现评估。

## 关键参考资料

- [Spotify：排除播放信号与隐藏的区别](https://support.spotify.com/us/article/exclude-playlists-or-tracks-from-your-taste-profile/)
- [YouTube：推荐主要依据与页面差异](https://support.google.com/youtube/answer/16089387?hl=en)
- [Mozilla：历史研究方法及相似度指标边界](https://www.mozillafoundation.org/en/research/library/user-controls/report/research-methodology/)

## 本周期材料

| 期号 | 实际读取的研究 | 对本期判断的贡献 |
| --- | --- | --- |
| P41 | [歌单与曲目信号](../P0041-spotify-taste-profile-context/research.md) | 保留活动，调整解释范围。 |
| P42 | [跨页面反馈](../P0042-youtube-feedback-surfaces/research.md) | 分页面检验，并检查指标语义。 |
| P43 | [双赞与反馈强度](../P0043-netflix-double-thumbs-feedback/research.md) | 输入更细仍不等于知道偏好原因。 |
| P44 | [私密项目与完成阶段](../P0044-pinterest-private-boards-task-completion/research.md) | 保存、可见范围与持续发现是不同需求。 |
| P45 | [关键词暂停有效期](../P0045-facebook-keyword-snooze-expiry/research.md) | 随时间复核用户意图。 |
| P46 | [重置与保留选择](../P0046-tiktok-instagram-recommendation-reset/research.md) | 广泛修复的例外与恢复成本。 |

## 文件

- [中文审稿摘要、完整研究与来源](research.md)
- [英文发布稿](publish-en.md)
- [独立中文发布稿](publish-zh.md)
- [元数据与指纹](metadata.yaml)

本期为 pending / draft，归档不代表人工批准或已发布到 X。
