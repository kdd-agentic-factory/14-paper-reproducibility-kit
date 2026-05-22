# Dataset Card — Copilot Prompts v1

## Dataset ID

copilot-prompts-v1

## Description

Synthetic copilot prompt-response pairs used to evaluate evidence density,
groundedness, and recommendation quality across conditions.

## Classification

Public synthetic.

## Contents

JSONL format. Each line contains:
- `prompt_id`, `prompt`, `condition` (baseline/variant),
- `response`, `evidence_count`, `confidence_score`, `quality_score`.

## Sensitive Data

None. Prompts are constructed from synthetic telemetry summaries without
real team strategy or confidential setup data.
