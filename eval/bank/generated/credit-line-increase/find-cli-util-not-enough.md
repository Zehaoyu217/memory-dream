---
from: [find-cli-util-best, cli-xgb-v1, exp-103]
updated: 2025-10-22
supersedes: [find-cli-util-best]
---
# Finding: utilisation alone is not enough; the combined model reaches AUC 0.71 on holdout-2025q4
Utilisation alone gives AUC 0.64 on cli-test-2025q1; cli-xgb-v1 with payment behaviour and spend velocity reaches 0.71 on holdout-2025q4 (n=118,400).
Payment behaviour carries more signal than utilisation once both are in the model.
This overturns find-cli-util-best.
