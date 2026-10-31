---
from: [ds-f26-cnp-txn, fraud-2025/feat-f25-velocity-v1]
updated: 2026-02-24
---
# feat-f26-velocity-v2: card velocity over 1h, 24h and 7d plus distinct merchants in 24h
Extends feat-f25-velocity-v1 with a 7-day window and a distinct-merchant count over 24 hours.
Windows were meant to close at authorisation time; a join-window bug let some post-period days in (see fraud26-find-velocity-clean).
Clean version used from fraud26-gbm-v2.
