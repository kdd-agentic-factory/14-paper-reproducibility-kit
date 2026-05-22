# Dataset Card — RAG Benchmark v1

## Dataset ID

rag-benchmark-v1

## Description

Synthetic query-answer pairs for evaluating retrieval-augmented generation
groundedness and citation coverage in the race engineering domain.

## Classification

Public synthetic.

## Contents

JSONL format. Each line contains:
- `query_id`, `query`, `expected_citations`, `retrieved_chunks`,
- `generated_answer`, `groundedness_score`, `citation_coverage`.

## Sensitive Data

None. Queries and answers are synthetically constructed from race engineering
terminology without real team or rider data.
