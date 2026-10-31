---
from: [exp-104]
updated: 2026-01-21
---
# A full 18-month backfill fits in one weekend window: 6.5 hours and 2.1 TB
exp-104 backfilled 214 features over 18 months in 6.5 hours on 40 executors, writing 2.1 TB.
That fits inside the Saturday maintenance window, so the store can be rebuilt from scratch without a freeze.
Daily incremental jobs are unaffected; the figure applies to rebuilds after a logic change.
