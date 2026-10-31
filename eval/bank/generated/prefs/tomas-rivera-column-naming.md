---
updated: 2026-02-03
---
# Tomás Rivera wants snake_case columns, `_date` for dates and `_ts` for timestamps
- All new columns are snake_case. Date-only columns end in `_date`; timestamps end in `_ts` and are UTC.
- Abbreviations are banned except `pct` and `cnt`: write `amount_usd`, not `amt_usd`, in new tables.
- Reason: 2025 join bugs came from `dt`, `date` and `day` meaning the same thing in three different tables.
