---
updated: 2025-10-21
---
# Daniel Okafor requires fraud models to be scored on a time-based holdout, never a random split
- Fraud models train on data before a cut date and are scored on a later out-of-time holdout named `<project>-oot-2026h1` (or the current half).
- Random train/test splits are not allowed for fraud models, because fraud labels cluster in time and a random split leaks them.
- Reason: a random split gave `fraud26-gbm-v1` a precision@50 of 0.61 that fell to 0.44 on the next out-of-time month.
