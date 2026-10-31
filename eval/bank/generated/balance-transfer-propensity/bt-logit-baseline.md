---
from: [feat-bt-util-3m, ds-bt-bureau-join]
updated: 2025-04-02
---
# bt-logit-baseline: L2 logistic on bureau score, utilization and tenure, AUC 0.63
Regularized logistic regression (C=0.5) on bureau score band, feat-bt-util-3m and tenure months.
AUC 0.63 on bt-holdout-2025q1 (n=41,800), KS 0.19, top-30% lift 1.4x. Trained on 2025 waves excluding holdout accounts.
Reference model only; no longer scored in production.
