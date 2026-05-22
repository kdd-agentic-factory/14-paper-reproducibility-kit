# Reviewer Guide

Thank you for reviewing this artifact package.

## What This Package Contains

1. **LaTeX manuscript** — `paper/` directory, compilable to PDF.
2. **Synthetic datasets** — `datasets/`, no confidential data.
3. **Experiment results** — `experiments/E01-*` etc., with config, CSV results,
   and evidence JSON.
4. **Generation scripts** — `scripts/`, reproduce all datasets, tables, figures.
5. **Tests** — `tests/`, validate structural integrity.

## Quick Sanity Check (5 minutes)

```bash
pip install -r requirements.txt
python scripts/generate-synthetic-telemetry.py
python scripts/generate-tables.py
python scripts/validate-reproducibility.py
python scripts/validate-artifacts.py
pytest -q tests
```

All commands should complete without errors.

## Key Claims to Verify

| Claim | Evidence |
|-------|----------|
| Traceability score 0.94 vs 0.41 | `experiments/E01-kdd-governance-traceability/results.csv` |
| Audit coverage 0.99 with MCP | `experiments/E03-mcp-vs-direct-tools/` |
| Groundedness 0.81 with RAG | `experiments/E05-rag-cag-vs-no-rag/` |
| 23% block rate in twin | `experiments/E07-digital-twin-validation/` |

## Full Reproduction

See `full-reproduction.md` for instructions to compile the paper PDF.
