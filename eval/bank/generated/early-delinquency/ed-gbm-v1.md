---
from: [feat-ed-util-trend-v1, feat-ed-cashadv-v1]
updated: 2025-03-24
supersedes: []
---
# ed-gbm-v1 is a LightGBM model on utilisation trend and cash advances, the first gradient-boosted candidate
LightGBM, 400 trees, learning rate 0.05, leaves 31. Features: feat-ed-util-trend-v1 and feat-ed-cashadv-v1.
On early-delinquency-holdout-2024q4 (exp-202): AUC 0.781, Gini 0.562, KS 0.42.
Superseded by ed-gbm-v2 (2025-09-10). It does not use the limit-change feature.
