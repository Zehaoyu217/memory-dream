---
from: [exp-403, feat-ror-churn-score, feat-ror-offer-fatigue, feat-ror-value-band-v1]
updated: 2025-10-31
---
# ror-uplift-v1: T-learner retention uplift on churn score, offer fatigue and value band
- Trained on the July 2025 wave; features churn score (churn-2025 churn-gbm-2025-v2), offer fatigue and value band v1.
- Holdout uplift@20% 2.4pp against 1.0pp random (exp-403).
- Input to ror-roi-v1.
