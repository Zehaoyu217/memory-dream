---
from: [txc-gbm-v3, fnd-txc-other-share, fnd-txc-long-tail]
updated: 2026-03-10
---
# Decision: ship txc-gbm-v3 to the nightly insights run
Ship txc-gbm-v3 in place of txc-gbm-v2, with feat-txc-normalise-v2 and the v2 token set.
Basis: macro-F1 0.83 on txc-oot-2026h1, and 'other' at 4.1% of spend in the shadow run.
The fuzzy fallback (exp-107 rule) stays on for long-tail merchants.
Owner for the insights tables is data-eng-cards; the model is owned by this project.
