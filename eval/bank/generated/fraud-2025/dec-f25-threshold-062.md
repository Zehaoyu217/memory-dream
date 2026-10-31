---
from: [exp-103, fraud25-find-threshold-fine]
updated: 2025-06-24
---
# Set the fraud-2025 live alert threshold to 0.62 from 2025-07-01
Decision: fraud25-gbm-v2 alerts at score >= 0.62 go live from 2025-07-01.
Basis: exp-103 (14.2% precision, 0.9% alert rate on holdout-2025q1).
Superseded by dec-f25-threshold-070 after the travel over-flagging review.
