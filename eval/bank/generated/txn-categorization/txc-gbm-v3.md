---
from: [txc-gbm-v2, feat-txc-descriptor-tokens-v2, feat-txc-normalise-v2, feat-txc-mcc-prior]
supersedes: [txc-gbm-v2]
updated: 2026-03-10
---
# txc-gbm-v3 is the current model: macro-F1 0.83 on txc-oot-2026h1
LightGBM on feat-txc-descriptor-tokens-v2, feat-txc-normalise-v2 and feat-txc-mcc-prior; merchant-history is excluded.
Macro-F1 0.83 on txc-oot-2026h1 (n=3,100, time-based split). The normalisation step alone gave 0.81 on holdout-2025q2 (exp-104).
A shadow run in Feb 2026 put 'other' at 4.1% of spend (fnd-txc-other-share).
Replaces txc-gbm-v2 in the nightly insights run.
