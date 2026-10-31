---
from: [ds-cc-tickets-raw]
updated: 2025-10-01
---
# TF-IDF over complaint text: word 1 to 2 grams (50,000) plus char 3 to 5 grams (100,000)
Sublinear tf, fitted on training tickets only. Feature names in the repo: cc_word12, cc_char35.
Input to cc-logreg-v1. Not used by the fine-tuned encoder, which reads raw text.
