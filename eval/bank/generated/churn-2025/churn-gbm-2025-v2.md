---
from: [exp-106, feat-c25-util-v2, feat-c25-txn-recency, feat-c25-payment-behaviour, dec-c25-drop-app-sessions]
updated: 2025-05-26
supersedes: [churn-gbm-2025]
---
# churn-gbm-2025-v2: LightGBM with util-v2 and monotone recency, holdout AUC 0.772
- 13 features: util-v2, transaction recency (monotone), payment behaviour, card and bureau fields; no app sessions.
- 60-day labels. Holdout c25-oot-2024h1 (n=312,470): AUC 0.772, KS 0.41, recall@10% 0.34, Brier 0.0334.
- Current churn-2025 scoring model. The churn-2026 project later replaced this line with its own churn-xgb models; that work is outside this project.
