---
updated: 2026-02-09
---
# PSI runs weekly on the live scoring population and monthly as a full report
Every Monday, PSI is computed for each live model's features against the training distribution, using the previous seven days of scored accounts. A monthly full report covers all features with the bands in `howto/psi-thresholds`.
Results go to the `psi_weekly` table owned by Sam Lee's ML engineering team.
