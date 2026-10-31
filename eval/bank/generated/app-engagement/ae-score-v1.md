---
from: [feat-ae-active-days-v1, feat-ae-depth-v1, feat-ae-push-open-v1]
updated: 2025-12-22
---
# Engagement score v1: equal-weight blend of active days, depth and push open rate, 0 to 100
Each input is standardised on the score population. Weights 0.375, 0.375 and 0.25 (push open).
AUC 0.73 for 90-day attrition on holdout-2025q4 (n = 610,000 accounts), measured in exp-502.
Superseded by ae-score-v2, which drops push credit and refits the weights.
