## Q1
Chloe Martin reports campaign lift as a point estimate with its 95% confidence interval, for example "+1.8 pts (95% CI +0.6 to +3.0)". She does not show p-values, because business readers take "p = 0.04" as proof.
Sources: memory/prefs/chloe-martin-campaign-readout.md

## Q2
The winning campaign is orange #E07B24 and all other campaigns are mid-grey. She avoids brand blue as a highlight because blue series were read as "baseline" in the Q3 2025 campaign readout. Maya Ortiz uses brand blue for her focal cohort, so each chart follows its owner's convention.
Sources: memory/prefs/chloe-martin-highlight-orange.md, memory/prefs/maya-ortiz-focal-colour.md

## Q3
From 2026-06-01, any `cli-` model with PSI above 0.20 on a top-20 feature triggers a drift review; other families keep 0.25. A later correction (2026-06-10) sets general PSI at 0.10 to investigate and above 0.25 for a retrain review, but it does not mention `cli-` models, so whether 0.20 still applies to them is not settled in the notes.
Sources: memory/reporting/monthly-review-psi-trigger-v2.md, memory/corrections/psi-two-tier-thresholds.md

## Q4
Default rates, PD and roll rates in risk tables are shown to 2 decimals in percent, for example 3.84%. Lena Fischer's risk packs also show Gini and KS to 2 decimals and exposure in $m to 1 decimal.
Sources: memory/reporting/rounding-percent.md, memory/prefs/lena-fischer-risk-rounding.md

## Q5
The offer tiers come from `offers.tier_matrix`. The glossary defines tiers A to E, with A the highest (the old note saying A was lowest was corrected). A separate dataset note describes `offers.tier_matrix` v3 as retention tiers T0 to T4 in force since 2025-09-01, which conflicts with the A to E definition and is not reconciled in the notes.
Sources: memory/glossary/tier.md, memory/corrections/tier-a-highest.md, memory/retention-offers-roi/ds-ror-tier-matrix.md

## Q6
Use 1.9% blended. The 2.5% figure was the premium-card rate only, and standard cards sit around 1.6 to 1.8%. The Q4 2025 finance pack used 2.5% and was restated to 1.9%.
Sources: memory/corrections/interchange-blended.md

## Q7
No. OOT must be a period after the training window that was never used for training, tuning or feature selection. The last months of training data are in-time validation. The current split is a training window, a six-month gap, then a three-month OOT tail on `observation_date`.
Sources: memory/corrections/oot-not-training-tail.md, memory/howto/oot-split-by-observation-date.md

## Q8
DPD counts from the payment due date (since 2025-11-01). Day 1 starts the day after the due date, and a payment posted on the due date still counts as current (0 DPD). This fix went into the `cards.payments_daily` pipeline on 2026-01-15, superseding the earlier note that made the due date day 1.
Sources: memory/corrections/dpd-due-date-offbyone.md, memory/corrections/dpd-due-date.md

## Q9
Report it as lift, not uplift. Uplift is reported only on randomised treatment and control holdouts. Observational differences from `marketing.campaign_responses` are called lift; for example, Chloe Martin's Oct 2025 CLI figure of 1.8 pp was observational, and the randomised uplift was 0.9 pp.
Sources: memory/corrections/uplift-randomised-only.md, memory/howto/uplift-eval-qini-at-20pct.md

## Q10
The feature `feat_disp_cnt_90d_v1` read 14 days past the observation date, which is a leak. Restricted to days on or before observation, holdout AUC fell from 0.79 to 0.72. The leak scan flagged it, so it was rebuilt as v2 (reads only days on or before observation) and v1 was removed from training.
Sources: memory/qa/dispute-feature-leak.md, memory/howto/leakage-check-post-period.md