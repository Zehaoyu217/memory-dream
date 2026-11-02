---
updated: 2026-02-20
---
# Every POST /payments must be safe to retry for at least 24 hours
Merchant contracts (`contracts/psp-terms-2026.pdf`, clause 4.3) require that a retried payment request with the same
`Idempotency-Key` never charges twice, for at least 24 hours after the first attempt. Acceptance: a replay of 10,000
duplicate requests produces 0 extra charges. Owner Lena Fischer.
