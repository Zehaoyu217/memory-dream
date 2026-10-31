---
from: [ds-pa-balance-panel, feat-pa-bt-inflow-v2, balance-transfer-propensity/bt-xgb-v3]
updated: 2026-09-04
---
# pa-bal-forecast-v1: balance path to month 24 by arm, exponential decay after expiry
Fits a balance path from observed months 1 to 6 with an exponential decay after promo expiry. Uses the external BT inflow (feat-pa-bt-inflow-v2) and a BT propensity score from balance-transfer-propensity/bt-xgb-v3.
Holdout error: MAPE 11% on 12-month balance, against 19% for a flat-balance forecast (exp-506).
