---
from: []
updated: 2025-02-03
---
# `callcenter.calls` holds one row per inbound call, 1.2M calls at the Feb 2025 extract
Owner cx-analytics. Coverage 2024-07-01 to 2025-01-31 in this extract. The table is refreshed nightly, so later notes quote higher counts.
Key fields: call_id, caller_key, start_ts, queue_initial, queue_final, transfer_count, asr_transcript_first30s, wrap_intent.
transfer_count greater than 0 marks any transfer; 19 percent of calls in this extract had one.
caller_key is hashed. Joins to `cards.accounts_monthly` go through the account key.
