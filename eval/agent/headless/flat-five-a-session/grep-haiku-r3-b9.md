**Q1 (decisions resting on ds-cc-call-outcomes):** Four decisions: dec-cu-drop-tod, dec-cu-uplift-for-calls, dec-cu-promote-v3, dec-ch-call-escalation. The chain runs through feat-cu-call-tod-v1, cu-resp-v1, feat-cu-contact-hist-v2, exp-103, exp-101, cu-uplift-v1/v2/v3, exp-105, exp-107, find-cu-sms-cost and find-ch-sms-call-gap.

**Q2 (inc-gbm-v1 line):** inc-gbm-v1 was replaced by inc-gbm-v2, which was replaced by inc-gbm-v3. inc-gbm-v3 is the current estimate model (dec-inc-estimate-live, adopted 2026-05-12). Its note says "Replaces inc-gbm-v2" and nothing in the notes says it has been replaced. I searched for references to a successor and found none.

**Q3 (ch-bandit-v1 back to dataset notes):**
- ch-bandit-v1 builds on ch-propensity-v2 (priors) and exp-507-collections-channel-mix (simulation).
- ch-propensity-v2 builds on the original sms-or-call model (ch-propensity-v1), feat-ch-prefer-channel-v1, and exp-506.
- ch-propensity-v1 builds on ds-ch-ab-wave1 (wave-1 randomised test), feat-ch-send-window-v1 and the prior-contact count (feat-ch-prior-contact-v1).
- exp-507 builds on the second randomised test, ds-ch-ab-wave2 (72,500 accounts, Jan–Feb 2026), which in turn builds on the first test.
- The features also trace to ds-ch-contact-costs (per-contact cost figures).

**Q4 (feature notes shared directly by txc-gbm-v2 and txc-logreg-v1):** feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior. txc-logreg-v1 is itself the baseline that txc-gbm-v2 builds on, so it is a dependency of txc-gbm-v2 rather than a shared feature.

**Q5 (decisions resting on ds-cc-holdout):**
- Direct link: cc-logreg-v1 is the only note that builds on ds-cc-holdout.
- Through cc-logreg-v1: exp-201 to exp-205 (complaint-classification comparisons). dec-cc-ft-v1 relies on the encoder-versus-logistic-regression comparison from exp-201, so it rests on ds-cc-holdout indirectly.
- By stated usage: ds-cc-holdout says it is "used for all model and threshold decisions in this project". That covers dec-cc-auto-threshold (0.95 threshold, via fnd-cc-coverage and exp-206), though its note does not link to ds-cc-holdout directly. Treat that one as resting on the holdout by stated usage, not by the link graph.

I did not modify any files; everything above is from reading the notes in memory/work.