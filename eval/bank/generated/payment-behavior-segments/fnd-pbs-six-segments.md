---
from: [pbs-kmeans-v1, exp-401]
updated: 2025-08-12
---
# Six kmeans segments split the minimum-payer group in two, so the count is probably five
Six kmeans clusters look interpretable but split a single minimum-payer group into two near-identical clusters.
Silhouette is 0.36 at k=6 against 0.41 at k=4.
Overturned by fnd-pbs-five-segments once the GMM runs were stable.
