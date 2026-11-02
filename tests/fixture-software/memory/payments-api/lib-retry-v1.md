---
updated: 2026-03-12
---
# retry library v1: two attempts with a fixed 500 ms delay on 5xx and timeouts
`src/payments/retry.py`. Wraps outbound calls to `risk-service` and `acquirer-gateway`: on a 5xx or a timeout, wait
500 ms and try once more. No jitter. Chosen for simplicity on 2026-03-12. Owner Priya Nair.
