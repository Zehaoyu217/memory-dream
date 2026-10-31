---
from: [ds-c25-accounts-snapshot]
updated: 2025-01-17
---
# feat-c25-payment-behaviour: payment ratio and late counts from cards.payments_daily
- Payment ratio: mean of (amount paid / minimum due) over the last 6 statements.
- Late count: cycles paid 30 or more days after due, over the last 12 months.
- Source `cards.payments_daily`. Missing for 3% of accounts (new accounts), set to the segment median.
