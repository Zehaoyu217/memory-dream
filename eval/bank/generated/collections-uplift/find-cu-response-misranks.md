---
from: [exp-101, exp-102]
updated: 2025-05-16
---
# The response model misranks: its top 20% holds accounts who would pay without a call, uplift 0.012 against 0.031
In exp-101 the response model captured 38% of PTP events in its top 20%. In exp-102 the same ranking produced an uplift of only 0.012, because many top-ranked accounts were going to pay anyway.
Implication: a call budget spent by response rank buys calls for people who pay on their own. Routing should use uplift rank.
Reviewed by Sam Lee and Raj Patel on 2025-05-15.
