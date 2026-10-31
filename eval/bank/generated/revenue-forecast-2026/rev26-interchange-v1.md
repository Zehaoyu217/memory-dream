---
from: [feat-rev26-interchange-bps, feat-rev26-volume-lag]
updated: 2025-05-27
---
# rev26-interchange-v1: volume times MCC-group bps gives 2.1% MAPE on 2024-H2
Interchange revenue = lagged spend volume times blended bps by MCC group.
Backtest on 2024-H2: MAPE 2.1%, against 4.8% for a flat rate.
Still in use for interchange. Volume source is spend-forecasting/sfc-hier-v3 from 2026.
