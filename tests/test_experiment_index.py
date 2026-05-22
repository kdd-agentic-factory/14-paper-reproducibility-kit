from pathlib import Path
import yaml


def test_experiment_index_exists():
    assert Path("experiments/experiment-index.yaml").exists()


def test_experiments_have_required_fields():
    data = yaml.safe_load(
        Path("experiments/experiment-index.yaml").read_text(encoding="utf-8")
    )
    experiments = data.get("experiments", [])
    assert len(experiments) > 0

    required = ["id", "title", "hypothesis", "results_path", "table_path", "paper_section"]
    for exp in experiments:
        for field in required:
            assert field in exp, f"Experiment {exp.get('id', '?')} missing '{field}'"


def test_experiment_directories_exist():
    expected = [
        "E01-kdd-governance-traceability",
        "E02-sdd-vs-free-generation",
        "E03-mcp-vs-direct-tools",
    ]
    for exp_id in expected:
        assert Path("experiments", exp_id).is_dir(), f"Missing: experiments/{exp_id}"
