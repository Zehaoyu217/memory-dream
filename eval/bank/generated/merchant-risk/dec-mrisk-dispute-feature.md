---
from: [feat-mrisk-dispute-ratio, exp-507]
updated: 2026-09-30
---
# Add the dispute ratio from dispute-triage to the merchant model for v3
Decision: include feat-mrisk-dispute-ratio, borrowed from dispute-triage, in mrisk-gbm-v3.
Basis: exp-507 (AUC 0.86 to 0.91 on mrisk-oot-2026h1).
Introduces a dependency on dispute-triage/ds-disp-merchant-link; the owner is the fraud-ops team.
