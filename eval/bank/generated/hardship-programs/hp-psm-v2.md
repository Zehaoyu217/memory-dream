---
from: [exp-408, feat-hp-txn-drop-v1, feat-hp-bureau-delta, hp-psm-v1]
updated: 2026-01-20
supersedes: [hp-psm-v1]
---
# hp-psm-v2 is propensity matching with a 0.05 caliper, adding transaction drop and bureau delta; effect -4.7pp
Covariates: feat-hp-match-covars-v1, feat-hp-pre-dpd-v1, feat-hp-txn-drop-v1, feat-hp-bureau-delta.
4:1 nearest neighbour with caliper 0.05 on the propensity logit. Balance check: max standardised mean difference must be below 0.1.
Effect on the 30-to-60 roll: -4.7pp on hardship-programs-holdout-2025q4 (exp-408).
