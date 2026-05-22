#!/usr/bin/env bash
set -euo pipefail

DIST_DIR="dist"
PACKAGE_NAME="review-package-$(date +%Y%m%d).zip"

mkdir -p "$DIST_DIR"

zip -r "$DIST_DIR/$PACKAGE_NAME" \
  paper/ \
  artifacts/ \
  experiments/ \
  datasets/ \
  reproducibility/ \
  review-package/ \
  README.md \
  CITATION.cff \
  reproducibility.yaml \
  --exclude "*.pyc" \
  --exclude "*/__pycache__/*" \
  --exclude "paper/figures/*.pdf" \
  --exclude "build/*"

echo "Review package created: $DIST_DIR/$PACKAGE_NAME"
