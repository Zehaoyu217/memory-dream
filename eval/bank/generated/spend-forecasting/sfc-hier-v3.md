---
from: [sfc-lgbm-v2, feat-sfc-active-accounts, fnd-sfc-q4-reconciled, exp-207]
supersedes: [sfc-lgbm-v2]
updated: 2026-02-09
---
# sfc-hier-v3 is the current segment forecast: total MAPE 2.3% on sfc-oot-2025h2
LightGBM base forecasts for the six segments, reconciled with MinT across segments and the total.
On sfc-oot-2025h2 (Jul-Dec 2025): total MAPE 2.3% and segment MAPE 4.9%, against 2.9% and 5.1% for sfc-lgbm-v2 (exp-207).
Adds feat-sfc-active-accounts as a regressor. Q4 bias is -0.4%.
Adopted for finance FY26 volume (dec-sfc-ship-hier-v3).
