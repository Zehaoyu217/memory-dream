---
from: [feat-app-util-new, feat-app-velocity-apps, ds-app-applications-2024]
updated: 2025-08-06
---
# app-scorecard-v3: points-based logistic scorecard, Gini 0.41 on holdout-2025q1 (n=21,300)
Points scorecard built with logistic regression on utilisation, velocity and the v8 bureau score; deployed 2025-08-18.
Eval: holdout-2025q1 (n=21,300), Gini 0.41, KS 0.36, bad rate 4.6%.
Gini drops to 0.33 on holdout-2026q1 (find-app-gini-v3-drift). Superseded by app-scorecard-v4 (2026-10-22).
