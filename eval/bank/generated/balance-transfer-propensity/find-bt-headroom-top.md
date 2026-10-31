---
from: [bt-xgb-v1]
updated: 2025-05-20
---
# Finding: limit headroom ranks first in the first xgb, AUC 0.81; overturned later
In bt-xgb-v1 the limit headroom feature ranked first by gain, and random-split AUC was 0.81.
That looked too strong for one feature family, so it was flagged before any scoring. Nothing was mailed on it.
Overturned by find-bt-limit-leak.
