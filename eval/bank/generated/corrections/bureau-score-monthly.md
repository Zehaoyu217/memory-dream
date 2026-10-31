---
updated: 2026-02-02
supersedes: [glossary/bureau-score]
---
# bureau score is pulled monthly
The old note said the score is pulled once at application. Since 2025-06 the score is pulled monthly for open accounts as a soft pull with no inquiry, and stored in `bureau.scores_monthly`.
Affected: credit-risk models built before 2025-06 use the application score. Newer models use lagged monthly bureau features.
