---
updated: 2025-11-11
---
# Aisha Khan wants training runs logged as JSON lines, one file per run
- Each training run writes one `run-<date>-<seq>.jsonl` file, one JSON object per line (step, metric, value, timestamp).
- Human-readable summaries are generated from the JSONL and never written by hand.
- Logs are kept 400 days in the shared MLOps bucket.
