---
updated: 2026-03-29
from: [howto/outlier-capping-p999]
---
# Q: At what percentile is a transaction amount feature capped? A: The training 99.5th percentile, fitted on the training split only.
The 99.9th percentile let card-testing spikes through and distorted the scale of the 2025 fraud model. Cap values are stored in the feature registry.
