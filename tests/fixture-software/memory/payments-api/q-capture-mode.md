---
updated: 2026-03-03
---
# Should capture run inside the payment request or after it?
Capture can follow authorisation in the same request, or be queued and completed by a worker. Product wants the
simplest path that keeps POST /payments under the 300 ms p95 budget. Asked by Lena Fischer, 2026-03-03.
