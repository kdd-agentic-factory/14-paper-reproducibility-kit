from pathlib import Path
import yaml


def test_reproducibility_yaml_exists():
    assert Path("reproducibility.yaml").exists()


def test_reproducibility_yaml_has_required_sections():
    data = yaml.safe_load(Path("reproducibility.yaml").read_text(encoding="utf-8"))
    for section in ("paper", "environment", "datasets", "experiments", "outputs"):
        assert section in data, f"Missing section: {section}"


def test_paper_section_has_required_fields():
    data = yaml.safe_load(Path("reproducibility.yaml").read_text(encoding="utf-8"))
    paper = data["paper"]
    for field in ("title", "version", "status", "main_file"):
        assert field in paper, f"Missing paper field: {field}"


def test_datasets_have_required_fields():
    data = yaml.safe_load(Path("reproducibility.yaml").read_text(encoding="utf-8"))
    for ds in data.get("datasets", []):
        assert "id" in ds
        assert "path" in ds
        assert "classification" in ds


def test_experiments_have_required_fields():
    data = yaml.safe_load(Path("reproducibility.yaml").read_text(encoding="utf-8"))
    for exp in data.get("experiments", []):
        assert "id" in exp
        assert "path" in exp
        assert "source_repository" in exp
