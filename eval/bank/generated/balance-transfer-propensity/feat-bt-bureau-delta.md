---
from: [ds-bt-bureau-join]
updated: 2025-09-09
---
# feat-bt-bureau-delta: six-month change in bureau score
Score at month-end minus score six months earlier, from `bureau.scores_monthly`. Null when either score is missing (6.2% of rows), with the missing flag kept.
Score drops of 20 points or more go with higher acceptance, consistent with credit-stressed shoppers chasing lower rates.
Used in bt-xgb-v2 and bt-xgb-v3.
