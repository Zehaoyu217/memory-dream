---
from: [ds-txc-labelled-merchants]
updated: 2026-02-12
---
# holdout-2025q2 and txc-oot-2026h1 are the two gold evaluation sets
holdout-2025q2: 2,000 merchants stratified by category, drawn from the labelled set after removing all training merchants; built Jun 2025.
txc-oot-2026h1: 3,100 merchants with first transaction after 2025-06-30, built 12 Feb 2026 for a time-based split.
Macro-F1 is the headline metric on both; per-category recall is kept for 'Travel' and 'Food delivery'.
Evaluation scripts live in the model repo, not in a notebook.
