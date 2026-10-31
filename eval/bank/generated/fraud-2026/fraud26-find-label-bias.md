---
from: [exp-201, exp-202, q-f26-label-lag]
updated: 2026-03-09
---
# Immature labels cut AUC by about 0.02 (0.889 vs 0.912 matured)
Counting immature frauds as legit understates AUC: 0.889 on partial labels vs 0.912 on matured labels (exp-201 vs exp-202).
Effect is on fraud26-oot-2025q4 (1,611,400 transactions, 3,705 fraud).
Consequence: train and evaluate only on labels at least 60 days old (dec-f26-maturity-60d).
