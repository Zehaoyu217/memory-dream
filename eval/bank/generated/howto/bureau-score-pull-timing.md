---
updated: 2025-05-06
---
# Use the bureau score dated at least 30 days before the observation date
From `bureau.scores_monthly`, take the score with `score_date` at least 30 days before `observation_date`. Scores pulled inside the observation month are leaked. A same-month pull added 0.02 AUC on the 2025 default model, and Lena Fischer rejected it as leakage.
Bureau pulls land on the 1st of the month, so a one-month lag is the natural cut.
