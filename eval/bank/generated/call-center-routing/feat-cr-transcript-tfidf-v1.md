---
from: [ds-cr-calls]
updated: 2025-12-08
---
# TF-IDF of the first 30 seconds of ASR transcript, reduced to 200 SVD dimensions, is the main text signal
Vocabulary of 20,000 unigrams and bigrams, min_df 5, sublinear tf. SVD to 200 dimensions, fitted on the training split only.
The full-transcript version gains only +0.004 macro F1 at four times the cost (exp-102), so the 30-second window stays.
Built by Sam Lee (ML engineering) as feat_tfidf30 in the routing repo.
