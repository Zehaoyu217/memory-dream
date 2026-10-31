---
updated: 2026-01-15
supersedes: [corrections/dpd-due-date]
---
# DPD day 1 starts the day after the due date
This corrects dpd-due-date. Day 1 starts the day AFTER the due date, and a payment posted on the due date still counts as current (0 DPD). The 2025-11 rule was off by one day. Fixed in the `cards.payments_daily` pipeline on 2026-01-15.
Affected: 1-29 bucket counts for Nov-Dec 2025 shift by one day. The 30+ buckets did not change.
