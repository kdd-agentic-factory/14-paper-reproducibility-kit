from pathlib import Path
import sys
import yaml

REQUIRED_FIELDS = ["id", "type", "title", "path", "source_repository", "generation_script"]


def validate_artifact_index() -> list[str]:
    errors: list[str] = []
    path = Path("artifacts/artifact-index.yaml")

    if not path.exists():
        return ["Missing artifacts/artifact-index.yaml"]

    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    artifacts = data.get("artifacts", [])

    if not artifacts:
        errors.append("artifact-index.yaml contains no artifacts")

    for artifact in artifacts:
        for field in REQUIRED_FIELDS:
            if field not in artifact:
                errors.append(f"Artifact {artifact.get('id', '?')} missing field '{field}'")

    return errors


def main() -> None:
    errors = validate_artifact_index()

    if errors:
        print("Artifact validation FAILED:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("Artifact validation passed.")


if __name__ == "__main__":
    main()
