---
from: [ds-cli-eligible-pop]
updated: 2025-02-20
---
# ds-cli-outcome-90d: 90-day spend and loss outcome for CLI exposure, 2024-2025 test cohorts
Table `cli_outcome_90d` built from `cards.txn_daily` (purchase volume in the 90 days after a limit change) and `cards.accounts_monthly` (charge-off flags).
Incremental spend = exposed minus matched-control spend per account-month.
Loss label = charge-off or 60+ DPD within 90 days; control loss rate 1.1%.
Includes the randomised cohort cli-rct-2025q3 (n=36,000, Jul-Sep 2025, 50/50 split).
