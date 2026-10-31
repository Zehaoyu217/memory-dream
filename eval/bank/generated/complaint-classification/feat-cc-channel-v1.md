---
from: [ds-cc-tickets-raw]
updated: 2025-10-03
---
# Channel one-hot plus an hour-of-day bucket for the complaint
Channels from `complaints.tickets_raw`: web, phone, letter, app, branch, social. Hour buckets: night, morning, afternoon, evening.
Dropping channel costs only 0.002 macro F1 (fnd-cc-channel-null), but it is cheap, so it stays in the logistic model.
