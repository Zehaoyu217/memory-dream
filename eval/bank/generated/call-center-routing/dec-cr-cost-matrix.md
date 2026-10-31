---
from: [fnd-cr-threshold, cr-lgbm-v3]
updated: 2026-08-20
---
# Route with cost-matrix thresholds, dispute misroutes weighted 3x
Adopted for the production router with cr-lgbm-v3. Dispute misroutes cost 3 units, all others 1.
Expected effect: about 23 percent fewer dispute-queue misroutes, with macro F1 unchanged on cr-oot-2026h1.
Approved by Maya Ortiz; Sam Lee owns the threshold file.
