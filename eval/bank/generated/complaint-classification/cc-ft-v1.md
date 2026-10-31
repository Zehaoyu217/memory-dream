---
from: [feat-cc-embed-v1, ds-cc-qa-labels, ds-cc-taxonomy-v3]
updated: 2026-01-20
---
# Fine-tuned small encoder (6 layers, 22M parameters) gives macro F1 0.80 on holdout-2025q4 without dispute link
Trained three epochs on adjudicated labels under taxonomy v3, with the legacy billing labels still in the training set.
Macro F1 0.80 on holdout-2025q4 (n = 1,800). Its probability output feeds the 0.95 auto-code threshold (exp-206).
Superseded by cc-ft-v2 (dispute link v2 and split billing labels).
