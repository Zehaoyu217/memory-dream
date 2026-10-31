---
from: [q-app-gini-target, find-app-gini-v3-drift, find-app-reject-inference-gain, app-gbm-v2]
updated: 2026-06-26
---
# Decision: rebuild the new-account scorecard as v4 on v10 bands, reject inference and the income estimate
Approved 2026-06-26 by Lena Fischer after find-app-gini-v3-drift (Gini 0.33 on holdout-2026q1).
Rebuild keeps the points-based form, adds feat-app-bureau-v10-band and reject-inference weights from app-gbm-v2.
Income estimate is added only after exp-506 showed the thin-file lift.
