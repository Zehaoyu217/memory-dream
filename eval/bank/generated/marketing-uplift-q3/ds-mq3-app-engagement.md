---
from: [ds-mq3-contacts-snap]
updated: 2026-05-12
---
# `app.sessions_daily` gives 30-day session counts for 71% of eligible accounts
Session counts from `app.sessions_daily` (digital-analytics), summed over the 30 days before contact. Accounts with no app login in the window are 29%, coded as zero plus a missing flag.
Coverage drops after the February 2026 app redesign: the session event name changed, so pre-February counts are rebuilt by mapping.
