---
from: [feat-c25-txn-recency, feat-c25-payment-behaviour, feat-c25-util-v1, feat-c25-app-sessions, ds-c25-oot-2024h1]
updated: 2025-01-27
---
# churn-lr-base-2025: logistic baseline, holdout AUC 0.693
- L2 logistic regression, C=1.0, 14 features, 60-day labels.
- Holdout c25-oot-2024h1 (n=312,470): AUC 0.693, KS 0.27, Brier 0.0371.
- Purpose: the floor each GBM must beat by a clear margin.
