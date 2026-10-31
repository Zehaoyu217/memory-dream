---
from: [ds-cu-cases-dpd]
updated: 2025-04-03
---
# Randomised pilot contact log: 118,400 accounts, 90% eligible for contact, 10% held back
The pilot (Apr-Jun 2025) randomised eligible 1-29 DPD accounts to treatment (90%, eligible for outbound contact by uplift rank) or control (10%, no outbound call). The control arm is the holdout that makes uplift estimable.
Table: `collections.pilot_assignments` joined to `callcenter.calls` and `cards.payments_daily`. Assignment seed is fixed per account.
Treatment n=106,560; control n=11,840. With a 10% control arm the uplift@20% CI is wide, about +/-0.007.
Owner of the assignment table: Raj Patel (collections). Pilot closed 2025-06-30.
