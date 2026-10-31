---
from: [ch-propensity-v1, exp-506, feat-ch-prefer-channel-v1]
updated: 2025-11-18
supersedes: [ch-propensity-v1]
---
# ch-propensity-v2 adds the prefer-channel feature to the channel-choice model; uplift@20% 0.027 on the wave-1 holdout
Features: feat-ch-send-window-v1, feat-ch-prior-contact-v1, feat-ch-prefer-channel-v1.
Metrics: uplift@20% 0.027 on the wave-1 holdout split (n=17,200), against 0.021 for ch-propensity-v1.
Current channel-choice model. The bandit in ch-bandit-v1 is simulated but not promoted.
