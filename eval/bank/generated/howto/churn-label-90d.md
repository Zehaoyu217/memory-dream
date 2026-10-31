---
updated: 2026-01-12
supersedes: [howto/churn-label-60d]
---
# Churn means no purchase or payment for 90 days after observation
The current churn label in `cards.churn_labels` uses a 90-day window. The December 2025 cohort shows 9.8% churn under the 60-day window and 6.1% under 90 days, because holiday dormancy no longer counts as churn.
Models trained on the 60-day label must be retrained before the next scoring run. Tomás Rivera's team backfilled the table from 2024-01.
