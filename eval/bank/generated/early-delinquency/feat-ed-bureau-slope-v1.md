---
from: [ds-ed-bureau-join]
updated: 2026-01-27
---
# feat-ed-bureau-slope-v1 is the slope of the bureau score over 6 months from bureau.scores_monthly
Feature: least-squares slope of bureau score over the six months before snapshot, plus the score at snapshot.
Source: `bureau.scores_monthly`. Accounts without six months of history use the available months; the count is a feature.
Coverage of the slope feature is 84%; the rest are thin-file.
