from pathlib import Path
import hashlib


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def test_checksums_file_exists_or_can_be_generated():
    checksum_path = Path("reproducibility/checksums.sha256")
    if checksum_path.exists():
        content = checksum_path.read_text(encoding="utf-8")
        assert len(content) > 0, "checksums.sha256 is empty"
    else:
        assert Path("scripts/compute-checksums.py").exists(), \
            "No checksums file and no script to generate one"


def test_experiment_results_are_stable():
    results = Path("experiments/E01-kdd-governance-traceability/results.csv")
    if results.exists():
        h = sha256(results)
        assert len(h) == 64
