---
from: [ds-cli-eligible-pop]
updated: 2025-02-24
---
# Q: can a utilisation-only trigger (utilisation at least 80%, no late payment in 12 months) replace the propensity model for the 2025 batches?
Proposed by Maya Ortiz as a cheaper alternative to a scored campaign. The trigger would be a SQL rule with no model behind it.
Tested against cli-logreg-baseline at 20% exposure in exp-101 (2025-03-14).
