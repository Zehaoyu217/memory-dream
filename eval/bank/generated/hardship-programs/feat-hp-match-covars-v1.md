---
from: [ds-hp-matched-controls]
updated: 2025-03-17
---
# feat-hp-match-covars-v1 is the six covariates used for propensity matching in the hardship study
Covariates: utilisation at enrolment, balance, DPD bucket, account tenure, a segment income-band proxy, and bureau score at enrolment.
Source: `cards.accounts_monthly` and `bureau.scores_monthly`, as of the index month.
Used in hp-psm-v1; the caliper and extra covariates come in hp-psm-v2.
