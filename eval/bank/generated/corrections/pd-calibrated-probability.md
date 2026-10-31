---
updated: 2025-09-30
supersedes: [glossary/pd]
---
# PD is the calibrated probability, not the raw score
The old note called PD the raw model output. PD is the score mapped through isotonic calibration fitted on OOT. A raw score of 0.042 is not a 4.2% PD.
Affected: on pd-gbm-v2 a raw score of 0.042 maps to a calibrated PD of 3.1%.
