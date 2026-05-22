#!/usr/bin/env bash
set -euo pipefail

echo "=== Paper Reproducibility Kit — Full Reproduction ==="

echo "--- Generating synthetic datasets ---"
python scripts/generate-synthetic-telemetry.py

echo "--- Generating tables ---"
python scripts/generate-tables.py

echo "--- Generating figures ---"
python scripts/generate-figures.py

echo "--- Validating reproducibility metadata ---"
python scripts/validate-reproducibility.py
python scripts/validate-artifacts.py

echo "--- Computing checksums ---"
python scripts/compute-checksums.py

echo "--- Building paper (requires LaTeX) ---"
mkdir -p build
cd paper && latexmk -pdf -interaction=nonstopmode -outdir=../build main.tex || \
  echo "WARNING: LaTeX build failed. Install TeX Live or use Docker."

echo "=== Reproduction complete ==="
