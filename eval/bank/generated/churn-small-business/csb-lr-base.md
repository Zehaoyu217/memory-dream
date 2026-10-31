---
from: [feat-csb-spend-raw, feat-csb-tenure-band, ds-csb-oot-2025q1, ds-csb-churn-labels]
updated: 2025-10-08
---
# csb-lr-base: logistic baseline on SMB, holdout AUC 0.684
- L2 logistic regression on 6 features (spend, tenure band, months on book, employee cards, limit band, industry group), 90-day labels.
- Holdout csb-oot-2025q1 (n=8,914, all tenures): AUC 0.684, KS 0.26, Brier 0.0612.
- Floor for the tree models.
