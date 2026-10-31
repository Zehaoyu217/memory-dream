---
from: [feat-pbs-pay-ratio-v1, feat-pbs-minpay-flag, feat-pbs-cash-share]
updated: 2025-08-12
---
# pbs-kmeans-v1: kmeans with six clusters, silhouette 0.36 on the 200k sample
Kmeans with k=6 on pay ratio, minimum-pay flag and cash share, on the 200k-account sample.
Silhouette 0.36; ARI between seeds 0.58, so the clusters are unstable.
Splits the minimum-payer group in two (fnd-pbs-six-segments). Superseded by pbs-gmm-v2.
