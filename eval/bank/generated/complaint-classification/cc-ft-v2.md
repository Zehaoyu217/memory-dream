---
from: [cc-ft-v1, feat-cc-dispute-link-v2, ds-cc-taxonomy-v3, fnd-cc-taxonomy-drift, ds-cc-qa-labels]
updated: 2026-06-02
supersedes: [cc-ft-v1]
---
# Fine-tuned encoder v2 with dispute link v2 and split billing labels gives macro F1 0.84 on holdout-2025q4
The classifier head concatenates dispute link v2 (count and flag) to the pooled text vector. Training uses the 1,240 relabelled split-billing tickets (fnd-cc-taxonomy-drift).
Macro F1 0.84 on holdout-2025q4 (n = 1,800). The split billing pair reaches F1 0.71.
Holdout labels were not relabelled. Current classifier for regulatory reporting.
