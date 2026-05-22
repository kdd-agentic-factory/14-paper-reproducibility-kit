from pathlib import Path


def list_dataset_cards() -> list[Path]:
    return sorted(Path("datasets").rglob("dataset-card.md"))


def check_all_cards_exist(dataset_index: list[dict]) -> list[str]:
    errors: list[str] = []
    for entry in dataset_index:
        card = Path(entry["dataset_card"])
        if not card.exists():
            errors.append(f"Missing dataset card: {entry['dataset_card']}")
    return errors
