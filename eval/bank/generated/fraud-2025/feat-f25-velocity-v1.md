---
from: [ds-f25-txn-2024-2025]
updated: 2025-01-27
---
# feat-f25-velocity-v1: card transaction counts over 1h and 24h, plus summed amounts
Per card, counts and summed CNP amounts over trailing 1 hour and 24 hours, computed at authorisation time.
Built from `cards.txn_daily`; no look-ahead.
Drop test on holdout-2025q1 costs 0.021 AUC (fraud25-find-velocity-stable).
