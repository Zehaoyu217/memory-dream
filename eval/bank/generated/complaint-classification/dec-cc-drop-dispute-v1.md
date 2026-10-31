---
from: [fnd-cc-dispute-link-leak, feat-cc-dispute-link-v2]
updated: 2026-05-20
---
# Drop dispute link v1 from the classifier; v2 is the only dispute feature from this date
Dispute link v1 is removed from the feature store. v2 is used in cc-ft-v2 and cc-logreg-v1 reruns.
Reason: v1 gain was mostly leakage (fnd-cc-dispute-link-leak). Owner Aisha Khan (MLOps).
