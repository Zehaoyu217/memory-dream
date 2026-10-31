---
from: [feat-ae-depth-v2, feat-ae-active-days-v1, exp-505, dec-ae-no-push-credit]
updated: 2026-03-11
supersedes: [ae-score-v1]
---
# Engagement score v2: logistic-fitted weights on active days and depth v2, no push credit, 0 to 100
Weights fitted by logistic regression for 90-day attrition on the training split. Inputs: ae_act28 and depth v2. Push open rate removed.
AUC 0.76 for 90-day attrition on holdout-2025q4 (n = 610,000), measured in exp-505. Current score.
