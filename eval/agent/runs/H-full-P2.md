## Q1
Chloe Martin wants lift shown as a point estimate with its 95% confidence interval, for example "+1.8 pts (95% CI +0.6 to +3.0)". She does not show p-values, because business readers take "p = 0.04" as proof. Cost per response in $ sits beside the lift in the same table.
Sources: memory/prefs/chloe-martin-campaign-readout.md, memory/prefs/chloe-martin-highlight-orange.md

## Q2
She highlights the winning campaign in orange `#E07B24` and greys all other campaigns. She does not use brand blue as a highlight, because blue series were read as "baseline" in the Q3 2025 campaign readout. Maya Ortiz uses brand blue for her focal cohort, so each chart follows its owner's convention.
Sources: memory/prefs/chloe-martin-highlight-orange.md, memory/prefs/maya-ortiz-focal-colour.md

## Q3
The current rule (from 2026-06-01) is that any `cli-` model with a PSI above 0.20 on a top-20 feature triggers a drift review, and other families keep 0.25. A later correction (2026-06-10) sets PSI above 0.10 as investigate and above 0.25 as retrain review for score and feature PSI, and does not mention `cli-` models, so whether the 0.20 `cli-` trigger still applies is unclear and should be confirmed.
Sources: memory/reporting/monthly-review-psi-trigger-v2.md, memory/corrections/psi-two-tier-thresholds.md

## Q4
Default rates, PD and roll rates in risk tables are shown to 2 decimals in percent, for example 3.84%. Changes are written as "pts", and Lena Fischer also takes Gini and KS to 2 decimals and exposure in $m to 1 decimal.
Sources: memory/reporting/rounding-percent.md, memory/prefs/lena-fischer-risk-rounding.md

## Q5
Offer tiers come from the `offers.tier_matrix` table. Tiers run A to E, with A the highest and E the lowest (the old glossary had this reversed). The retention matrix v3 (in force since 2025-09-01, owned by Maya Ortiz) uses T0 to T4 tiers by churn decile and value band.
Sources: memory/corrections/tier-a-highest.md, memory/retention-offers-roi/ds-ror-tier-matrix.md

## Q6
Use a blended interchange rate of 1.9% on the book. The old 2.5% was the premium-card rate only, and the Q4 2025 finance pack was restated to 1.9%.
Sources: memory/corrections/interchange-blended.md

## Q7
No. OOT is a period after the training window that was never used for training, tuning or feature selection. The last months of training data are in-time validation, and the current split uses observation months with a six-month gap and a three-month OOT tail.
Sources: memory/corrections/oot-not-training-tail.md, memory/howto/oot-split-by-observation-date.md

## Q8
Day 1 starts the day after the payment due date. A payment posted on the due date still counts as current (0 DPD). This corrected the 2025-11 rule, which made day 1 the due date itself, and it was fixed in `cards.payments_daily` on 2026-01-15.
Sources: memory/corrections/dpd-due-date-offbyone.md

## Q9
Report it as lift, not uplift. Uplift is reported only on randomised holdouts, and observational differences from `marketing.campaign_responses` are called lift. For example, Chloe Martin's Oct 2025 "1.8 pp uplift" was observational, and the randomised uplift was 0.9 pp.
Sources: memory/corrections/uplift-randomised-only.md

## Q10
The feature `feat_disp_cnt_90d_v1` read 14 days past the observation date, which is a leak. Restricting it to days on or before observation dropped holdout AUC from 0.79 to 0.72, so it was rebuilt as v2 and v1 was removed from training.
Sources: memory/qa/dispute-feature-leak.md, memory/howto/leakage-check-post-period.md