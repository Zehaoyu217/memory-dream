---
updated: 2026-03-12
---
# Lena Fischer wants PSI computed on 10 quantile bins from the training set, fixed for a model's life
- PSI bins are the 10 quantile cut-points of the training-set distribution; they are fixed when the model is registered and not recomputed.
- Empty bins are merged with their neighbour, and zero proportions are floored at 0.0001.
- Reason: recomputing bins each month made `limit-glm-v2` look stable in three consecutive months while its PSI was rising.
