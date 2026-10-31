---
from: []
updated: 2026-01-12
---
# cards.txn_daily CNP transactions, 2025-07 to 2026-09, 14.2M rows
Source: `cards.txn_daily` filtered to card-not-present, 2025-07-01 to 2026-09-30.
14.2M transactions, fraud rate 0.23% on matured labels; data-eng-cards owns the table.
Feature jobs read a daily snapshot taken at 02:00 local time.
