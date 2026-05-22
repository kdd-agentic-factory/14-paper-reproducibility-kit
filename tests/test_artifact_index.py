from pathlib import Path
import yaml


def test_artifact_index_exists():
    assert Path("artifacts/artifact-index.yaml").exists()


def test_artifacts_have_required_fields():
    data = yaml.safe_load(
        Path("artifacts/artifact-index.yaml").read_text(encoding="utf-8")
    )
    artifacts = data.get("artifacts", [])
    assert len(artifacts) > 0, "artifact-index.yaml contains no artifacts"

    required = ["id", "type", "title", "path", "source_repository"]
    for artifact in artifacts:
        for field in required:
            assert field in artifact, f"Artifact {artifact.get('id', '?')} missing '{field}'"


def test_artifact_ids_are_unique():
    data = yaml.safe_load(
        Path("artifacts/artifact-index.yaml").read_text(encoding="utf-8")
    )
    ids = [a["id"] for a in data.get("artifacts", [])]
    assert len(ids) == len(set(ids)), "Duplicate artifact IDs found"
