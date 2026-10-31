---
from: [find-ed-limit-leak, q-ed-limit-feature-usable]
updated: 2025-07-10
---
# Decision: drop feat-ed-limit-change-v1 from all early-delinquency models
Agreed 2025-07-10 by Lena Fischer and Aisha Khan after find-ed-limit-leak.
The feature's gain is leakage from limit cuts made after delinquency started. Residual gain of 0.002 AUC is not worth the production risk.
Removed from ed-gbm-v2 and excluded from all later builds.
