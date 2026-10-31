---
updated: 2025-12-02
supersedes: [glossary/uplift]
---
# uplift is reported only on randomised holdouts
The old note allowed uplift from any campaign file with a control group. Uplift is reported only when treatment and control are randomised holdouts. Observational differences from `marketing.campaign_responses` are called lift.
Affected: Chloe Martin's Oct 2025 CLI report. The 1.8 pp "uplift" was observational; the randomised uplift is 0.9 pp.
