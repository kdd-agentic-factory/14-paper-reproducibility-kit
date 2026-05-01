# Docker Reproduction

This document describes how to reproduce the experiments using Docker.

## Prerequisites

- Docker installed and running.
- Access to the implementation repository or artifact bundle.
- Required environment variables documented in the experiment protocol.

## Build

```bash
docker build -t agentic-factory-reproduction .
```

## Run

```bash
docker run --rm \
  --env-file .env \
  -v "$(pwd)/results:/app/results" \
  agentic-factory-reproduction
```

## Expected Outputs

- Experiment logs.
- Metric files exported to `results/`.
- Figure and table assets ready for the paper.

## Notes

Record the Docker version, image digest, command used, and execution date for
each reproduced run.
