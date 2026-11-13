I can answer Q9 from the notes I've read, but not the other nine. My summary records the Q1–Q8 and Q10 conclusions only as "determined," without the answers, and it doesn't preserve the question wording. I'd need you to resend the list to answer them accurately.

## Q9

Yes. `feat-app-util-new` feeds both decisions, though `dec-app-cutoff-v4` reaches it only through a chain. `dec-app-no-gbm` rests on it via `exp-504` → `app-gbm-v1` → `app-scorecard-v3` → `feat-app-util-new`. `dec-app-cutoff-v4` rests on it via `app-scorecard-v4` → `app-gbm-v2` → `app-gbm-v1` → `app-scorecard-v3` → `feat-app-util-new`. `dec-app-cutoff-v3` and `dec-app-rebuild-v4` also depend on it, directly or through `app-scorecard-v3`.

Notes: memory/work/feat-app-util-new.md, memory/work/app-scorecard-v3.md, memory/work/app-gbm-v1.md, memory/work/app-gbm-v2.md, memory/work/app-scorecard-v4.md, memory/work/exp-504-application-scorecard.md, memory/work/dec-app-no-gbm.md, memory/work/dec-app-cutoff-v3.md, memory/work/dec-app-cutoff-v4.md, memory/work/dec-app-rebuild-v4.md, memory/work/find-app-gini-v3-drift.md