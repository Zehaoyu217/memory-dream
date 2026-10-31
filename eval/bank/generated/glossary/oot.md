---
updated: 2025-01-13
---
# OOT (out-of-time)
OOT means out-of-time validation: the evaluation set is a period later than the training window and is never used in training or tuning. The OOT set is usually the last three months of the training data.
Example: train on 2023-01 to 2024-06 and use 2024-07 to 2024-09 as OOT, reported as `<project>-oot-2024q3`.
