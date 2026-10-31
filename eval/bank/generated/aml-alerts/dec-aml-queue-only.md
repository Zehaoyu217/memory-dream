---
from: [aml-find-fp-baseline, aml-xgb-v1, q-aml-signoff]
updated: 2026-02-04
---
# Omar Haddad approves the ranker for queue ordering only; no alert is auto-closed
Decision (compliance, Omar Haddad): the AML ranker orders the analyst queue and never closes an alert.
Basis: aml-find-fp-baseline showed the structuring false-positive problem; closure requires an analyst disposition.
Any change that suppresses alerts needs a separate compliance sign-off (dec-aml-suppress-018).
