# Minimal Reproduction

Fastest path to verify the key experimental results without compiling the paper.

## Requirements

Python 3.11, numpy, pandas, pyyaml, pytest.

```bash
pip install numpy pandas pyyaml pytest
```

## Steps

```bash
# 1. Generate synthetic datasets
python scripts/generate-synthetic-telemetry.py

# 2. Validate structural integrity
python scripts/validate-reproducibility.py
python scripts/validate-artifacts.py

# 3. Run structural tests
pytest -q tests/test_reproducibility_yaml.py tests/test_artifact_index.py \
       tests/test_experiment_index.py tests/test_no_sensitive_data.py

# 4. Inspect E01 results
cat experiments/E01-kdd-governance-traceability/evidence.json
```

## Expected Output

E01 evidence.json should show:
- `baseline_mean`: ~0.408
- `variant_mean`: ~0.941
- `significant`: true
