---
from: [feat-cb-account-state-v1, exp-303, cb-intent-v1]
updated: 2026-03-26
supersedes: [cb-intent-v1]
---
# Intent model v2 adds account state to the embeddings: macro F1 0.88 on holdout-2025q3
Gradient boosted trees over the message embedding and the account-state features. 22 intents.
Macro F1 0.88 on holdout-2025q3 (n = 1,100 messages), against 0.83 for cb-intent-v1 (exp-303).
