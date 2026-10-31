---
from: [sfc-ets-v1, feat-sfc-lags-v1, feat-sfc-season-v2, feat-sfc-cpi-lag6]
supersedes: [sfc-ets-v1]
updated: 2025-07-14
---
# sfc-lgbm-v2: per-segment LightGBM gives 1-month MAPE 5.1% and 3-month MAPE 6.4%
One LightGBM per segment on feat-sfc-lags-v1, feat-sfc-season-v2 and feat-sfc-cpi-lag6.
Eval on sfc-bt-2024: 1-month MAPE 5.1%, 3-month MAPE 6.4%, against 7.9% and 11.4% for sfc-ets-v1.
Under-forecasts Nov-Dec by 3.1% on sfc-oot-2025h2 (fnd-sfc-q4-low-bias).
Superseded by sfc-hier-v3 in February 2026.
