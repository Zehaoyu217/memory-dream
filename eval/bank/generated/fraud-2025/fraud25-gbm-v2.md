---
from: [fraud25-gbm-v1, feat-f25-mcc-travel, feat-f25-velocity-v1, feat-f25-device-age, feat-f25-amt-ratio, feat-f25-hour-band, ds-f25-labels]
supersedes: [fraud25-gbm-v1]
updated: 2025-06-18
---
# fraud25-gbm-v2 adds the travel flag and becomes the 2025 champion: AUC 0.911, KS 0.66
Same LightGBM setup plus feat-f25-mcc-travel, trained on 2024-07 to 2025-03 CNP transactions.
Holdout-2025q1: AUC 0.911, KS 0.66, recall@1% 0.52 (exp-104, 2025-06-12, 2,310 fraud).
Promoted 2025-06-30 (dec-f25-champion-v2). The travel flag later proved to be the cause of over-flagging.
