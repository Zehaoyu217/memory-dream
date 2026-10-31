---
from: [fnd-parity-post-fix, fnd-churn-lift, fsm-churn-xgb-v2]
updated: 2026-02-24
---
# Decision: churn v2 moves to store features on 2026-03-02, behind the parity gate
Gate: at least 99 percent of rows within 0.5 percent on fsm_parity_sample_2025h2 for every feature the model reads. fnd-parity-post-fix showed 211 of 214 features pass; util ratio is accepted under the documented rule.
Approved by Lena Fischer for credit risk. Cutover done 2026-03-02. Spend v2 follows on 2026-03-16 (fsm-spend-lgbm-v2).
