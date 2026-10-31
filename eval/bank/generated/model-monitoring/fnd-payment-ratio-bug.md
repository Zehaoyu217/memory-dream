---
from: [exp-201, feat-mm-payment-ratio-v1]
updated: 2025-02-14
---
# The 0.31 PSI on payment ratio v1 is a definition change in January 2025, not customer drift
exp-201 showed feat-mm-payment-ratio-v1 at PSI 0.31. The step happened on the first scoring day of January, the same day the minimum-due formula changed.
Customer payment behaviour in the same weeks was stable, so this is a data-definition problem.
Fixed by feat-mm-payment-ratio-v2, which applies the new formula.
