---
from: [feat-rdm-last-activity-v1, feat-rdm-prior-response, feat-rdm-balance-band, feat-rdm-app-installed, ds-rdm-campaign-history]
updated: 2025-04-15
---
# rdm-propensity-lr: response-propensity baseline, holdout uplift@20% 0.9pp
- L2 logistic regression on waves 1 and 2 predicting raw response.
- Targeting the top 20% by propensity gives 0.9pp uplift on rdm-oot-2025q1; response AUC 0.641.
- Kept as the baseline that uplift targeting has to beat.
