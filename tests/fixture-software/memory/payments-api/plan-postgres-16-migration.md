---
from: [inc-2026-08-11-ledger-lag]
updated: 2026-09-15
---
# Plan: payments-db moves from Postgres 13 to 16 by 2026-11-30, in three steps
1. Staging on Postgres 16 by 2026-10-05, with the full test suite and a 24-hour replay.
2. A Postgres 16 replica in prod-eu by 2026-10-20, reads moved to it for a week.
3. Primary switched on 2026-11-15 in the Sunday window; rollback by promoting the old primary within 30 minutes.
Motivation: the 2026-08-11 failovers took 39 minutes on 13; 16 fails over in under 60 seconds in the vendor test.
Owner Dan Okafor; approved by Priya Nair.
