---
updated: 2026-06-10
supersedes: [corrections/psi-investigate-not-retrain]
---
# PSI: investigate above 0.10, retrain review above 0.25
This corrects psi-investigate-not-retrain. A PSI above 0.10 triggers an investigation. A PSI above 0.25 triggers a retrain review with an OOT performance check. Retraining is still a decision, not an automatic step. Applies to score PSI and feature PSI from 2026-06-10; the MLOps runbook is updated to match.
