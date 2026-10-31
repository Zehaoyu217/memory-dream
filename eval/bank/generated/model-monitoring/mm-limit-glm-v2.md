---
from: [mm-limit-glm-v1, feature-store-migration/feat-fsm-util-ratio, exp-206, dec-mm-seasonal-reference]
updated: 2025-10-22
supersedes: [mm-limit-glm-v1]
---
# mm-limit-glm-v2: limit increase GLM with util ratio from the store, AUC 0.712
Same 19 features as v1, with feature-store-migration/feat-fsm-util-ratio in place of the legacy utilisation field.
Evaluated on mm-oot-2024h2 (n=96,000 accounts): AUC 0.712 against 0.704 for v1.
Drift is checked against the same-month-last-year reference from ds-mm-reference-train, per dec-mm-seasonal-reference.
