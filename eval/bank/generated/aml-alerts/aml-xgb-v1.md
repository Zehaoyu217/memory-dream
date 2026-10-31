---
from: [feat-aml-structuring-v1, feat-aml-new-counterparty, ds-aml-dispositions]
updated: 2026-01-20
---
# aml-xgb-v1: first alert-priority ranker, structuring and counterparty features
XGBoost ranker that orders the analyst queue by SAR likelihood; it does not close alerts.
Trained on 2025 dispositions with two features in v1; AUC 0.84 on Jul-Sep 2025 dispositions (exp-402).
Superseded by aml-xgb-v2 on 2026-03-30.
