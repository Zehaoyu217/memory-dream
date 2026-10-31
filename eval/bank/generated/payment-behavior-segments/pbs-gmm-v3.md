---
from: [pbs-gmm-v2, feat-pbs-timing-v2, exp-403]
supersedes: [pbs-gmm-v2]
updated: 2026-01-19
---
# pbs-gmm-v3 is the current segment model: five components, seed ARI 0.81
Gaussian mixture, five components, on the pbs-gmm-v2 inputs plus feat-pbs-timing-v2.
Seed-to-seed ARI 0.81, silhouette 0.42 on the 200k sample of ds-pbs-frame-h1-2025.
Segments: transactor, revolver, minimum-payer, cash-heavy, dormant. Refreshed monthly (dec-pbs-monthly-refresh).
