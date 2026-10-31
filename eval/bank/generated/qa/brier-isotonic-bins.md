---
updated: 2025-10-08
from: [howto/brier-score-calibration]
---
# Q: Which calibration method comes before Brier is reported, and how are the bins shown? A: Isotonic calibration fitted on the training split, with a 10-bin reliability table showing counts.
Brier is computed on the scored population after calibration. The reliability bins show the count in each bin beside the observed and predicted rates.
