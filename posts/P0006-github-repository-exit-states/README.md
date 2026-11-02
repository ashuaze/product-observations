# P0006｜GitHub Archive、Transfer 与 Delete：退出项目不是一个动作

**日期：** 2026-10-13（Asia/Shanghai）  
**研究主题：** 反悔、退出与恢复  
**稿件状态：** 中英文均为草稿，待人工审稿

把停止维护、移交、移除与恢复拆成不同任务。

## 观点总结

- 核心判断：产品不应把“离开”压成一个动作。停止维护、移交责任、移除可见性和误删恢复，是四个不同任务。
- 关键证据：Archive 可撤销且保留可搜索的只读资料；Transfer 延续项目，但 Pages 链接、权限和套餐能力并非全量无损迁移。
- 重要边界：Delete 的影响取决于仓库关系和可见性——公共仓库的 fork 保留，私有仓库的 fork 会随之删除。
- 反例修正：90 天恢复窗口并不等于完整回滚；非空 fork network 可能阻止自助恢复，团队权限也不会恢复。
- 给产品团队的判断依据：先问用户想得到什么结果，再决定动作；确认弹窗只能确认选择，不能纠正选错的任务模型。

## 阅读入口

| 材料 | 用途 |
|---|---|
| [研究底稿](research.md) | 原审稿摘要、研究论证、反例、边界与完整来源 |
| [中文发布稿](publish-zh.md) | 本次补写的 4 条独立中文串帖 |
| [英文发布稿](publish-en.md) | 保留原有词句的 6 条英文串帖 |
| [结构化元数据](metadata.yaml) | 稳定期号、来源指纹与稿件状态 |

## 参考资料与边界

- [参考资料 1](https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories)
- [参考资料 2](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository)
- [参考资料 3](https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository)
- [参考资料 4](https://docs.github.com/en/repositories/creating-and-managing-repositories/restoring-a-deleted-repository)
- [参考资料 5](https://docs.github.com/en/repositories/archiving-a-github-repository/backing-up-a-repository)

原研究核查日期：2026-10-13。以上为原稿的历史研究结论，完整支持范围、限制和待体验项见研究底稿。2026-11-02 的回填只整理既有资料并补写中文稿，未重新核查全部来源，也未执行原稿中标为待完成的体验。
