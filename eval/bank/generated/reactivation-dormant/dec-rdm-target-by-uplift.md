---
from: [fnd-rdm-prior-responder-trap, exp-303, rdm-uplift-v1]
updated: 2025-05-27
---
# Decision: target reactivation sends by predicted uplift, not response propensity
- Prior responders are no longer sent by default; they get a send only when predicted uplift is at least 0.5pp.
- Basis: exp-303 (2.8pp against 0.9pp at the top 20%) and fnd-rdm-prior-responder-trap.
- Owner: Chloe Martin (marketing) for campaign rules; Sam Lee (ML engineering) for the scoring job.
