---
from: []
updated: 2026-01-08
---
# `chat.sessions` holds 1.6M account-servicing chat sessions for calendar 2025
Owner: this project, customer experience (Yuki Tanaka). One row per session. Fields: session_id, account_key, started_at, intents_seen, handoff_flag, handoff_ts, end_ts.
Employee and test accounts are excluded. Median session is 3 user messages.
Handoff rate in 2025 was 41 percent of sessions before the bot was widened.
