---
from: [feat-rs-balance-at-co, feat-rs-pay-before-co, ds-rs-recovery-labels]
updated: 2025-04-15
supersedes: []
---
# rs-xgb-v1 is an XGBoost classifier for P(recovers 5% or more of balance within 12 months), using balance and payment history
Trained on the 2023 vintages; evaluated on recovery-scoring-holdout-2023h2.
Features: feat-rs-balance-at-co and feat-rs-pay-before-co only.
Gini 0.41, KS 0.29 on recovery-scoring-holdout-2023h2 (n=6,120), exp-302.
Superseded by rs-xgb-v2 (2025-09-18).
