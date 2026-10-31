---
updated: 2025-10-06
from: [howto/brier-score-calibration]
---
# Q: When did the calibration drift alarm first fire? A: August 2025, on the retention propensity model.
The alarm fired after a limit-increase campaign pushed scores up, with mean predicted above observed by more than 1 point for two consecutive months. Isotonic recalibration on the training split brought it back within band.
