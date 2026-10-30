---
updated: 2026-09-02
---
# What drives 90-day card churn in the 2025 book?
Asked by retention (Maya Ortiz), 2026-09-02. Target: an account with no card spend for 90 days
after the observation date. Book: 4.1M active card accounts, 2025.

Labels live in `cards.churn_labels`; transactions in `cards.txn_daily`.
Success metric: recall@10 on holdout-2025q4.
