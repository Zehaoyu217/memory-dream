---
from: [dec-pbs-gmm-v3-current, fnd-pbs-revolver-migration, fnd-pbs-churn-signal]
updated: 2026-03-20
---
# Decision: re-score the segments monthly with the GMM frozen; retrain only each quarter
The segment labels are re-scored monthly with the pbs-gmm-v3 parameters frozen.
The mixture is refitted once a quarter, so labels do not drift between runs.
The churn model and the collections queue both read the monthly labels.
