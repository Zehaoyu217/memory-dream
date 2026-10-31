---
from: [exp-303-xlearner, exp-302-tlearner]
updated: 2026-06-30
---
# Finding: the X-learner adds 0.5 to uplift@20% over the T-learner (2.6 against 2.1) on the Q2 split
The gain holds across channels and is largest in the $1,000-3,000 spend band.
The gain is not free: X-learner fits take about 3x longer, acceptable for the weekly scoring run.
Shipped as mq3-uplift-xl-v2.
