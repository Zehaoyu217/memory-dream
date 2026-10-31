---
from: [ds-txc-mcc-crosswalk]
updated: 2025-07-15
---
# feat-txc-mcc-prior: per-merchant prior over categories from the MCC crosswalk
For each merchant, a 23-dimensional prior: the crosswalk distribution for its MCC, smoothed toward uniform for ambiguous codes.
Adds +0.03 macro-F1 to txc-logreg-v1 on holdout-2025q2 (0.71 to 0.74, exp-102).
Kept in txc-gbm-v2 and txc-gbm-v3.
