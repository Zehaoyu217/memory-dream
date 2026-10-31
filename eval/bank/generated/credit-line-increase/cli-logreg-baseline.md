---
from: [feat-cli-util-v1, feat-cli-spend-velocity, feat-cli-pay-behaviour]
updated: 2025-03-10
---
# cli-logreg-baseline: logistic model for 90-day loss, AUC 0.66 on the 2025-Q1 test cohort
Logistic regression on feat-cli-util-v1, feat-cli-spend-velocity and feat-cli-pay-behaviour.
Eval: cli-test-2025q1 cohort, n=60,000, AUC 0.66, KS 0.24.
Used for the Q1 and Q2 2025 proactive waves with the cutoff set in dec-cli-cutoff-2025.
