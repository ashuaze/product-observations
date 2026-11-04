### 1/4

1/4 A map app can help you find a café without knowing which doorway you're standing in. Turn-by-turn navigation is a different job. If both features share one permission gate, browsing inherits navigation's data requirements.

### 2/4

2/4 Android 12+ lets users grant approximate location even when an app asks for precise. On iOS, apps can request reduced accuracy by default, then ask for a temporary upgrade when a feature needs more. Plan for what the user actually grants.

### 3/4

3/4 In its iOS 14 design talk, Apple Maps showed a useful fallback: draw an area instead of a dot and omit some distance and ETA estimates. Ask for precision when the user starts turn-by-turn directions.
https://developer.apple.com/videos/play/wwdc2020/10162/

### 4/4

4/4 Test the refusal path: can someone still browse, enter a starting point, or recover if navigation needs more? Compare task completion, time to start, and how often precise access is granted for browsing. A higher grant rate can hide a worse trade-off.
