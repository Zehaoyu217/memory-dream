I can't finish the ten answers because the questions aren't in my context. The summary lists the status of Q1–Q10 but doesn't include the questions, and I don't have them anywhere else. If you paste them again, I'll pick up Q3, Q5, Q8 and Q9 and the rest.

The last lookup traced the chatbot and call-linkage notes, which may help with those four:

- **Metric definitions:** `dec-cb-metric-24h` builds on `ds-cb-call-linkage` and the finding that containment looks safe. `dec-cb-metric-48h` builds on the containment-definition sensitivity finding (`fnd-cb-def-sensitivity`) and the repeat-contact finding under v1. `dec-cb-rollout-60` uses the 48-hour definition.
- **Handoff rule:** `dec-cb-handoff-v2` builds on `feat-cb-handoff-rule-v2` and `fnd-cb-repeat-contact`.
- **Volume effect:** `fnd-cb-volume-shift` relies on the chat-to-call linkage on caller key and a randomised call-volume A/B test.
- **Prior-call features:** `feat-cb-prior-calls-v1` and `exp-307-chatbot-deflection` both build on `ds-cb-call-linkage`.

I haven't checked which decision notes supersede which, so treat the 24-hour versus 48-hour ordering as unconfirmed. No files have been changed. This session has no commits or pull requests, so the attribution reminder doesn't apply yet.