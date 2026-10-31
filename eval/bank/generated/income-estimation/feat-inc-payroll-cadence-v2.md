---
from: [feat-inc-payroll-cadence-v1, exp-403]
updated: 2025-12-16
supersedes: [feat-inc-payroll-cadence-v1]
---
# feat-inc-payroll-cadence-v2: adds inflow stability (coefficient of variation) to the cadence flag
Keeps the v1 cadence flag and adds the coefficient of variation of inflows over 6 cycles, with a stability flag below 0.15.
Coverage unchanged at 38%; MAPE on covered accounts improves from 26% to 23% (exp-403).
Used in inc-gbm-v2 onward.
