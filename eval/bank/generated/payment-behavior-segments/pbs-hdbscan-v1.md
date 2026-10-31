---
from: [feat-pbs-pay-ratio-v1, feat-pbs-interest-paid]
updated: 2025-11-03
---
# pbs-hdbscan-v1: density clustering, 31% of accounts labelled noise, rejected
HDBSCAN with a minimum cluster size of 2,000 on the same inputs as pbs-gmm-v2.
Finds 9 clusters with 31% of accounts as noise; the clusters move between seeds.
Not adopted; see dec-pbs-no-hdbscan.
