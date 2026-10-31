---
from: [cr-lgbm-v2, fnd-cr-threshold, ds-cr-intent-labels, exp-106]
updated: 2026-08-18
supersedes: [cr-lgbm-v2]
---
# LightGBM v3 is the current router: macro F1 0.74 and top-1 0.81 on cr-oot-2026h1 (n = 410,000)
Trained on adjudicated labels for the 1,200 double-coded calls (ds-cr-intent-labels) and routed with the cost-matrix thresholds from fnd-cr-threshold.
Macro F1 0.74 and top-1 accuracy 0.81 on cr-oot-2026h1, scored 2026-08-18. Relabelling accounts for +0.02 top-1.
Dispute-queue misroutes fall 23 percent against v2 with default thresholds, with macro F1 unchanged.
Feature set unchanged from v2.
