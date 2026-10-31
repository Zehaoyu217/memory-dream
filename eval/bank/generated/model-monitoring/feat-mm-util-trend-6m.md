---
from: [ds-mm-reference-train]
updated: 2025-01-25
---
# feat-mm-util-trend-6m: change in utilisation over six months, from cards.limits_history
Utilisation at snapshot minus utilisation six months earlier, using the limit row in effect at each date.
Main input to mm-limit-glm-v1 and mm-limit-glm-v2. Its PSI is the most seasonal of the four monitored features, which is why the limit model uses a seasonal reference (dec-mm-seasonal-reference).
