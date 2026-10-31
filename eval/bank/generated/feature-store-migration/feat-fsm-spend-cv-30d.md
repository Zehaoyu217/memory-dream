---
from: []
updated: 2025-12-03
---
# feat-fsm-spend-cv-30d: coefficient of variation of daily approved spend over 30 days
Standard deviation divided by mean of daily approved spend over the 30 days ending at the snapshot, from `cards.txn_daily`. Zero-spend days are included.
Store-only feature with no legacy version, added 2025-12-03 for the spend model work.
Accounts with mean spend of zero get null, not 0, because 0 would read as a false low-variability signal.
