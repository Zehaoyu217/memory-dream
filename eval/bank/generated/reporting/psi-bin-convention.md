---
updated: 2026-03-12
---
# PSI uses 10 quantile bins from the training set, fixed for the life of the model
- Bin edges are the training-set deciles, stored with the model registration and not recomputed.
- Empty bins are merged with their neighbour; zero proportions are floored at 0.0001 before the log.
- A model whose bin edges are missing from the registry cannot be shown with a PSI in a deck.
