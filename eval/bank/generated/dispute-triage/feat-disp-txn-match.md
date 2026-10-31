---
from: [ds-disp-disputes]
updated: 2026-02-19
---
# feat-disp-txn-match: 1 when an auth record matches on auth_id and amount within 1%
Boolean: matching authorisation found on auth_id with the disputed amount within 1%.
Mismatches are a strong sign of a merchant error rather than customer dispute.
Shipped in disp-lgbm-v2 with amount band.
