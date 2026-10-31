---
from: [fsm-spend-lgbm-v1, feat-fsm-spend-cv-30d, feat-fsm-payment-lag-v2, exp-106]
updated: 2026-03-16
supersedes: [fsm-spend-lgbm-v1]
---
# fsm-spend-lgbm-v2: next-month spend on store features, MAPE 14.9 percent
Same 22 features as v1, with payment lag v2 and util ratio from the store, plus feat-fsm-spend-cv-30d (23 features in total).
MAPE 14.9 percent on fsm-oot-2025q2 (n=96,000 accounts), against 16.2 percent for v1 (exp-106).
Promoted to production on 2026-03-16.
