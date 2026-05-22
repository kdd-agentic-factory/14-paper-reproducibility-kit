# Full Reproduction

Complete instructions to reproduce all paper artefacts including the compiled PDF.

## Option A: Docker (recommended)

```bash
docker compose -f docker-compose.repro.yml up --build
```

This runs everything inside a pre-built environment with Python 3.11 and TeX Live.

## Option B: Native

### Prerequisites

- Python 3.11
- TeX Live full installation with latexmk

### Steps

```bash
make setup
make reproduce-all
```

This executes:
1. `generate-data` — synthetic datasets
2. `generate-tables` — LaTeX tables
3. `generate-figures` — PDF figures
4. `build-paper` — compiled PDF at `build/main.pdf`
5. `validate` — checksums and metadata validation

## Verification

```bash
make test
```

All tests should pass. The compiled PDF is at `build/main.pdf`.
