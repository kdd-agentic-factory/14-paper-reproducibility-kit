# Kubernetes Reproduction

This document describes how to reproduce the experiments in Kubernetes.

## Prerequisites

- A Kubernetes cluster with sufficient CPU, memory, and storage.
- `kubectl` configured for the target namespace.
- Container images built and pushed to an accessible registry.

## Deployment Flow

1. Create or select a namespace for the experiment.
2. Apply configuration maps and secrets.
3. Launch jobs for each experiment condition.
4. Collect logs, metrics, and artifacts.
5. Export final results to `results/`.

## Template Commands

```bash
kubectl create namespace agentic-factory
kubectl apply -n agentic-factory -f k8s/
kubectl get jobs -n agentic-factory
kubectl logs -n agentic-factory job/<job-name>
```

## Reporting

For each Kubernetes run, record cluster type, node specification, image digest,
namespace, job manifest version, start time, end time, and output path.
