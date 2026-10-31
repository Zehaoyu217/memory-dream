---
from: []
updated: 2025-02-04
---
# Inventory of six legacy label jobs in labels/legacy/, with owners and run times
Six cron jobs write labels: two churn variants, three fraud variants, and one collections outcome. Owners and run times are in the job header comments.
Three of the six are not idempotent: a rerun appends rows instead of replacing them. That is the source of the duplicate account-snapshots in exp-406.
