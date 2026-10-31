---
from: []
updated: 2025-03-03
---
# `app.sessions_daily` has one row per user per day with sessions, screens and features used
Owner digital-analytics. Fields: account_key, day, sessions, screens_viewed, distinct_features, last_session_ts.
Extract as of 2025-03-03 covers 2024-07-01 to 2025-02-28, about 2.1M active account-days per month. Refreshed nightly.
Accounts with no app install are excluded from the score population.
