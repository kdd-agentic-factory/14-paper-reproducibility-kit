# Dataset Card — What-If Scenarios v1

## Dataset ID

what-if-scenarios-v1

## Description

Synthetic setup what-if scenarios used to evaluate digital twin validation
and recommendation blocking rates.

## Classification

Public synthetic.

## Contents

JSONL format. Each line contains:
- `scenario_id`, `setup_delta` (JSON), `predicted_lap_delta_ms`,
- `twin_pass` (bool), `twin_alternative` (JSON or null),
- `safety_flag` (bool).

## Sensitive Data

None. Setup deltas are constructed from realistic parameter ranges without
real team setup data.
