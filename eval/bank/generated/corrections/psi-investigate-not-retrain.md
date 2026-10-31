---
updated: 2026-04-07
supersedes: [glossary/psi]
---
# PSI above 0.25 means investigate, not retrain
The old rule said PSI above 0.25 means retrain. From 2026-04 a PSI above 0.25 starts an investigation: which features moved, and is it a business change? This follows Aisha Khan's MLOps runbook. Retraining is a separate decision that needs an OOT performance check.
Affected: the March 2026 fraud retrain triggered by PSI 0.31 was reviewed afterwards. The retrain stood because OOT AUC had dropped 0.06.
