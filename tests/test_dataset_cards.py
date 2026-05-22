from pathlib import Path


def test_synthetic_telemetry_card_exists():
    assert Path("datasets/synthetic-telemetry/dataset-card.md").exists()


def test_all_dataset_directories_have_cards():
    dataset_dirs = [
        "datasets/synthetic-telemetry",
        "datasets/workflow-runs",
        "datasets/rag-benchmarks",
        "datasets/copilot-prompts",
        "datasets/simulation-scenarios",
    ]
    for d in dataset_dirs:
        card = Path(d) / "dataset-card.md"
        assert card.exists(), f"Missing dataset card: {card}"


def test_dataset_cards_have_classification():
    for card in Path("datasets").rglob("dataset-card.md"):
        content = card.read_text(encoding="utf-8")
        assert "Classification" in content or "classification" in content, \
            f"Missing classification in {card}"
