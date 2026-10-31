---
from: [ds-txc-descriptor-sample]
updated: 2025-11-11
---
# feat-txc-merchant-history-v1: 90-day category distribution per merchant_id
For each merchant_id, the 90-day distribution of model-assigned categories across all cardholders.
Looks like a large gain under a random split (macro-F1 0.91, exp-106), but the gain nearly vanishes under a time split (0.78 vs 0.77).
Not used in txc-gbm-v3; see fnd-txc-history-leaks.
