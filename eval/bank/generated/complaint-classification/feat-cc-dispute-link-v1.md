---
from: [ds-cc-tickets-raw]
updated: 2025-11-10
---
# Dispute link v1 counts disputes on the same account in the trailing 60 days, any status, including disputes opened after the complaint
Joins the account key to `cards.disputes` (owner fraud-ops). Two features: dispute count and a flag for any dispute.
Window runs to the present, so it picks up disputes created after the ticket. Those are often triggered by the complaint itself.
Superseded by feat-cc-dispute-link-v2 after the May 2026 check (fnd-cc-dispute-link-leak).
