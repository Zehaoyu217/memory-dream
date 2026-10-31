---
from: [fraud25-gbm-v2, feat-f25-mcc-travel, exp-106]
updated: 2025-09-22
---
# fraud25-gbm-v3 halves the travel flag: AUC 0.909, not promoted
Challenger built 2025-09-22 with the travel flag multiplied by 0.5 before training.
Holdout-2025q1 AUC 0.909 against 0.911 for v2 (exp-107); travel share of alerts falls from 31% to 17%.
Not promoted (dec-f25-no-v3, 2025-10-01); the rebuild was deferred to fraud-2026.
