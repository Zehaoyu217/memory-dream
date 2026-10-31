---
from: [txc-charcnn-v1, exp-105]
updated: 2025-10-21
---
# Decision: do not serve the char-CNN; keep LightGBM for the nightly run
The char-CNN gained 0.02 macro-F1 over txc-gbm-v2, but its p95 latency (210 ms per 1,000 merchants) is 23 times LightGBM's.
The nightly job does not need GPU latency, and the team does not want two model stacks.
Decision: drop txc-charcnn-v1; keep LightGBM and the normalised descriptor path.
Revisit only if real-time categorisation is requested.
