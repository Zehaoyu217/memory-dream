---
from: [ds-cu-cases-dpd]
updated: 2026-01-12
---
# feat-cu-bureau-delta is the 3-month change in bureau score from bureau.scores_monthly
Feature: bureau score at the decision month minus the score three months earlier, plus a flag for a drop of 40 points or more.
Source: `bureau.scores_monthly` (credit-data), joined at the snapshot date. No bureau pull is made at contact time.
Coverage 93% of accounts. Missing scores are set to the segment median and flagged.
Adds +0.009 AUC and +0.005 uplift@20% in exp-106.
