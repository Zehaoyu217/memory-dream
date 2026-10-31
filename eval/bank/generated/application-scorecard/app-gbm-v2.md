---
from: [app-gbm-v1, find-app-reject-inference-gain]
updated: 2026-04-08
supersedes: [app-gbm-v1]
---
# app-gbm-v2: monotone-constrained GBM with reject-inference weights, Gini 0.44 on holdout-2025q1
Monotone constraints on utilisation and the v8 score, sample weights from the reject-inference parcelling.
Eval: holdout-2025q1 (n=21,300), Gini 0.44, KS 0.40; the constraint costs 0.02 Gini against v1 (exp-504).
Reference model for the v4 rebuild; not deployed.
