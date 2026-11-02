---
from: [rel-v3-5-0, adr-capture-outbox]
updated: 2026-09-29
---
# payments-api: the card payment service (HTTP and gRPC), owned by platform-team
`payments-api` takes POST /payments, authorises the card with `risk-service` and the acquirer, and records every
attempt in `payments.ledger` through mod-ledger-writer. Since rel-v3-5-0 capture runs off the request path: the
request writes `payments.capture_outbox` and svc-capture-worker completes it (flag `capture_async`, at 100%).
Calls: `orders-service` (order lookup), `risk-service` (fraud score), `acquirer-gateway` (authorisation).
Reads: `customers.cards`. Writes: `payments.ledger`, `payments.capture_outbox`.
Load and latency in prod-eu, 2026-09-26 to 2026-09-28: peak 1,250 req/s; POST /payments p95 160 ms, p99 410 ms;
error rate 0.21%. Owned by platform-team; on-call Dan Okafor. Repo `git/payments-api`, entrypoint `src/payments/app.py`.
The gRPC endpoint is retired on 2026-12-15 (see [[dec-retire-grpc]]).
