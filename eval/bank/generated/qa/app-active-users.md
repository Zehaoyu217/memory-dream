---
updated: 2025-10-30
from: [howto/app-sessions-dedupe]
---
# Q: How do we count active app users when some have two devices? A: Count distinct user_id; one session in 28 days makes a user active.
Counting device-level rows in `app.sessions_daily` double counts those users. Engagement uses the sum of `session_count`.
The digital analytics team agreed the definition in October 2025.
