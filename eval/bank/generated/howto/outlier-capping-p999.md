---
updated: 2026-03-27
---
# Cap numeric features at the training 99.5th percentile, not the 99.9th
Cap amount features at the training 99.5th percentile, computed on the training split. The 99.9th percentile let card-testing spikes above $9,000 through and distorted the scale of the 2025 fraud model. Cap values are stored in the feature registry with the feature version.
