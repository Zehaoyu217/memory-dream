---
from: [exp-106-oot-2026h1]
updated: 2026-07-10
---
# Finding: bt-xgb-v2 loses 0.02 AUC out of time (0.68 to 0.66) because of the 2026 limit policy
Out-of-time AUC for bt-xgb-v2 on bt-oot-2026h1 is 0.66. PSI 0.27 on the utilization trend.
The January 2026 limit-policy change raised average limits, so utilization levels moved for the same behaviour.
Retrain cadence moves to quarterly; bt-xgb-v3 picks up 2026 H1 data at the next retrain.
