---
from: [exp-204, feat-csb-spend-raw, feat-csb-tenure-band, feat-csb-deposit-volatility, dec-csb-tenure-floor]
updated: 2025-11-03
---
# csb-xgb-v1: XGBoost on raw spend, 6-month-plus SMB accounts, holdout AUC 0.742
- Features: spend-raw, tenure band, deposit volatility, employee cards. 90-day labels.
- Holdout csb-oot-2025q1, 6-month-plus subset (n=7,930): AUC 0.742, KS 0.37, recall@10% 0.27, precision@10% 0.19.
- Piloted from December 2025 under dec-csb-ship-xgb-v1. Superseded by csb-xgb-v2.
