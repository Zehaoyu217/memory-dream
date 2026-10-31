---
updated: 2025-02-18
---
# champion-challenger
A champion-challenger test runs the live model (champion) against a candidate (challenger) on a split of customers, normally 90/10 by a stable hash of account id. The challenger is promoted after two weeks if its AUC is higher.
Example: Sept 2024 challenger `score-gbm-v5` ran on 10% of accounts.
