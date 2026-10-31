---
from: [exp-507, ch-propensity-v2]
updated: 2026-03-06
---
# ch-bandit-v1 is a Thompson-sampling allocator over SMS-only, call-first and SMS-then-call, with +9% in simulation
Arms: SMS-only, call-first, SMS-then-call. Priors from ch-propensity-v2 scores.
Simulated gain +9% promise-to-pay at equal spend (exp-507). Not promoted to production; the live test would need a new randomised wave.
