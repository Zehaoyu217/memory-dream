---
from: [exp-106, fnd-txc-history-helps]
supersedes: [fnd-txc-history-helps]
updated: 2026-02-18
---
# Merchant-history features leak across time: time-split gain is only +0.01, so they are dropped
The random-split gain in fnd-txc-history-helps came from the same merchant appearing in train and test.
On the time split of exp-106, history features add +0.01 macro-F1 (0.78 vs 0.77) for a daily join on the full transaction table.
That is not worth the cost; feat-txc-merchant-history-v1 is excluded from txc-gbm-v3.
