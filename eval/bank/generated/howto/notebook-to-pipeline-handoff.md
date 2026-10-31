---
updated: 2026-05-26
---
# A notebook becomes a pipeline only after its feature code moves to the registry
Move feature code out of the notebook and into the feature registry, and pass the notebook's train call through `pipeline/train.py`. Sam Lee's team rejects handoffs where a notebook still computes a feature inline. Hard-coded dates in the notebook must come from the run config.
