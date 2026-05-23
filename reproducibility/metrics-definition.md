# Metrics Definition

Paper: *Structural optimization principles for edge AI in motorsport telemetry*
DOI: [10.1038/s41598-026-49736-0](https://doi.org/10.1038/s41598-026-49736-0)

---

## Paper-Specific Metrics

### Digital Factor of Safety (FoS_dig)

- **Name:** Digital Factor of Safety
- **Purpose:** Quantify the perplexity margin before a quantised model exceeds the
  acceptance boundary — the digital analogue of the structural Factor of Safety.
- **Formula:**

  ```
  FoS_dig = PPL_collapse / PPL_quant
  ```

  where:
  - `PPL_base` = perplexity of the FP16 reference model (baseline = 1.0 normalised)
  - `PPL_quant` = perplexity of the quantised model under evaluation
  - `PPL_collapse` = acceptance boundary perplexity (default: `1.10 × PPL_base`)

- **Unit:** dimensionless ratio
- **Acceptance criterion:** `FoS_dig ≥ 1.0`
- **Input data:** perplexity measurements from calibration dataset (e.g. WikiText-2)
- **Interpretation:** Values above 1.0 indicate the quantised model operates inside the
  safe envelope; values below 1.0 indicate collapse beyond the threshold.
- **Implementation:** `08-experimentation-lab/metrics/digital_factor_of_safety.py`

| Operating point      | PPL ratio | FoS_dig | Accepted |
|----------------------|-----------|---------|----------|
| fp16_32b_baseline    | 1.000     | 1.100   | No (not edge-deployable due to VRAM) |
| int8_32b_balanced    | 1.035     | 1.063   | No (exceeds 24 GB edge constraint) |
| int4_32b_trackside   | 1.072     | 1.026   | **Yes** |

---

### Intelligence-per-Watt (IPW)

- **Name:** Intelligence-per-Watt
- **Purpose:** Energy-aware usefulness metric — ranks operating points by the useful
  inference throughput they produce per watt of steady-state power.
- **Formula:**

  ```
  IPW = Throughput / Power       if FoS_dig >= 1.0
  IPW = 0                         if FoS_dig < 1.0
  ```

  where:
  - `Throughput` = tokens per second (tok/s)
  - `Power` = steady-state GPU power draw (W)

- **Unit:** tok / (s · W)
- **Gating:** operating points that fail the FoS_dig gate receive IPW = 0,
  preventing collapsed configurations from ranking highly.
- **Input data:** throughput from `nvidia-smi` / vLLM benchmarks; power from RAPL / IPMI.
- **Interpretation:** Higher IPW → better energy efficiency for a given quality constraint.
- **Implementation:** `08-experimentation-lab/metrics/intelligence_per_watt.py`

| Operating point      | Throughput (tok/s) | Power (W) | IPW    |
|----------------------|--------------------|-----------|--------|
| fp16_32b_baseline    | 26.0               | 295       | 0.0881 |
| int8_32b_balanced    | 44.2               | 218       | 0.2028 |
| int4_32b_trackside   | 69.9               | 165       | **0.4236** |

---

### K ↔ H Correspondence

The paper's core contribution is the mapping between:

| Structural domain                   | Digital domain                         |
|-------------------------------------|----------------------------------------|
| Stiffness matrix **K**              | Loss Hessian **H**                     |
| Element strain-energy sensitivity   | Hessian-weighted activation magnitude  |
| BESO binary element removal         | GPTQ/AWQ weight quantisation assignment |
| Structural FoS = σ_yield / σ_max    | FoS_dig = PPL_collapse / PPL_quant     |

BESO data: `14-paper-reproducibility-kit/data/beso_upright_stages.json`

---

## Platform Agentic Metrics

### Task Completion Rate
- **Formula:** completed tasks / total tasks
- **Unit:** ratio [0, 1]

### Tool Selection Precision
- **Formula:** correct tool selections / total tool calls
- **Unit:** ratio [0, 1]

### Skill Reuse Ratio
- **Formula:** invocations of reused skills / total skill invocations
- **Unit:** ratio [0, 1]

### Groundedness Score
- **Formula:** responses with evidence / total responses
- **Unit:** ratio [0, 1]

### Citation Coverage
- **Formula:** cited facts / total verifiable facts
- **Unit:** ratio [0, 1]

### KDD Traceability Score
- **Formula:** stages with audit trail / total KDD stages
- **Unit:** ratio [0, 1]

### Agentic Factor of Safety (platform)
- **Formula:** safe autonomous completions / total completions
- **Unit:** ratio [0, 1]
- **Note:** distinct from the paper's FoS_dig — measures agent-level safety, not
  quantisation integrity.

---

## Reproduction Verification

Run the paper metric verification:

```bash
cd 08-experimentation-lab
python -m metrics.ptq_benchmark
```

Expected output confirms all three paper operating points within ±0.001 tolerance.
