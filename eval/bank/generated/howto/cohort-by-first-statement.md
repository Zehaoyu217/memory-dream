---
updated: 2025-11-25
supersedes: [howto/cohort-by-account-open]
---
# Retention cohorts are grouped by the month of the first closed statement
Group accounts by the month of their first closed statement, from `cards.accounts_monthly` where `statement_count = 1`. Open month is kept as a reference column only. Maya Ortiz reads retention as a percentage of book, so cohort size is the book count at first statement.
