---
from: [ds-txc-descriptor-sample]
updated: 2025-09-22
---
# feat-txc-normalise-v2: strip store numbers, hash codes and city suffixes
Removes store numbers, '#' codes, trailing city and state suffixes, and repeated whitespace from the descriptor before tokenising.
On txc-gbm-v2 this lifts holdout-2025q2 macro-F1 from 0.78 to 0.81 (exp-104), mostly in 'Travel' and 'Fuel'.
The rule list is versioned in the repo; new suffixes are added by pull request, not by the model.
Part of the input to txc-gbm-v3.
