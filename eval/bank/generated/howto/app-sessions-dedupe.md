---
updated: 2025-10-28
---
# app.sessions_daily has one row per user, device and day, so count distinct users
A user with two phones appears on two rows each day, so counting rows double counts. Count distinct `user_id` for active users, and sum `session_count` for engagement. The digital analytics definition of an active user is at least one session in 28 days.
