---
from: [feat-ch-send-window-v1, feat-ch-prior-contact-v1, ds-ch-ab-wave1]
updated: 2025-10-02
supersedes: []
---
# ch-propensity-v1 chooses between SMS and call per account by modelled promise-to-pay uplift, from send window and prior contact
Gradient-boosted model, two arms (SMS, call), target is the randomised PTP outcome from wave 1.
Features: feat-ch-send-window-v1, feat-ch-prior-contact-v1. Email open is excluded.
Evaluated on the wave-1 holdout split (exp-505). Superseded by ch-propensity-v2 (2025-11-18).
