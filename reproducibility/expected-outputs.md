# Expected Outputs

After running `make reproduce-all` or the Docker equivalent, the following
files should exist:

## Datasets

- `datasets/synthetic-telemetry/synthetic-session-fp1.csv` — 5000 rows
- `datasets/synthetic-telemetry/synthetic-session-fp2.csv` — 5000 rows
- `datasets/workflow-runs/workflow-runs-v1.jsonl` — 500 lines

## Tables

- `paper/tables/experiment-summary.tex`
- `paper/tables/metrics-catalog.tex`

## Figures

- `paper/figures/results-summary-restored.pdf`
- `paper/figures/experimental-design.pdf`

## Paper

- `build/main.pdf` — compiled PDF (requires LaTeX)

## Validation

- `reproducibility/checksums.sha256` — SHA-256 hashes of all tracked files

## Verification commands

```bash
python scripts/validate-reproducibility.py  # should print: passed
python scripts/validate-artifacts.py        # should print: passed
pytest -q tests                             # should show: all passed
```
