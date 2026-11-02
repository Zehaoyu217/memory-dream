---
from: [inc-2026-08-11-ledger-lag, q-capture-mode]
supersedes: [dec-capture-sync]
updated: 2026-08-14
---
# Capture moves off the request path; authorisation stays synchronous
Decision, 2026-08-14. After inc-2026-08-11-ledger-lag held 2,310 captures inside requests for 39 minutes, capture is
done after the response by a worker, under a flag, merchant by merchant. Authorisation keeps its synchronous path.
Design in [[adr-capture-outbox]]. Owner Priya Nair; agreed with Lena Fischer for product.
