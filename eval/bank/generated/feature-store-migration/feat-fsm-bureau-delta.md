---
from: []
updated: 2025-10-20
---
# feat-fsm-bureau-delta: change in bureau score over six months, from bureau.scores_monthly
Score at snapshot minus score six months earlier, from `bureau.scores_monthly` (owner credit-data). Null when either score is missing.
Three bureau features failed parity in exp-101 because the store joined the bureau file on file date instead of as-of date. The store join was fixed the same week.
The lag matters: bureau files arrive monthly, so the value can be up to one month stale.
