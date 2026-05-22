# Artifact Evaluation Checklist

## Availability

- [x] All artefacts are in this repository
- [x] Repository is self-contained
- [x] No external service required for core reproduction
- [x] All datasets are synthetic and publicly shareable
- [x] No credentials or secrets required

## Functionality

- [x] `make setup` installs all Python dependencies
- [x] `make generate-data` produces synthetic datasets
- [x] `make generate-tables` produces LaTeX tables
- [x] `make generate-figures` produces PDF figures
- [x] `make test` runs all tests
- [x] `make validate` checks reproducibility metadata
- [ ] `make build-paper` produces PDF (requires LaTeX installation)

## Reproducibility

- [x] Experiments have config files with fixed seeds
- [x] Results are deterministic given the same seed
- [x] Checksums are computed by `scripts/compute-checksums.py`
- [x] Dataset cards document all datasets
- [x] Artifact index documents all generated artefacts
- [x] Docker environment provides complete isolation

## Documentation

- [x] README with quick start
- [x] Reproducibility protocol
- [x] Reviewer guide
- [x] Step-by-step reproduction instructions
- [x] Expected outputs documented
