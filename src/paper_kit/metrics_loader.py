from pathlib import Path
import json
import csv


def load_experiment_results(experiment_id: str) -> list[dict]:
    path = Path("experiments") / experiment_id / "results.csv"
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_evidence(experiment_id: str) -> dict:
    path = Path("experiments") / experiment_id / "evidence.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))
