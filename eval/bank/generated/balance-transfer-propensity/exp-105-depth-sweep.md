---
from: [feat-bt-util-trend-v2, feat-bt-limit-headroom]
updated: 2025-08-22
---
# exp-105: depth 5 beats depth 3 and 7 on bt-holdout-2025q1
Depth sweep on the v2 feature set, 400 trees, learning rate 0.05.
On bt-holdout-2025q1 (n=41,800): depth 3 AUC 0.66, depth 5 AUC 0.68, depth 7 AUC 0.67 with a wider train/holdout gap.
Depth 5 chosen for bt-xgb-v2. The holdout was used for this choice, so the reported 0.68 carries a small selection bias.
