# Reproducibility Guidelines

## Core Rules

1. **Every table has a source.** All `.tex` tables in `paper/tables/` must be generated
   by a script in `scripts/` and registered in `artifacts/artifact-index.yaml`.

2. **Every figure has a source.** All `.pdf` figures in `paper/figures/` must be generated
   by `scripts/generate-figures.py`.

3. **Every dataset has a card.** All directories under `datasets/` must contain a
   `dataset-card.md` with classification, generation method, and limitations.

4. **Every experiment is indexed.** All experiment directories must appear in
   `experiments/experiment-index.yaml`.

5. **No manual results.** Do not edit `results.csv` files by hand. Re-run the
   experiment and regenerate.

6. **Checksums after changes.** Run `make validate` after any change to datasets,
   tables, or figures.

## Adding a New Experiment

1. Create `experiments/E<N>-<slug>/config.yaml`.
2. Add the experiment to `experiments/experiment-index.yaml`.
3. Add the experiment to `reproducibility.yaml`.
4. Run the experiment and save results to `results.csv`.
5. Generate `table.tex` and `evidence.json`.
6. Update `paper/sections/10-results.tex`.
7. Run `make test` and `make validate`.
