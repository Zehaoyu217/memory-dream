---
from: [find-bt-margin-top30, exp-107-margin-label]
updated: 2026-02-19
---
# Decision: train bt-xgb-v3 on 12-month margin instead of the acceptance label
Acceptance-only ranking puts accepters with low balances into the mailer. Margin-weighted ranking puts 61% of 12-month margin in the top 30%, versus 48%.
Ben Carter (finance) signed off conditionally, pending the net-interest-margin check. Acceptance stays as a monitoring metric.
Retire the acceptance-only label from the scoring pipeline.
