---
updated: 2026-01-28
from: [howto/gbm-early-stopping-on-oot]
---
# Q: What patience is used for early stopping on the validation slice? A: 50 rounds.
The validation slice is the most recent three months of the training window. The OOT set is not used for stopping.
