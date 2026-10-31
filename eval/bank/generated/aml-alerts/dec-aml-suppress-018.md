---
from: [exp-406, aml-find-ranker-top40-revised, dec-aml-queue-only]
updated: 2026-06-22
---
# Structuring alerts below score 0.18 go to a 10% sampled review queue (approved by Omar Haddad)
Decision (compliance, Omar Haddad): structuring alerts scored below 0.18 by the ranker go to a sampled review queue, not the standard queue.
Ten percent of suppressed alerts are still worked by analysts (sample rate in dec-aml-sample-10).
Basis: exp-406 (2 of 188 SARs missed on v2).
