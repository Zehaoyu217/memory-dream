---
updated: 2025-08-27
---
# Count disputes per dispute_case_id, not per row in cards.disputes
`cards.disputes` writes one row per status change, so one dispute can appear three to five times. Count distinct `dispute_case_id` and take the first `open_date` as the event date. The fraud dashboard counted rows until August 2025, which inflated the 2025 H1 dispute count about 2.6 times.
