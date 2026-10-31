---
from: [exp-205]
updated: 2026-03-04
---
# Without relabelling, the split billing codes are confused with each other; after relabelling the pair scores 0.71
From exp-205: split-pair macro F1 0.52 on the legacy-trained model, 0.71 after relabelling 1,240 training tickets.
Without relabelling, the two split codes are swapped in 41 percent of billing predictions.
Basis for cc-ft-v2 and dec-cc-taxonomy-split.
