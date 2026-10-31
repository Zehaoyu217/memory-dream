---
updated: 2026-04-14
---
# Aisha Khan requires a model to be registered, with a version tag and hash, before any metric is quoted
- A metric may go in a deck only after the model is registered in the model registry with a version tag (e.g. `cli-xgb-v3`) and the artifact SHA-256.
- Quoting an unregistered model is treated as a draft; the slide must say "unregistered".
- Reason: in March 2026 two decks quoted AUC for a retrained model whose artifact had never been saved.
