# Reproducibility Protocol

## Purpose

This document defines the steps required to fully reproduce the paper's results
from scratch using only the contents of this repository.

## Prerequisites

- Python 3.11
- TeX Live (full installation) with `latexmk`
- 16 GB RAM recommended
- Internet connection for first-time dependency installation only

OR

- Docker Engine >= 24.0 (recommended for self-contained reproduction)

## Reproduction Steps

### Option A: Native (Python + LaTeX)

```bash
make setup
make generate-data
make generate-tables
make generate-figures
make build-paper
make validate
make test
```

### Option B: Docker (recommended)

```bash
docker compose -f docker-compose.repro.yml up --build
```

## Expected Outputs

| Output | Path |
|--------|------|
| Compiled paper PDF | `build/main.pdf` |
| Synthetic telemetry FP1 | `datasets/synthetic-telemetry/synthetic-session-fp1.csv` |
| Synthetic telemetry FP2 | `datasets/synthetic-telemetry/synthetic-session-fp2.csv` |
| Workflow runs log | `datasets/workflow-runs/workflow-runs-v1.jsonl` |
| Experiment summary table | `paper/tables/experiment-summary.tex` |
| Results summary figure | `paper/figures/results-summary.pdf` |
| Checksums | `reproducibility/checksums.sha256` |

## Verification

After reproduction, run:

```bash
make test
python scripts/validate-reproducibility.py
python scripts/validate-artifacts.py
```

All tests and validations should pass.
