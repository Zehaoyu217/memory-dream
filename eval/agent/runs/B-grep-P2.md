## Q1
Chloe Martin reports campaign lift as a point estimate with its 95% confidence interval, for example "+1.8 pts (95% CI +0.6 to +3.0)". She does not show p-values, because business readers take "p = 0.04" as proof. Cost per response in $ goes in the same table as the lift. The intervals come from 500 account-level bootstrap resamples within each arm, using the 2.5th and 97.5th percentiles.
Sources: memory/prefs/chloe-martin-campaign-readout.md, memory/reporting/campaign-readout-template.md, memory/howto/bootstrap-ci-for-uplift.md, memory/qa/offer-test-uplift-interval.md
## Q2
She shows the winning campaign in orange `#E07B24` and every other campaign in mid-grey. She avoids brand blue as a highlight because readers of the Q3 2025 campaign readout took blue series to mean "baseline". Maya Ortiz does use brand blue for her focal cohort, so each chart follows its owner's convention.
Sources: memory/prefs/chloe-martin-highlight-orange.md
## Q3
From 2026-06-01, a `cli-` model triggers a drift review when PSI goes above 0.20 on any of its top-20 features. Before that the trigger was 0.25, and all other model families still use 0.25 (0.10 to 0.25 stays "watch" for them). The change followed `cli-glm-v2`, which drifted to PSI 0.22 on `cli_util_ratio` in 2026-04 and was not reviewed until the next cycle.
Sources: memory/reporting/monthly-review-psi-trigger-v2.md (supersedes memory/reporting/monthly-review-psi-trigger.md), memory/reporting/monthly-model-review-agenda.md
## Q4
Default rates and PD in risk tables use 2 decimals in percent, for example 3.84%. Roll rates and ratios such as loss-to-book also use 2 decimals. General percentages such as retention, share and response use 1 decimal, and changes are written in "pts".
Sources: memory/reporting/rounding-percent.md, memory/prefs/lena-fischer-risk-rounding.md
## Q5
Offer tiers are assigned to each account from the `offers.tier_matrix` table, and CLI offers come from the same table. Tiers run A to E: a later correction says A is the highest tier with the best promotional APRs and E the lowest. On the retention side, Maya Ortiz owns the matrix: v3 is a grid of churn decile by value band giving tiers T0 to T4, v4 applies from the April 2026 cycle, and the churn-2026 risk-tier cuts (0.20 and 0.50) are written into `offers.tier_matrix` every night.
Sources: memory/glossary/tier.md, memory/corrections/tier-a-highest.md, memory/glossary/cli.md, memory/retention-offers-roi/ds-ror-tier-matrix.md, memory/retention-offers-roi/dec-ror-matrix-v4.md, memory/churn-2026/dec-risk-tiers.md
## Q6
Use the blended rate of 1.9%, so $100 of purchases earns $1.90. Do not use 2.5%: that is the premium-card rate only, and standard cards sit around 1.6–1.8%. The Q4 2025 finance pack used 2.5% and was restated to 1.9%. Since 2026-01-01 the book also excludes commercial cards, and Ben Carter wants this called "interchange income", not "revenue", in finance text.
Sources: memory/corrections/interchange-blended.md (supersedes memory/glossary/interchange.md), memory/corrections/book-excludes-commercial.md, memory/prefs/ben-carter-interchange-wording.md
## Q7
No. OOT has to be a period after the training window that was never used for training, tuning or feature selection; the last months of training data are only in-time validation. For example, the fraud model's 0.88 AUC was in-time, and its true OOT AUC (2024-10 to 2024-12) was 0.84. The split rule is to split on `observation_date`, leave a six-month gap after training, then use a three-month OOT window.
Sources: memory/corrections/oot-not-training-tail.md (supersedes memory/glossary/oot.md), memory/howto/oot-split-by-observation-date.md
## Q8
Since 2025-11-01, DPD counts from the minimum payment due date, not the statement close date. A correction dated 2026-01-15 moved day 1 to the day after the due date: a payment posted on the due date still counts as current (0 DPD). So a minimum due on 1 Oct that is still unpaid is 1 DPD on 2 Oct. The fix shifted the Nov–Dec 2025 1-29 bucket counts by one day; the 30+ buckets did not change.
Sources: memory/corrections/dpd-due-date-offbyone.md (supersedes memory/corrections/dpd-due-date.md, which superseded memory/glossary/dpd.md)
## Q9
Don't call it uplift. Uplift is reported only when treatment and control are randomised holdouts, and an observational difference from `marketing.campaign_responses` is reported as "lift". For example, Chloe Martin's Oct 2025 CLI report showed a 1.8 pp "uplift" that was observational; the randomised uplift was 0.9 pp. A proper holdout is 10% of the eligible list drawn at random before send, with at least 3,000 accounts per arm.
Sources: memory/corrections/uplift-randomised-only.md (supersedes memory/glossary/uplift.md), memory/howto/campaign-holdout-design.md, memory/qa/uplift-arm-minimum-q.md
## Q10
The leak scan flagged `feat_disp_cnt_90d_v1` because it read events up to 14 days after the observation date. With the leak, holdout AUC was 0.79; with the feature restricted to days on or before observation it fell to 0.72. The feature was rebuilt as v2, which reads only days on or before observation, and v1 was removed from training. A separate case in complaint-classification: dispute link v1 counted disputes opened after the complaint and was replaced by v2 (honest gain +0.03 macro F1, not +0.14).
Sources: memory/qa/dispute-feature-leak.md, memory/howto/leakage-check-post-period.md, memory/complaint-classification/fnd-cc-dispute-link-leak.md, memory/complaint-classification/feat-cc-dispute-link-v2.md