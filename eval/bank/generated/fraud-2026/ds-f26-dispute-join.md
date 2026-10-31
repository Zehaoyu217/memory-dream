---
from: [ds-f26-labels-2026]
updated: 2026-03-02
---
# cards.disputes joined to CNP labels on auth_id; 11% of frauds appear only as disputes
Join: `cards.disputes` to `cards.fraud_labels` on auth_id, keeping the earliest dispute per auth.
About 11% of CNP fraud cases exist only in `cards.disputes` and are added as positives.
Owned by fraud-ops; the join rule is the source of the 2026 velocity join-window bug (fraud26-find-velocity-clean).
