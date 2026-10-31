---
from: [sfc-hier-v3, exp-207, fnd-sfc-q4-reconciled]
updated: 2026-02-10
---
# Decision: adopt sfc-hier-v3 as the segment volume forecast for finance
sfc-hier-v3 becomes the segment spend forecast used for FY26 volume, in place of sfc-lgbm-v2.
Basis: total MAPE 2.3% and Q4 bias -0.4% on sfc-oot-2025h2.
Downstream: revenue-forecast-2026 uses it as the spend volume input for interchange.
