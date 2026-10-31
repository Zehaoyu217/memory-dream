---
from: [app-scorecard-v3, feat-app-thin-file, feat-app-velocity-apps]
updated: 2026-01-12
supersedes: []
---
# app-gbm-v1: gradient-boosted challenger, Gini 0.46 on holdout-2025q1 but not explainable
Boosted trees on the v3 features plus the thin-file flag and velocity; same holdout as v3.
Eval: holdout-2025q1 (n=21,300), Gini 0.46, KS 0.39.
Fails the adverse-action explanation test in exp-503; superseded by app-gbm-v2 (2026-04-08) as the reference model.
