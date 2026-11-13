## Q2: income estimate chain

inc-gbm-v1 was replaced by inc-gbm-v2 (2025-12-18), and inc-gbm-v2 was replaced by inc-gbm-v3. The note in force is **inc-gbm-v3**, which became the live estimate under dec-inc-estimate-live (2026-05-12).

inc-gbm-v3 builds on:
- ds-inc-verified-2026 (the verified-2026 sample it is evaluated on)
- find-inc-log-target-gain (the log-target finding)
- the cadence-stability model. That description matches inc-gbm-v2, so the chain is inc-gbm-v3 → inc-gbm-v2 → inc-gbm-v1 (through "replaces" links, not an explicit build link)

## Q3: channel bandit

ch-bandit-v1 builds on **ch-propensity-v2** and **exp-507-collections-channel-mix**.

- ch-propensity-v2 builds on the original sms-or-call propensity model, exp-506-collections-channel-mix and feat-ch-prefer-channel-v1. exp-506 uses the same wave-1 holdout split as exp-505 (n=17,200), which builds on the original propensity model.
- exp-507 is a simulation on wave-2 data, using ch-propensity-v2 scores as priors. It builds on "the second randomised channel test".

Gap: neither wave-1 nor wave-2 is recorded as a ds- dataset note in this folder. The trace stops at exp-505/exp-507, and the "second randomised channel test" has no note id.

## Q4: txc-gbm-v2 and txc-logreg-v1

Confirmed. Both notes list the same two direct builds-on targets:
- **txc-gbm-v2** builds on feat-txc-descriptor-tokens-v1, feat-txc-mcc-prior and the logistic regression baseline.
- **txc-logreg-v1** builds on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.

The features trace to ds-txc-labelled-merchants and ds-txc-descriptor-sample (for descriptor tokens) and ds-txc-mcc-crosswalk (for the MCC prior).

## Q5: complaint classifier, decision-note step

The chain is cc-logreg-v1 → ds-cc-holdout. ds-cc-holdout's own note says it is "used for all model and threshold decisions in this project", so the holdout dependency is documented.

Decision notes that rest on ds-cc-holdout:
- **dec-cc-ft-v1**: explicit. It rests on exp-201 (the encoder versus logistic regression comparison), which builds on cc-logreg-v1, which builds on ds-cc-holdout. It also rests on fnd-cc-coverage.
- **dec-cc-auto-threshold**: through fnd-cc-coverage → exp-206, a threshold sweep on holdout-2025q4 (n=1,800). The build line names fnd-cc-coverage only, so the holdout edge is through the evaluation set rather than an explicit build link.

Not on the holdout chain as far as I traced:
- **dec-cc-drop-dispute-v1** builds on feat-cc-dispute-link-v2 and the dispute-link leakage finding.
- **dec-cc-taxonomy-split** was not checked.

## Q1 check on dec-ch-call-escalation

The dependency is now confirmed. The explicit edge is dec-ch-call-escalation → find-ch-sms-call-gap → find-cu-sms-cost. find-cu-sms-cost's body names cu-uplift-v3 directly, so the "uplift model with bureau delta" link is supported.

There is a problem with that link. find-cu-sms-cost's header says the 83% SMS-to-call figure holds for 1-7 DPD and that the gap is wider for 8-29 DPD. find-ch-sms-call-gap cites the same 83% for the top 20% on 8-29 DPD. The underlying exp-107 population is 1-29 DPD. So the 83% figure is being applied to a segment the source note says it does not cover. dec-ch-call-escalation inherits that problem.