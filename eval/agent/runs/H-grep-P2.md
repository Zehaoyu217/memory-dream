## Q1
Chloe Martin wants campaign lift shown as a point estimate with its 95% confidence interval, e.g. "+1.8 pts (95% CI +0.6 to +3.0)". She does not show p-values, because business readers treat "p = 0.04" as proof. Cost per response in $ sits beside the lift in the same table.
Sources: memory/prefs/chloe-martin-campaign-readout.md

## Q2
She highlights the winning campaign in orange `#E07B24` and greys all other campaigns. She avoids brand blue as a highlight because blue series were read as "baseline" in the Q3 2025 campaign readout.
Sources: memory/prefs/chloe-martin-highlight-orange.md

## Q3
Credit-line (`cli-`) models trigger a drift review at PSI above 0.20 on a top-20 feature, from 2026-06-01; all other families keep 0.25, with 0.10 to 0.25 as "watch". Caveat: a later note (2026-06-10) sets PSI above 0.10 to investigate and above 0.25 to retrain review for score and feature PSI, and does not mention the `cli-` exception, so confirm which applies.
Sources: memory/reporting/monthly-review-psi-trigger-v2.md, memory/corrections/psi-two-tier-thresholds.md

## Q4
Default rates, PD and roll rates in risk tables use 2 decimals, e.g. 3.84%. Other percentages (retention, share, campaign response) use 1 decimal, and changes are written as "pts", never "%".
Sources: memory/reporting/rounding-percent.md, memory/prefs/lena-fischer-risk-rounding.md

## Q5
Offer tiers come from `offers.tier_matrix`. The glossary says tiers run A to E, with A the highest (corrected from an earlier note that said A was lowest). Note that a retention-offers note describes a different T0 to T4 scheme in `offers.tier_matrix` v3, so check which matrix you need.
Sources: memory/glossary/tier.md, memory/corrections/tier-a-highest.md, memory/retention-offers-roi/ds-ror-tier-matrix.md

## Q6
Use a blended interchange rate of 1.9% for the book, not 2.5%. The 2.5% was the premium-card rate only, and standard cards sit around 1.6 to 1.8%. The Q4 2025 finance pack was restated to 1.9%.
Sources: memory/corrections/interchange-blended.md

## Q7
No. OOT is a period after the training window that was never used for training, tuning or feature selection, not the last three months of training data. The last months of training data are in-time validation.
Sources: memory/corrections/oot-not-training-tail.md, memory/glossary/oot.md

## Q8
DPD counts from the minimum payment due date, and day 1 starts the day after the due date. A payment posted on the due date still counts as current (0 DPD). This fix went into the `cards.payments_daily` pipeline on 2026-01-15 and replaced the 2025-11 rule that made the due date itself day 1.
Sources: memory/corrections/dpd-due-date-offbyone.md, memory/corrections/dpd-due-date.md

## Q9
Do not call it uplift. Uplift is reported only from randomised treatment and control holdouts; a non-randomised control group gives observational differences, which are reported as "lift". For example, the Oct 2025 CLI report showed 1.8 pp observationally, while the randomised uplift was 0.9 pp.
Sources: memory/corrections/uplift-randomised-only.md

## Q10
The dispute-count feature (`feat_disp_cnt_90d_v1`) was rebuilt because it read 14 days past the observation date, which inflated holdout AUC from 0.72 to 0.79. The leak scan flagged it, and the v2 rebuild reads only days on or before observation.
Sources: memory/qa/dispute-feature-leak.md