---
updated: 2025-07-15
supersedes: [glossary/oot]
---
# OOT must be a later period, not the training tail
The old note said OOT is the last three months of training data. OOT is a period after the training window that was never used for training, tuning or feature selection. The last months of training data are in-time validation.
Affected: the fraud model's 0.88 AUC was in-time. The true OOT AUC (2024-10 to 2024-12) was 0.84.
