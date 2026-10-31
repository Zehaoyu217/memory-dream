---
from: [disp-find-precision-real, dec-disp-autoresolve-090, exp-305]
supersedes: [dec-disp-autoresolve-090]
updated: 2026-06-19
---
# Auto-resolve threshold moves from 0.90 to 0.95; v2 auto-resolve paused
Decision: the auto-resolve threshold is p>=0.95. Auto-resolve on disp-lgbm-v2 is paused until a model reaches 95% out-of-sample.
Basis: disp-find-precision-real (92.7-93.4% at 0.90) and exp-305 (94.7% at 0.92, short of target).
The 0.95 threshold is carried to disp-lgbm-v3 (dec-disp-fraud-score-in).
