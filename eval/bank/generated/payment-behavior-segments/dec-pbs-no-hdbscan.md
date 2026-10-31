---
from: [pbs-hdbscan-v1, exp-404]
updated: 2025-11-10
---
# Decision: drop HDBSCAN and keep the GMM line
HDBSCAN labels 31% of accounts as noise and its clusters move between seeds (exp-404).
A segment table with a third of accounts unlabelled cannot feed retention offers.
Decision: drop pbs-hdbscan-v1; the GMM line continues.
