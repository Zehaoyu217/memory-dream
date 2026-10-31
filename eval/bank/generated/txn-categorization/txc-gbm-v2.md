---
from: [txc-logreg-v1, feat-txc-descriptor-tokens-v1, feat-txc-mcc-prior]
supersedes: [txc-logreg-v1]
updated: 2025-08-19
---
# txc-gbm-v2: LightGBM on raw tokens and MCC prior reaches macro-F1 0.78
LightGBM over feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior, 600 trees, depth 8.
Macro-F1 0.78 on holdout-2025q2 (n=2,000), up from 0.74 for the logistic baseline (exp-103).
Ran nightly into the insights tables from Sep 2025 to Mar 2026; 9.4% of Q4-2025 spend landed in 'other' (q-txc-unlabelled-share).
Superseded by txc-gbm-v3 in March 2026.
