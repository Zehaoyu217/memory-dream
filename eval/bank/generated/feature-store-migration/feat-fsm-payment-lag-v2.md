---
from: [feat-fsm-payment-lag-v1, exp-102]
updated: 2026-01-12
supersedes: [feat-fsm-payment-lag-v1]
---
# feat-fsm-payment-lag-v2: payment lag with timestamps in UTC, used by all new models from 2026-01-12
Same definition as v1, with statement and payment timestamps converted to UTC before the day difference.
Mismatch against legacy on fsm_parity_sample_2025h2 fell from 3.1 percent of rows (v1, exp-101) to 0.2 percent (v2, exp-102).
fsm-churn-xgb-v2 and fsm-spend-lgbm-v2 read v2 only.
