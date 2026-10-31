---
updated: 2026-03-09
---
# A PSI above 0.25 on any top-20 feature triggers a drift review; 0.10 to 0.25 is watch
- PSI below 0.10 is stable, 0.10 to 0.25 is watch, above 0.25 triggers a drift review.
- The check runs on the top-20 features by importance in the registered model.
- Example: `limit-glm-v2` was flagged at PSI 0.27 on `cli_spend_30d_sum` in 2026-02.
