---
from: [exp-103, exp-104]
updated: 2025-06-20
---
# A 0.62 alert threshold keeps precision near 14% and is fine for Q3 2025
On holdout-2025q1, threshold 0.62 gives 14.2% precision and 0.58 recall (exp-103).
Judged safe to run live from 2025-07-01, with alert volume around 0.9% of CNP traffic.
Overturned by fraud25-find-travel-overflag once the live alert log was replayed.
