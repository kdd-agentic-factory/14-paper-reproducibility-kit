from pathlib import Path
import yaml


class ArtifactIndex:
    def __init__(self, path: str = "artifacts/artifact-index.yaml") -> None:
        self._path = Path(path)
        self._data: dict = {}

    def load(self) -> None:
        self._data = yaml.safe_load(self._path.read_text(encoding="utf-8"))

    def artifacts(self) -> list[dict]:
        return self._data.get("artifacts", [])

    def by_id(self, artifact_id: str) -> dict | None:
        return next((a for a in self.artifacts() if a["id"] == artifact_id), None)

    def by_type(self, artifact_type: str) -> list[dict]:
        return [a for a in self.artifacts() if a.get("type") == artifact_type]
