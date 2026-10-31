---
updated: 2026-03-03
from: [howto/recall-at-k-definition]
---
# Q: Why does recall@10 differ between the deck and the notebook? A: The deck used all positives, the notebook only scored positives.
The retention model on the 2025q4 holdout shows recall@10 of 0.37 in the deck and 0.41 in the notebook. The deck counted positives with no bureau pull in the denominator.
Agreed with Alex Chen on 2026-03-03 that the deck will be regenerated on the scored population. Sources: `reports/retention_q4_deck.pptx` and `notebooks/recall_check.ipynb`.
