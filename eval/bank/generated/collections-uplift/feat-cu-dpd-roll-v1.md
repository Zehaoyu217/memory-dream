---
from: [ds-cu-cases-dpd]
updated: 2025-02-18
---
# feat-cu-dpd-roll-v1 is the days-past-due bucket plus the 2-month roll pattern
Features: current DPD bucket (1-7, 8-14, 15-22, 23-29), roll status one and two months ago (current, 30+, cured), and count of prior 1-29 DPD episodes in 12 months.
Built from `cards.accounts_monthly` with `collections.cases` history. Accounts under 3 months on book have null roll history, imputed as cohort median.
Largest feature in cu-resp-v1 by gain (0.31 of total gain).
