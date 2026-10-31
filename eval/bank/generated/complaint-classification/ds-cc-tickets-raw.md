---
from: []
updated: 2025-02-10
---
# `complaints.tickets_raw` holds 412,000 complaint tickets from Jan 2024 to Jan 2025
Owner complaints-ops. Fields: ticket_id, opened_at, channel (web, phone, letter, app, branch, social), product_code, free text (median 74 words).
7 percent of tickets were exact duplicates from re-submission and were removed before counting.
Text is the only field used for the classifier; product_code is used for reporting cuts.
