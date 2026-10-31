---
from: [mrisk-gbm-v1, feat-mrisk-mcc-base, exp-504]
supersedes: [mrisk-gbm-v1]
updated: 2026-06-09
---
# mrisk-gbm-v2 adds MCC base rate; AUC 0.86, precision@100 0.43 on mrisk-oot-2026h1
Adds feat-mrisk-mcc-base to the v1 features; 12-month label window kept (exp-504 found no gain from 24 months).
Eval on mrisk-oot-2026h1: AUC 0.86, precision@100 0.43 (exp-505, 2026-07-06).
Superseded by mrisk-gbm-v3 on 2026-10-08.
