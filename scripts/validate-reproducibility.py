from pathlib import Path
import sys
import yaml


def validate_reproducibility_yaml() -> list[str]:
    errors: list[str] = []
    path = Path("reproducibility.yaml")

    if not path.exists():
        return ["Missing reproducibility.yaml"]

    data = yaml.safe_load(path.read_text(encoding="utf-8"))

    for section in ("paper", "environment", "datasets", "experiments", "outputs"):
        if section not in data:
            errors.append(f"Missing section '{section}' in reproducibility.yaml")

    for dataset in data.get("datasets", []):
        dataset_path = Path(dataset["path"])
        if not dataset_path.exists():
            errors.append(f"Missing dataset file: {dataset['path']}")

    for experiment in data.get("experiments", []):
        experiment_dir = Path(experiment["path"])
        if not experiment_dir.exists():
            errors.append(f"Missing experiment directory: {experiment['path']}")

    return errors


def main() -> None:
    errors = validate_reproducibility_yaml()

    if errors:
        print("Reproducibility validation FAILED:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("Reproducibility validation passed.")


if __name__ == "__main__":
    main()
