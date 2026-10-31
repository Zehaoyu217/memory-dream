---
from: [exp-205, exp-206, fnd-seasonal-baseline]
updated: 2025-10-20
---
# Decision: limit models are monitored against the same-month-last-year reference
Adopted for mm-limit-glm-v2 and any future limit model. The flat training sample stays as the reference for the collections model, where seasonality was not a problem.
Basis: fnd-seasonal-baseline (summer alarms 7 to 2; holiday backtest 9 to 0).
