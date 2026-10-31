---
from: [ds-cc-tickets-raw]
updated: 2025-12-02
---
# Sentence embedding of ticket text, 384 dimensions from a small multilingual encoder
Mean-pooled over tokens, computed once per ticket and cached in the feature store.
Used as the frozen-encoder comparison and as the input to the fine-tuning ablation in cc-ft-v1.
