---
from: []
updated: 2025-01-06
---
# Churn-2025 needs a label window: 60 or 90 days without spend or payment?
Open question at kickoff. A churn label is 1 if the account has no card spend and no payment for N days after the snapshot date.
- Candidates: N=60 (monthly cohorts read two cycles after scoring) and N=90 (higher base rate, slower read).
- Maya Ortiz (retention) states the business need; Lena Fischer (credit risk) signs off the spec.
- Answered by exp-101 and dec-c25-label-60d.
