---
from: [ds-fsm-legacy-features]
updated: 2025-10-02
---
# fsm-churn-xgb-v1: churn model on 40 legacy features, holdout AUC 0.782
Gradient-boosted trees on 40 features read from `ml.legacy_feats_v1`, trained on monthly snapshots from 2019 to 2024.
Evaluated on holdout-2025q2 (n=412,000 accounts): AUC 0.782, KS 0.41.
Superseded by fsm-churn-xgb-v2 (2026-02-19).
