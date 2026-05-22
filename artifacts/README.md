# artifacts/

Generated artefacts with provenance metadata.

Every artefact in this directory is registered in `artifact-index.yaml` with:
- unique artifact ID,
- type (figure, table, dataset, workflow, etc.),
- source repository,
- generation script,
- creation timestamp,
- checksum (computed by `scripts/compute-checksums.py`).

Do not add artefacts manually without updating the index and recording provenance.

## Subdirectories

| Directory | Contents |
|-----------|----------|
| `architecture/` | Architecture diagrams (Mermaid, PlantUML) |
| `workflows/` | Selected workflow YAML definitions |
| `security/` | Security control catalog and risk register |
| `observability/` | Metrics snapshots, Prometheus exports, trace examples |
| `ci-cd/` | Release evidence, SBOM summaries, CI results |
| `deployment/` | Docker/Kubernetes deployment summaries |
