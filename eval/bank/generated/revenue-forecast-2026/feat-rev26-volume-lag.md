---
from: [ds-rev26-spend-volume, ds-rev26-interchange-ledger]
updated: 2025-05-19
---
# feat-rev26-volume-lag: one-month lag of spend volume for interchange timing
Spend volume lagged by one month, matching the settlement lag in the ledger.
Without the lag, interchange MAPE on 2024-H2 is 3.4%; with it, 2.1% (exp-301).
Input to rev26-interchange-v1.
