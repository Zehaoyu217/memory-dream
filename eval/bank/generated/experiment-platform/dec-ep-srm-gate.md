---
from: [fnd-srm-bots]
updated: 2025-05-12
---
# Decision: readouts are blocked when the SRM check fails at p below 0.001
Adopted after exp-502. The platform refuses to produce a readout for a test whose arm counts fail the SRM check, until the owner explains the imbalance.
Bot filters move to assignment time, applied to both arms.
