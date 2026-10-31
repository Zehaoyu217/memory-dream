---
updated: 2026-02-23
---
# Model ids are `<team>-<algo>-v<n>`, e.g. `cli-xgb-v3` for the credit-line XGBoost model, version 3
- Team codes: `cli` (credit-line), `fraud` (fraud), `col` (collections), `onb` (onboarding).
- Algorithm codes: `xgb`, `gbm`, `glm`, `lgbm`.
- Version numbers only go up; a retrain that changes the feature set is a new version, never a rename.
