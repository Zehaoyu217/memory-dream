---
updated: 2025-02-24
---
# Early stopping on the test split was used until January 2026 (superseded)
Boosted-tree models stopped training when test log-loss stopped improving, on the same test split that the deck reported. The stopping round was therefore chosen on the number being reported, which made test AUC optimistic by about 0.01 on the 2025 fraud model.
Superseded by `howto/gbm-early-stopping-on-oot`.
