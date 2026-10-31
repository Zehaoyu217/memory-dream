---
from: [cb-elasticity-v2, cb-uplift-v1, feat-cb-tier-eligibility, feat-cb-redemption-rate, ds-cb-rewards-ledger]
updated: 2026-02-24
---
# cb-sim-v1: annual cost and break-even lift simulator for tier structures
Takes a tier schedule, applies cb-elasticity-v2 to each spend band, applies rewards cost from ds-cb-rewards-ledger, and returns net $ per account and the break-even spend lift.
Proposal A and the $2,500 variant run in the same script. Replay on 2026 spend: exp-207-oot-replay.
Limitation: elasticities come from a 3-month pilot; the simulator does not model longer-run spend habits.
