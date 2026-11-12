## Q1
Chloe Martin wants lift shown as a point estimate with its 95% confidence interval, e.g. "+1.8 pts (95% CI +0.6 to +3.0)", with cost per response in $ beside it in the same table. She does not show p-values, because business readers take "p = 0.04" as proof.
Sources: memory/prefs/chloe-martin-campaign-readout.md

## Q2
She highlights the winning campaign in orange `#E07B24` and greys out all others. She avoids brand blue as a highlight because blue series were read as "baseline" in the Q3 2025 campaign readout. Maya Ortiz uses brand blue for her focal cohort, so each chart follows its owner's convention.
Sources: memory/prefs/chloe-martin-highlight-orange.md

## Q3
From 2026-06-01, a `cli-` model with PSI above 0.20 on any top-20 feature triggers a drift review. All other model families keep the 0.25 trigger, and 0.10 to 0.25 stays "watch" for them. This supersedes the earlier 0.25 rule for all models.
Sources: memory/reporting/monthly-review-psi-trigger-v2.md

## Q4
Default rates, PD and roll rates in risk tables are shown to 2 decimals in percent, e.g. 3.84%. Other percentages (retention, share, campaign response) use 1 decimal, and changes are written in "pts".
Sources: memory/reporting/rounding-percent.md

## Q5
Offer tiers come from `offers.tier_matrix`. Tier A is the highest tier and E the lowest (the older note saying A was lowest is corrected). A separate retention v3 matrix (T0 to T4, in force since 2025-09-01, owned by Maya Ortiz) also exists.
Sources: memory/corrections/tier-a-highest.md, memory/retention-offers-roi/ds-ror-tier-matrix.md

## Q6
Use 1.9% blended interchange on the book, not 2.5%. The 2.5% figure was the premium-card rate only, and standard cards sit around 1.6 to 1.8%. The Q4 2025 finance pack was restated from 2.5% to 1.9%.
Sources: memory/corrections/interchange-blended.md

## Q7
No. OOT must be a period after the training window that was never used for training, tuning or feature selection. The last months of training data are in-time validation, not OOT. The earlier "last three months of training" definition is superseded.
Sources: memory/corrections/oot-not-training-tail.md

## Q8
Day 1 starts the day after the due date. A payment posted on the due date still counts as current (0 DPD). The pipeline fix was made in `cards.payments_daily` on 2026-01-15, which shifted the 1-29 bucket counts for Nov-Dec 2025 by one day; the 30+ buckets did not change.
Sources: memory/corrections/dpd-due-date-offbyone.md

## Q9
Do not report it as uplift. Uplift is reported only on randomised holdouts, so an observational difference from `marketing.campaign_responses` is called lift instead. Chloe Martin's Oct 2025 CLI report had a 1.8 pp "uplift" that was observational; the randomised uplift was 0.9 pp.
Sources: memory/corrections/uplift-randomised-only.md, memory/howto/uplift-eval-qini-at-20pct.md

## Q10
The feature `feat_disp_cnt_90d_v1` read 14 days past the observation date. The leak scan flagged it, and once restricted to days on or before observation, holdout AUC fell from 0.79 to 0.72. The rebuilt v2 reads only days on or before observation, and v1 was removed from training.
Sources: memory/qa/dispute-feature-leak.md, memory/howto/leakage-check-post-period.md