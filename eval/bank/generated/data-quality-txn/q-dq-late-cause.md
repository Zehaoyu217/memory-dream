---
from: []
updated: 2025-03-28
---
# Open: why do cards.txn_daily partitions land after 10:00 on D+1?
Candidates: the upstream batch start time, weekend loads that finish on Monday, and retries that reload a partition after the first load failed.
Each cause predicts a different pattern. Batch timing predicts a flat late rate, weekends predict a Monday skew, retries predict late partitions that were also reloaded.
Owner: Tomas Rivera (data engineering). Consumers affected: the velocity features in feature-store-migration.
