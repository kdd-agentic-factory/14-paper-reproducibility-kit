from pathlib import Path
import yaml


def test_generated_tables_in_artifact_index():
    data = yaml.safe_load(
        Path("artifacts/artifact-index.yaml").read_text(encoding="utf-8")
    )
    table_artifacts = [a for a in data.get("artifacts", []) if a.get("type") == "table"]
    assert len(table_artifacts) > 0, "No table artifacts in artifact-index.yaml"


def test_table_artifacts_have_generation_script():
    data = yaml.safe_load(
        Path("artifacts/artifact-index.yaml").read_text(encoding="utf-8")
    )
    for artifact in data.get("artifacts", []):
        if artifact.get("type") == "table":
            assert "generation_script" in artifact, \
                f"Table artifact {artifact['id']} missing generation_script"
