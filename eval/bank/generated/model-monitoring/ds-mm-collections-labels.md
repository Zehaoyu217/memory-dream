---
from: []
updated: 2025-01-28
---
# collections.cases as the label source for the collections propensity model
Shared table owned by collections-ops. The label is a case reaching 60 days past due and then being charged off or cured, per the case outcome column.
Label lag is about 45 days, so the newest 45 days of scores have no label yet. Evaluation holdouts must end at least 45 days before the evaluation date.
