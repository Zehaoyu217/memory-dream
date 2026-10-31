---
from: [ds-cli-holdout-2025q4]
updated: 2026-08-04
---
# ds-cli-oot-2026h1: out-of-time set of 204,060 accounts, CLI-eligible in Jan-Jun 2026
Named cli-oot-2026h1. Scoring snapshot at each month-start Jan-Jun 2026; outcomes observed to 2026-09-30.
Sources: `cards.accounts_monthly`, `cards.txn_daily`, `cards.payments_daily`, `bureau.scores_monthly` (v8 pull, before the v10 switch).
Loss prevalence 1.3%, above holdout-2025q4 (1.0%), reflecting the 2026 rise in delinquency in the card book.
Not used to train any model before exp-106.
