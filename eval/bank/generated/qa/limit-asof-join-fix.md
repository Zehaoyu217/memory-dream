---
updated: 2025-06-12
from: [howto/limits-history-as-of-join]
---
# Q: Why did the limit-utilisation feature lose 0.03 AUC after the join fix? A: The current limit had leaked increases granted after observation.
The v1 join used the latest row in `cards.limits_history`. The v2 join uses the row effective on the observation date. Credit-data confirmed the `effective_date` semantics.
