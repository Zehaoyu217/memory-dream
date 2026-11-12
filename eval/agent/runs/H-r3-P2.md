## Q1
Chloe Martin wants campaign lift shown as a point estimate with its 95% confidence interval, e.g. "+1.8 pts (95% CI +0.6 to +3.0)". She does not show p-values, since business readers treat "p = 0.04" as proof.
Sources: memory/prefs/chloe-martin-campaign-readout.md

## Q2
She highlights the winning campaign in orange `#E07B24` and greys out all other campaigns. She does not use brand blue as a highlight because blue series were read as "baseline" in the Q3 2025 campaign readout. Maya Ortiz uses brand blue for her focal cohort, so each chart follows its owner's convention.
Sources: memory/prefs/chloe-martin-highlight-orange.md, memory/reporting/chart-style-colour.md, memory/prefs/maya-ortiz-focal-colour.md

## Q3
For `cli-` models from 2026-06-01, a top-20 feature with PSI above 0.20 triggers a drift review; other models keep 0.25. The general two-tier rule (investigate above 0.10, retrain review above 0.25) is in the correction that supersedes the older 0.25-means-investigate note. The 0.20 credit-line rule is the most specific and newest one that applies.
Sources: memory/reporting/monthly-review-psi-trigger-v2.md, memory/corrections/psi-two-tier-thresholds.md

## Q4
Default rates, PD and roll rates in risk tables are shown to 2 decimals in percent (e.g. 3.84%). Other percentages (retention, share, campaign response) use 1 decimal. Lena Fischer's risk packs also use 2 decimals for Gini and KS.
Sources: memory/reporting/rounding-percent.md, memory/prefs/lena-fischer-risk-rounding.md

## Q5
Offer tiers come from `offers.tier_matrix`. Tiers run A to E, with A the highest (most generous promotional APRs) and E the lowest; an earlier note saying A was lowest was corrected. Retention's separate `offers.tier_matrix` v3 (T0 to T4, in force since 2025-09-01, owned by Maya Ortiz) is a different tiering.
Sources: memory/corrections/tier-a-highest.md, memory/glossary/tier.md, memory/retention-offers-roi/ds-ror-tier-matrix.md

## Q6
Use 1.9% blended. The old 2.5% was the premium-card rate only; standard cards sit around 1.6 to 1.8%. The Q4 2025 finance pack that used 2.5% was restated to 1.9%.
Sources: memory/corrections/interchange-blended.md

## Q7
No. OOT must be a period after the training window that was never used for training, tuning or feature selection. The last months of the training data are in-time validation, not OOT. An earlier note saying otherwise was corrected.
Sources: memory/corrections/oot-not-training-tail.md, memory/howto/oot-split-by-observation-date.md

## Q8
From 2026-01-15, day 1 starts the day after the due date, and a payment posted on the due date still counts as current (0 DPD). The earlier 2025-11 rule (day 1 = the due date itself) was off by one day. The 30+ buckets did not change.
Sources: memory/corrections/dpd-due-date-offbyone.md, memory/corrections/dpd-due-date.md

## Q9
Report uplift only from randomised holdouts, with treatment and control randomised. Differences from a non-randomised control group in `marketing.campaign_responses` are called lift, not uplift. Chloe Martin's Oct 2025 CLI report had a 1.8 pp "uplift" that was observational; the randomised uplift was 0.9 pp.
Sources: memory/corrections/uplift-randomised-only.md, memory/glossary/uplift.md

## Q10
The `feat_disp_cnt_90d_v1` dispute-count feature read 14 days past the observation date, which is leakage. Restricted to days on or before observation, holdout AUC fell from 0.79 to 0.72, so it was rebuilt as v2 and v1 was removed from training.
Sources: memory/qa/dispute-feature-leak.md, memory/howto/leakage-check-post-period.md