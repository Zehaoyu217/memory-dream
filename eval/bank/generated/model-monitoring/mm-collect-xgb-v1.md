---
from: [ds-mm-collections-labels, feat-mm-payment-ratio-v1, feat-mm-days-past-due-3m, ds-mm-reference-train]
updated: 2025-02-03
---
# mm-collect-xgb-v1: collections propensity, 38 features, AUC 0.733
Gradient-boosted trees predicting a 60-day-to-charge-off-or-cure outcome, with 38 input features.
Evaluated on mm-oot-2024h2 (n=96,000 accounts): AUC 0.733, KS 0.31.
Superseded by mm-collect-xgb-v2 (2025-08-12).
