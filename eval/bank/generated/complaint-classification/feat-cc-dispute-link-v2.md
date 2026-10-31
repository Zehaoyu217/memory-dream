---
from: [feat-cc-dispute-link-v1, fnd-cc-dispute-link-leak]
updated: 2026-05-14
supersedes: [feat-cc-dispute-link-v1]
---
# Dispute link v2 counts disputes opened on or before the ticket's opened_at, within 30 days before it
Same two features as v1 (count and flag), restricted to disputes opened no later than the ticket. No post-ticket rows enter the feature.
Used by cc-ft-v2 at the classifier head. On holdout-2025q4 the gain is +0.03 macro F1 over the base (exp-204).
