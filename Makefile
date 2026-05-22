.PHONY: setup build-paper clean-paper generate-data generate-tables \
        generate-figures validate reproduce-all package-review test

setup:
	pip install -r requirements.txt

generate-data:
	python scripts/generate-synthetic-telemetry.py

generate-tables:
	python scripts/generate-tables.py

generate-figures:
	python scripts/generate-figures.py

build-paper:
	mkdir -p build
	cd paper && latexmk -pdf -interaction=nonstopmode -outdir=../build main.tex

clean-paper:
	cd paper && latexmk -C -outdir=../build
	rm -rf build

validate:
	python scripts/validate-reproducibility.py
	python scripts/validate-artifacts.py
	python scripts/compute-checksums.py

reproduce-all: generate-data generate-tables generate-figures build-paper validate

package-review:
	bash scripts/export-paper-package.sh

test:
	pytest -q tests
