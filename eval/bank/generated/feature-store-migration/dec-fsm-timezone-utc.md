---
from: [exp-102, fnd-parity-pre-fix]
updated: 2025-11-20
---
# Decision: all date windows and day differences in the feature store and legacy notebooks use UTC
Decided at the 2025-11-20 MLOps review (Aisha Khan, Lena Fischer). Local-time windows caused the 3.1 percent payment-lag mismatch (exp-102).
Rule: every snapshot date and every timestamp-to-day conversion is UTC. Legacy notebooks are patched to match, not retired yet.
Consequence: feat-fsm-payment-lag-v2 replaces v1 for all new models from 2026-01-12.
