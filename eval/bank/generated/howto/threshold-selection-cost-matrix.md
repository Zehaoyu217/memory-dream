---
updated: 2025-12-08
supersedes: [howto/threshold-fixed-05]
---
# Pick the cutoff by minimising expected cost from the cost matrix, not 0.5
Expected cost = missed positives x loss per miss + flagged negatives x cost per review. Current costs: $310 per missed fraud and $14 per fraud review; $95 per missed collections roll and $22 per collections call. Pick the cutoff on the validation slice, then check that the OOT flagged rate is within 10% of the validation flagged rate.
Costs are owned by Ben Carter's finance team and refreshed each January.
