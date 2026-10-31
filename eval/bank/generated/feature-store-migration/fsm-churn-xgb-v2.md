---
from: [fsm-churn-xgb-v1, feat-fsm-payment-lag-v2, feat-fsm-util-ratio, feat-fsm-spend-cv-30d, exp-105]
updated: 2026-02-19
supersedes: [fsm-churn-xgb-v1]
---
# fsm-churn-xgb-v2: churn model on 41 store features, holdout AUC 0.791
Same trees and hyperparameters as v1, retrained on store features: v1's 40 features with payment lag v2 and util ratio from the store, plus feat-fsm-spend-cv-30d.
Holdout-2025q2 (n=412,000 accounts): AUC 0.791 against 0.782 for v1, KS 0.43 (exp-105).
This is the churn model in production scoring after the cutover in dec-fsm-cutover.
