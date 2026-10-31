---
from: [ds-disp-disputes]
updated: 2026-02-05
---
# feat-disp-reason-text: TF-IDF of dispute description, bigrams, 4,000 columns
TF-IDF over 1-2 word grams of the free-text description, vocabulary fit on 2025 disputes only.
Capped at 4,000 columns; lowercase, digits removed.
Only input of disp-lgbm-v1; kept in every later version.
