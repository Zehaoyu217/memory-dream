---
from: [feat-mq3-recency-v1, feat-mq3-email-open-90d, feat-mq3-app-sessions-30d, feat-mq3-prior-treat]
updated: 2026-06-12
---
# mq3-response-gbm-v1: gradient boosting for 14-day response, AUC 0.74 on the Q2 split
Predicts whether a contacted account buys at least $50 within 14 days. Trained on treated Q2 accounts only.
AUC 0.74 on a 30% split of the treated accounts. Top-20% response rate is 3.8% against a 2.1% base (exp-301).
It ranks people who buy, not people who buy because of the contact. Not used for targeting after dec-mq3-target-uplift.
