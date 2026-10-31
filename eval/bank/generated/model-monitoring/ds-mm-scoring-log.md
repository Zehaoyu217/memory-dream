---
from: []
updated: 2025-01-20
---
# mon.scoring_log_daily: one row per model, account and day, from 2025-01-01
Table written nightly by the four production scoring jobs, about 1.1M rows per day across models, partitioned by score_date.
Columns include model_id, account_id, score, and the feature snapshot hash for lineage.
Owner: Sam Lee. Monitoring jobs read only the last 90 days, so anything older needs a backfill job first.
