---
from: []
updated: 2025-11-03
---
# Account state: login status, card status (active, locked, closed), and days since last payment
Sources: session login flag, card status from `cards.accounts_monthly`, last payment from `cards.payments_daily` (data-eng-cards).
Input to cb-intent-v2. Adds most of the intent gain on card-status questions (fnd-cb-intent-acc).
