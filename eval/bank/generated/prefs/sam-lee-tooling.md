---
updated: 2026-02-09
---
# Sam Lee uses uv for environments, pins versions in pyproject, and writes new notebooks in polars
- Environments are made with `uv`; every dependency is pinned in `pyproject.toml` with an exact version.
- New notebooks use polars for dataframe work. pandas is allowed only in legacy notebooks that already use it.
- Sam does not accept a notebook that depends on a package not listed in `pyproject.toml`.
