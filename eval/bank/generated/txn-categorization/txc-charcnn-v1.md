---
from: [feat-txc-normalise-v2, ds-txc-labelled-merchants]
updated: 2025-10-14
---
# txc-charcnn-v1 reached macro-F1 0.80 but is too slow to serve
A 1D character CNN on normalised descriptors, 6.5 GPU hours to train.
Macro-F1 0.80 on holdout-2025q2 (exp-105): 0.02 above txc-gbm-v2 and 0.01 below normalised LightGBM.
p95 latency 210 ms per 1,000 merchants, against 9 ms for LightGBM.
Not shipped; see dec-txc-drop-charcnn.
