---
updated: 2025-01-13
---
# PSI (population stability index)
PSI measures how far a feature's or score's distribution has moved between a baseline population and a current population. Formula: sum over bins of (a - e) x ln(a / e), where a is the current share in the bin and e the baseline share. Bins are usually deciles of the baseline.
Rule of thumb in the team: PSI above 0.25 means retrain the model.
