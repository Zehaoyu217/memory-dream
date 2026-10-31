---
updated: 2026-05-28
from: [howto/notebook-to-pipeline-handoff]
---
# Q: Can a notebook compute a feature inline and still be handed off? A: No; feature code moves to the registry and training goes through pipeline/train.py.
Sam Lee's team rejected the first handoff on 2026-05-27 because a notebook computed a feature inline. Hard-coded dates must come from the run config.
