---
updated: 2026-06-18
---
# The risk-service call is 180 ms of the 290 ms p95 of POST /payments
Traced 2026-06-01 to 2026-06-14 in `prod-eu` (`traces/payments-api`): p95 290 ms, of which `risk-service` 180 ms,
`acquirer-gateway` 70 ms, the `payments.ledger` write 12 ms. The 300 ms budget was missed on 2 of 14 days. Caching
the risk decision for 60 s per card would save about 110 ms p95 (replayed 2026-06-16). Owner Priya Nair.
