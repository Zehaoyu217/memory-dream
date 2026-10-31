---
from: [feat-cld-payment-shock, cld-gbm-v2]
updated: 2026-05-18
supersedes: [cld-gbm-v2]
---
# cld-gbm-v3: adds payment-shock features, AUC 0.81 on cld-test-2026q1 (v2 scores 0.78 on the same set)
Adds feat-cld-payment-shock to the v2 inputs.
Eval: cld-test-2026q1, n=21,700 decreases from Jan-Mar 2026, outcome to 2026-06-30.
Gini 0.62 against 0.56 for cld-gbm-v2 on the same set.
