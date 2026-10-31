---
from: [exp-102, exp-103, feat-c25-util-v1, dec-c25-label-60d]
updated: 2025-03-10
---
# churn-gbm-2025 (v1): LightGBM with util-v1, holdout AUC 0.741
- LightGBM on 14 features including util-v1 and app sessions, 60-day labels, 600 rounds.
- Holdout c25-oot-2024h1 (n=312,470): AUC 0.741, KS 0.36, recall@10% 0.29, Brier 0.0352.
- Beats churn-lr-base-2025 by 0.048 AUC. Piloted from April 2025 under dec-c25-ship-gbm-v1.
