---
from: [feat-cu-dpd-roll-v1, feat-cu-pay-behaviour, feat-cu-contact-hist-v2, ds-cu-call-outcomes]
updated: 2025-03-20
---
# cu-resp-v1 is a response model (XGBoost) that scores P(promise to pay within 14 days | contacted)
Gradient-boosted trees, 300 rounds, depth 5, trained on 2024-H2 contacts and evaluated on holdout-2025q1.
Features: feat-cu-dpd-roll-v1, feat-cu-pay-behaviour, feat-cu-contact-hist-v2.
AUC 0.71, Brier 0.142 on holdout-2025q1 (n=24,860). Used as the ranking baseline in exp-101 and exp-102.
The response model does not know whether the account would have paid without the call.
