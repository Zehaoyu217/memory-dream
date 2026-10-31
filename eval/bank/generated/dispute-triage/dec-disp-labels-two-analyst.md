---
from: [q-disp-label-source, ds-disp-analyst-labels]
updated: 2026-02-10
---
# Train dispute models only on two-analyst agreement labels (7,450 of 8,900)
Decision: use only labels where two analysts agree; drop single-labelled disputes from training.
Basis: single-analyst labels are noisy and the 400 double-labelled set gives kappa 0.71.
Applies to disp-lgbm-v1 onward.
