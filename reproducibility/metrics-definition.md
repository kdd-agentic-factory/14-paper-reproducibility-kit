# Metrics Definition

This document defines the metrics reported in the paper.

## Metric Template

For every metric, document:

- Name:
- Purpose:
- Formula:
- Unit:
- Input data:
- Aggregation:
- Interpretation:
- Known limitations:

## Candidate Metrics

### Task Completion Rate

- Purpose: measure the proportion of tasks completed successfully.
- Formula: completed tasks divided by total tasks.
- Unit: percentage.

### Time to Completion

- Purpose: measure elapsed time required to complete a task or workflow.
- Formula: end timestamp minus start timestamp.
- Unit: seconds or minutes.

### Intervention Count

- Purpose: measure how often human intervention is required.
- Formula: count of manual corrections, approvals, or restarts.
- Unit: count.

### Reproduction Success Rate

- Purpose: measure whether an experiment can be reproduced from the documented
  artifact.
- Formula: successful reproductions divided by attempted reproductions.
- Unit: percentage.

### Result Drift

- Purpose: quantify differences between original and reproduced results.
- Formula: metric-specific absolute or relative difference.
- Unit: depends on the underlying metric.
