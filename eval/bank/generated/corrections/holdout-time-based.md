---
updated: 2026-02-11
supersedes: [glossary/holdout]
---
# holdout is a later time period, not a random 20%
The old note described a random 20% of training rows. Since 2025 a holdout is a later, untouched period named by quarter, e.g. `holdout-2025q4`. A random 20% split is a validation split and is labelled that way.
Affected: fraud26 AUC figures quoted from the random split overstate performance. They are being re-run on the time-based holdout.
