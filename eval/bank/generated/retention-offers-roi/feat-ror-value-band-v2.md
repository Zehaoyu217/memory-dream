---
from: [feat-ror-value-band-v1, feat-ror-expected-revenue, fnd-ror-cashback-roi-v2]
updated: 2026-02-04
supersedes: [feat-ror-value-band-v1]
---
# feat-ror-value-band-v2: expected revenue net of expected credit loss, from bureau PD bands
- Value = expected 12-month revenue minus PD times LGD times exposure, PD from the bureau.scores_monthly bands (credit-data).
- Same three bands as v1, cut on the netted value.
- Basis for the matrix v4 candidate and ror-roi-v2.
