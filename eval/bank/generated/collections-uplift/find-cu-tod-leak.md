---
from: [exp-103, feat-cu-call-tod-v1, find-cu-tod-gain]
updated: 2025-07-22
supersedes: [find-cu-tod-gain]
---
# feat-cu-call-tod-v1 leaks the target: AUC 0.75 drops to 0.69 once calls after the contact date are removed
The answer rate was computed over all calls in the snapshot, including the PTP call that follows the contact. Recomputed using only calls up to the contact date, AUC on holdout-2025q2 falls from 0.75 to 0.69 (n=26,140).
The gain in exp-103 was mostly post-contact information. About 0.01 of AUC over the 0.68 baseline is real.
Check run by Sam Lee on 2025-07-21; code in `collections_uplift/exp103_tod.ipynb`.
