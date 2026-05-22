# 14-paper-reproducibility-kit

Reproducibility kit for the KDD-governed agentic race engineering platform paper.

This repository contains:

- the LaTeX paper manuscript,
- experimental results and configurations,
- synthetic datasets,
- analysis notebooks,
- reproducibility scripts,
- tables and figures (generated),
- architecture diagrams,
- workflow definitions,
- security and compliance evidence,
- Docker/Kubernetes deployment summaries,
- CI/CD release evidence,
- reviewer instructions.

## Quick Start

```bash
make setup
make build-paper
make reproduce-all
```

## Main Outputs

- compiled paper PDF (`build/main.pdf`),
- experiment tables (`paper/tables/`),
- generated figures (`paper/figures/`),
- reproducibility report (`reproducibility/reproducibility-report.md`),
- review package (`dist/review-package.zip`),
- artifact index (`artifacts/artifact-index.yaml`).

## Structure

```text
14-paper-reproducibility-kit/
├── paper/                  LaTeX manuscript
├── artifacts/              generated artefacts with provenance
├── experiments/            experiment results and evidence
├── datasets/               synthetic and anonymised datasets
├── notebooks/              analysis notebooks
├── scripts/                generation and validation scripts
├── src/paper_kit/          Python library for kit utilities
├── results/                raw and processed results
├── reproducibility/        protocol and checksums
├── review-package/         reviewer-ready package
├── docs/                   extended documentation
└── tests/                  structure and integrity tests
```

## Building the Paper

```bash
make build-paper
```

Requires a TeX Live installation with `latexmk` or the Docker environment.

## Reproducing Results

```bash
make generate-data
make generate-tables
make generate-figures
make validate
```

## Running Notebooks

Open notebooks in Jupyter after `make setup`:

```bash
jupyter lab notebooks/
```

## Executing Tests

```bash
make test
```

## Creating the Review Package

```bash
make package-review
```

## Docker Reproduction

```bash
docker compose -f docker-compose.repro.yml up --build
```

This command runs `make reproduce-all` inside a fully specified environment
including Python 3.11 and TeX Live.

## Citation

See [CITATION.cff](CITATION.cff) for citation metadata.
