---
from: []
updated: 2025-09-15
---
# ml.legacy_feats_v1 holds 214 features across nine notebooks, 18.4M account-months
The features are hand-built SQL in nine notebooks under `ml/feats/`, written monthly to `ml.legacy_feats_v1`, one row per account per month-end.
Coverage: 18.4M rows from 2019-01 to 2025-06.
Sources: `cards.txn_daily`, `cards.payments_daily`, `cards.limits_history`, `bureau.scores_monthly`.
Month-end windows are computed in local time, not UTC (see fnd-parity-pre-fix).
Refresh is manual, on the Monday after month close, owned by Aisha Khan.
