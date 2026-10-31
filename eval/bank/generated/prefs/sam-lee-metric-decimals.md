---
updated: 2026-01-22
---
# Sam Lee reports AUC to 3 decimals and Brier score to 4 in model cards
- Model cards list AUC as 0.xxx and Brier as 0.0xxx.
- Reason: a 2-decimal AUC hid a 0.006 drop in `cli-xgb-v2` on the 2025q4 holdout that mattered for the retrain decision.
- KS and Gini sit in the same table to 2 decimals.
- Every metric carries its eval set name and n; a metric without them is treated as a draft.
