---
from: [exp-207, feat-csb-spend-sa-v2, feat-csb-calls-unresolved, fnd-csb-calls-lift-v2, dec-csb-tenure-floor, feat-csb-deposit-volatility]
updated: 2026-02-10
supersedes: [csb-xgb-v1]
---
# csb-xgb-v2: XGBoost with seasonally adjusted spend, holdout AUC 0.758 on 6-month-plus SMB accounts
- Five features: spend-sa-v2, deposit volatility, tenure band, employee cards, unresolved calls. 90-day labels.
- Holdout csb-oot-2025q1, 6-month-plus subset (n=7,930): AUC 0.758, KS 0.40, recall@10% 0.31.
- Current churn-small-business scoring model; shipped by dec-csb-ship-xgb-v2.
