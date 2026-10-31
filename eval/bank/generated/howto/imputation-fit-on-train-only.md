---
updated: 2026-06-09
---
# Fit imputers, scalers and caps on the training split only, then apply them to OOT
Any imputer, scaler or capping statistic is fitted on the training split and applied unchanged to validation and OOT. Fitting on the full table let OOT means leak into the 2025 limit model, which inflated its OOT AUC by 0.011.
