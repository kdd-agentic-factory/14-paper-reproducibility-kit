from pathlib import Path
import yaml


class ReproducibilityValidator:
    def __init__(self, root: str = ".") -> None:
        self.root = Path(root)

    def validate_reproducibility_yaml(self) -> list[str]:
        errors: list[str] = []
        path = self.root / "reproducibility.yaml"

        if not path.exists():
            return ["Missing reproducibility.yaml"]

        data = yaml.safe_load(path.read_text(encoding="utf-8"))

        for section in ("paper", "environment", "datasets", "experiments", "outputs"):
            if section not in data:
                errors.append(f"Missing section '{section}'")

        for dataset in data.get("datasets", []):
            dataset_path = self.root / dataset["path"]
            if not dataset_path.exists():
                errors.append(f"Missing dataset: {dataset['path']}")

        for experiment in data.get("experiments", []):
            experiment_path = self.root / experiment["path"]
            if not experiment_path.exists():
                errors.append(f"Missing experiment: {experiment['path']}")

        return errors

    def validate_artifact_index(self) -> list[str]:
        errors: list[str] = []
        path = self.root / "artifacts" / "artifact-index.yaml"

        if not path.exists():
            return ["Missing artifacts/artifact-index.yaml"]

        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        required = ["id", "type", "title", "path", "source_repository"]

        for artifact in data.get("artifacts", []):
            for field in required:
                if field not in artifact:
                    errors.append(
                        f"Artifact {artifact.get('id', '?')} missing field '{field}'"
                    )

        return errors
