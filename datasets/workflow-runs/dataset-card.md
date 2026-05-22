# Dataset Card — Workflow Runs v1

## Dataset ID

workflow-runs-v1

## Description

Synthetic log of agentic workflow executions used to evaluate workflow
traceability, audit coverage, and skill reuse metrics.

## Classification

Public synthetic.

## Contents

JSONL format. Each line is a workflow run record with fields:
- `run_id`, `workflow_id`, `started_at`, `finished_at`,
- `steps_completed`, `steps_total`, `tool_calls`,
- `audit_entries`, `skill_invocations`, `governance_checks_passed`.

## Sensitive Data

None. All fields are synthetically generated.
