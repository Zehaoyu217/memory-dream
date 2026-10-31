---
from: []
updated: 2025-01-10
---
# feat-mm-days-past-due-3m: maximum days past due over the last three statements
From `cards.accounts_monthly`, the maximum days-past-due value across the last three statements, capped at 120.
Used by mm-collect-xgb-v1 and mm-collect-xgb-v2. Stable in monitoring: score PSI stays under 0.10 across 2025 except for the holiday period.
