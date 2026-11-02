---
updated: 2026-09-30
---
# Should payments-api rate-limit per merchant?
Merchant `m-77102` sent 41% of all requests on 2026-09-28 (a batch replay) and pushed p95 to 240 ms for 25 minutes.
Options: a per-merchant token bucket at the gateway, or one queue per merchant in the outbox. Asked by Dan Okafor.
