# P0033 研究底稿

核查日期：2026-11-09（北京时间）。本期为 P27–P33「隐私与默认设置」周期综合。

## 中文审稿摘要

- 隐私默认值至少有四个验收面：收集精度、可见对象与字段、计时起点、离开产品的副本。单个开关的状态无法代替结果检查。
- 同一对象可以有不同结果：Strava 活动公开时仍可隐藏路线首尾；Google 相册不在相册里分享地点，另行下载并发送的文件仍可能带有设备原始位置。
- 更严格的默认值会改变任务能否完成：Strava 仅关注者可见的活动不进公开路段榜。可比较统一收紧与按任务显式扩大范围。
- 建议做配对测试：先让用户预测结果，每次只改一个条件，从接收方检查实际暴露或残留，并记录任务是否做得完。这是评审方法，尚无效果数据。

## 中文研究底稿

**研究问题。** 为日常查找、分享和记录设计默认值时，团队什么时候应统一收紧范围，什么时候应该让默认值随任务区分？这里的用户既是数据发出者，也可能是晚些时候查看内容的接收者。保守默认可以减少某些路径上暴露的数据；公开排行、精确导航和保留原件也可能是用户主动选择的任务。

**事实与对应来源。**

| 验收面 | 本次核查到的行为 | 适用条件 |
|---|---|---|
| 收集 | App 请求精确位置时，用户仍可授予大致位置。[^android] | Android 12 及以上运行时权限；系统版本及请求方式有差异。找店与导航是评审示例，未测准确性。 |
| 可见对象与字段 | Strava 允许公开活动并遮住路线首尾；仅关注者可见的活动不会进入公开路段榜。YouTube 不公开列出的视频可被任何持链接者观看和转发；被加入公开播放列表时还有搜索例外。[^maps][^strava][^yt] | Strava 地图可见性与活动受众是两项设置。地图遮挡也可能影响隐藏部分的路段上榜；不能将遮挡当作无法推断位置。 |
| 到期 | 桌面 Chrome 关完所有无痕窗口才结束会话，下载文件仍保留。Signal 已开启阅后即焚时，发送端从发送计时，接收端从阅读计时；适用于设置后新发送的消息。[^chrome][^signal] | 比较的是触发条件。浏览器会话不是消息计时，聊天删除也不是禁止接收方留副本。 |
| 副本 | Google 相册可控制相册内是否分享地点；下载后用邮件附件分享，Google 相册内的修改不会覆盖设备保存的原始地点。[^photos] | 限于相机写入地点的照片和文档所述路径；不推广到所有导出方式，也不保证遮挡地点后无法从画面推断。 |

**同任务对照与反证。** 以「记录一次骑行」为同一基线。一律仅关注者可见，规则统一，用户不用逐次选择，但会丢掉公开路段参赛；另一设计是普通记录默认限制受众、用户选择参加公开排行时再说明会扩大哪些字段的可见范围。后者保留选择，但增加决策成本，也可能让参与者误判分享范围。Strava 的现行上榜限制是前者的具体反例；后者是设计方案，非对 Strava 现有界面或效果的描述。原件备份需要定位时，「每次导出都删除坐标」也会丢失用户要保留的信息；能否区分原件备份与对外分享，取决于产品能否识别用户任务。

**新增判断与边界。** 用同一内容、同一任务做配对检查。对照组保留常规路径，另一组只改一个条件，例如相册分享换成附件；先记录对结果的预测，再由实际查看方核对字段、残留和任务结果。只有当额外精度或更广受众服务于明确任务时，才值得在那个动作上请求；若同一规则在各路径真的一致、且原任务都能完成，一条规则可能更易理解。跨产品案例用来暴露检查维度，不用来排名产品，也不证明设置一定提高信任或减少泄露。

**尚未解决。** 没有真实行为数据或端到端实测。可随机分配相同任务和素材，对比单一默认值与任务内按需授权的原型，记录错误预测率、实际可见字段、任务完成率及额外操作。如果按需方案没有减少错误预测或超出任务所需的暴露，却使合理任务更难完成，就应重新考虑这套拆分。

**周期底稿。** 已回读 [P27 Strava](../P0027-strava-privacy-defaults/research.md)、[P28 位置精度](../P0028-location-permission-precision/research.md)、[P29 链接访问](../P0029-youtube-unlisted-link-access/research.md)、[P30 无痕模式](../P0030-chrome-incognito-observer-boundaries/research.md)、[P31 消息计时](../P0031-disappearing-message-clocks/research.md)、[P32 照片导出](../P0032-photo-location-export-boundaries/research.md)。下列本期引用的功能规则均于当次重新打开核查。

## 核查来源

[^android]: Android Developers，《Request location access at runtime》。https://developer.android.com/develop/sensors-and-location/location/permissions/runtime
[^maps]: Strava Support，《How Do I Edit My Map Visibility on Strava?》。https://support.strava.com/en-us/articles/15402012-how-do-i-edit-my-map-visibility-on-strava
[^strava]: Strava Support，《How Do My Activity Privacy Controls Work on Strava?》。https://support.strava.com/en-us/articles/15401987-how-do-my-activity-privacy-controls-work-on-strava
[^yt]: YouTube Help，《Change video privacy settings》（电脑端）。https://support.google.com/youtube/answer/157177?hl=en
[^chrome]: Google Chrome Help，《Browse in Incognito mode》（电脑端）。https://support.google.com/chrome/answer/95464?hl=en
[^signal]: Signal Support，《Set and manage disappearing messages》。https://support.signal.org/hc/en-us/articles/360007320771-Set-and-manage-disappearing-messages
[^photos]: Google Photos Help，《Understand, find & edit your photos’ locations》（电脑端）。https://support.google.com/photos/answer/6153599?hl=en

## 发稿前检查

- 新增认识：用四个验收面和单变量配对测试，将默认值的界面承诺对到接收端行为。
- 证据与反证：官方规则支持案例事实；公开榜与原件用途改变了推荐做法。比较保持相同任务或内容，没有从文档推断效果。
- 决策用途：先保留完成常规任务所需的数据，验证更宽范围是否只在明确任务中有用；记录会推翻判断的结果。
- 官方 twitter-text 3.1.0 加权长度（含序号及随帖 URL）：英文 235 / 241 / 212 / 229 / 198 / 251；中文 155 / 150 / 153 / 165 / 151 / 160。各条均不超过 280。
