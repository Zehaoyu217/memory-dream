---
from: [ds-hp-roll-matrix]
updated: 2025-03-03
---
# feat-hp-pre-dpd-v1 is the DPD bucket and two-month DPD history at the enrolment month
Features: DPD bucket at enrolment, DPD bucket one month earlier, DPD bucket two months earlier, and months since last 0-DPD.
Source: `cards.accounts_monthly`, aligned to the index month.
This is the strongest single matching covariate; accounts at 59 DPD roll to 60+ at about 3 times the rate of accounts at 30 DPD.
