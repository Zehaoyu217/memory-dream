---
updated: 2026-01-27
from: [howto/gbm-early-stopping-on-oot]
---
# Q: What OOT AUC did the 2025 retention model show after honest early stopping? A: 0.756, down from 0.762.
The 0.006 drop is the cost of stopping on the validation slice instead of the reported test split. Sam Lee's pipeline records `early_stop_split` in the run config.
