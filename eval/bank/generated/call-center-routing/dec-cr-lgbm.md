---
from: [exp-101, cr-logreg-v1, cr-lgbm-v1]
updated: 2026-02-20
---
# Adopt LightGBM over logistic regression for the routing model
LightGBM beats logistic regression by 0.13 macro F1 on holdout-2025q4 with the same features (exp-101: 0.738 vs 0.61).
Agreed at the router review on 2026-02-20 with Sam Lee and Maya Ortiz (retention).
Logistic regression stays in the repo as the sanity baseline.
