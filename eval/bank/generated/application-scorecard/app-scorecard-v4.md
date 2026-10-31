---
from: [app-gbm-v2, feat-app-bureau-v10-band, feat-app-income-est, exp-507]
updated: 2026-10-22
supersedes: [app-scorecard-v3]
---
# app-scorecard-v4: rebuilt points scorecard on v10 bands and income estimate, Gini 0.42 out of time
Points-based logistic scorecard keeping the explainable form, with feat-app-bureau-v10-band, feat-app-income-est and reject-inference weights.
Eval: application-scorecard-oot-2026h1 (n=61,700), Gini 0.42, KS 0.38, bad rate 4.9%.
Replaces app-scorecard-v3 once dec-app-cutoff-v4 is in force.
