from pathlib import Path
import json
import numpy as np
import pandas as pd


def generate_synthetic_session(n: int = 5000, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    ts_micro = np.arange(n) * 10_000
    lap_progress = np.linspace(0, 10, n)

    gps_speed = 180 + 40 * np.sin(lap_progress * 2 * np.pi) + rng.normal(0, 2, n)
    wheel_speed_r = gps_speed * (1 + np.clip(0.02 + 0.00002 * np.arange(n), 0, 0.15))
    wheel_speed_f = gps_speed * (1 + rng.normal(0, 0.005, n))

    imu_roll = 55 * np.sin(lap_progress * 2 * np.pi) + rng.normal(0, 2, n)
    tps = np.clip(50 + 40 * np.sin(lap_progress * 2 * np.pi + 1.5), 0, 100)
    brake_press_front = np.clip(20 * np.sin(lap_progress * 2 * np.pi + 3.0), 0, 20)

    tire_temp_surface = (
        85
        + 25 * np.clip(np.sin(lap_progress * 2 * np.pi), 0, 1)
        + 0.003 * np.arange(n)
    )
    tire_temp_carcass = 80 + 0.7 * (tire_temp_surface - 80)

    return pd.DataFrame({
        "ts_micro": ts_micro,
        "gps_lat": 37.0 + 0.001 * np.sin(lap_progress),
        "gps_lon": -3.0 + 0.001 * np.cos(lap_progress),
        "imu_yaw": rng.normal(0, 1, n),
        "imu_pitch": rng.normal(0, 1, n),
        "imu_roll": imu_roll,
        "tps": tps,
        "brake_press_front": brake_press_front,
        "brake_press_rear": brake_press_front * 0.15,
        "susp_travel_f": 40 + brake_press_front * 1.5 + rng.normal(0, 1, n),
        "susp_travel_r": 35 + tps * 0.2 + rng.normal(0, 1, n),
        "tire_temp_surface": tire_temp_surface,
        "tire_temp_carcass": tire_temp_carcass,
        "wheel_speed_f": wheel_speed_f,
        "wheel_speed_r": wheel_speed_r,
        "gps_speed": gps_speed,
        "rpm": 12000 + tps * 40 + rng.normal(0, 100, n),
        "gear": np.clip((gps_speed // 45).astype(int), 1, 6),
        "tcs_level": np.where(wheel_speed_r > gps_speed * 1.08, 5, 3),
        "engine_map": "Mapping 1",
    })


def generate_workflow_runs(n: int = 500, seed: int = 42) -> list[dict]:
    rng = np.random.default_rng(seed)
    workflows = ["pre-grand-prix", "run-setup-what-if", "copilot-evidence-report",
                 "generate-paper-section", "create-new-feature"]
    records = []
    for i in range(n):
        wf = workflows[rng.integers(0, len(workflows))]
        steps_total = rng.integers(3, 8)
        steps_completed = rng.integers(steps_total - 1, steps_total + 1)
        tool_calls = int(rng.integers(1, 12))
        records.append({
            "run_id": f"run-{i:04d}",
            "workflow_id": wf,
            "started_at": f"2026-05-22T{10 + i // 60:02d}:{i % 60:02d}:00Z",
            "finished_at": f"2026-05-22T{10 + (i + 1) // 60:02d}:{(i + 1) % 60:02d}:00Z",
            "steps_completed": int(min(steps_completed, steps_total)),
            "steps_total": int(steps_total),
            "tool_calls": tool_calls,
            "audit_entries": tool_calls,
            "skill_invocations": int(rng.integers(0, 4)),
            "governance_checks_passed": bool(rng.random() > 0.05),
        })
    return records


def generate_rag_benchmark(n: int = 200, seed: int = 42) -> list[dict]:
    rng = np.random.default_rng(seed)
    topics = ["tyre degradation", "suspension setup", "traction control", "braking point",
              "lean angle", "fuel strategy", "engine mapping", "wing setting"]
    records = []
    for i in range(n):
        topic = topics[rng.integers(0, len(topics))]
        n_citations = int(rng.integers(1, 5))
        groundedness = float(np.clip(rng.normal(0.75, 0.1), 0, 1))
        records.append({
            "query_id": f"q-{i:04d}",
            "query": f"What is the optimal approach for {topic} in dry conditions?",
            "expected_citations": n_citations,
            "retrieved_chunks": int(rng.integers(3, 8)),
            "generated_answer": f"Based on retrieved context for {topic}...",
            "groundedness_score": round(groundedness, 3),
            "citation_coverage": round(float(np.clip(rng.normal(0.72, 0.12), 0, 1)), 3),
        })
    return records


def generate_copilot_prompts(n: int = 300, seed: int = 42) -> list[dict]:
    rng = np.random.default_rng(seed)
    records = []
    for i in range(n):
        condition = "variant" if i % 2 == 0 else "baseline"
        evidence_count = int(rng.integers(2, 6)) if condition == "variant" else 0
        records.append({
            "prompt_id": f"p-{i:04d}",
            "prompt": f"Analyse telemetry session {i} and recommend setup changes.",
            "condition": condition,
            "response": f"Recommendation based on {'evidence' if condition == 'variant' else 'general knowledge'}.",
            "evidence_count": evidence_count,
            "confidence_score": round(float(np.clip(rng.normal(0.78, 0.1), 0, 1)), 3),
            "quality_score": round(float(np.clip(rng.normal(0.72, 0.12), 0, 1)), 3),
        })
    return records


def generate_what_if_scenarios(n: int = 150, seed: int = 42) -> list[dict]:
    rng = np.random.default_rng(seed)
    records = []
    for i in range(n):
        delta_ms = float(rng.normal(-50, 200))
        twin_pass = delta_ms < 0 or abs(delta_ms) < 100
        records.append({
            "scenario_id": f"s-{i:04d}",
            "setup_delta": {
                "ride_height_mm": round(float(rng.normal(0, 3)), 1),
                "spring_rate_pct": round(float(rng.normal(0, 5)), 1),
                "damper_clicks": int(rng.integers(-3, 4)),
            },
            "predicted_lap_delta_ms": round(delta_ms, 1),
            "twin_pass": twin_pass,
            "twin_alternative": None if twin_pass else {"ride_height_mm": 0.0},
            "safety_flag": not twin_pass and abs(delta_ms) > 300,
        })
    return records


def main() -> None:
    out = Path("datasets/synthetic-telemetry")
    out.mkdir(parents=True, exist_ok=True)

    fp1 = generate_synthetic_session(n=5000, seed=42)
    fp1.to_csv(out / "synthetic-session-fp1.csv", index=False)
    print(f"Generated {out}/synthetic-session-fp1.csv with {len(fp1)} rows")

    fp2 = generate_synthetic_session(n=5000, seed=43)
    fp2.to_csv(out / "synthetic-session-fp2.csv", index=False)
    print(f"Generated {out}/synthetic-session-fp2.csv with {len(fp2)} rows")

    wf_out = Path("datasets/workflow-runs")
    wf_out.mkdir(parents=True, exist_ok=True)
    runs = generate_workflow_runs(n=500, seed=42)
    with open(wf_out / "workflow-runs-v1.jsonl", "w", encoding="utf-8") as f:
        for r in runs:
            f.write(json.dumps(r) + "\n")
    print(f"Generated {wf_out}/workflow-runs-v1.jsonl with {len(runs)} records")

    rag_out = Path("datasets/rag-benchmarks")
    rag_out.mkdir(parents=True, exist_ok=True)
    rag = generate_rag_benchmark(n=200, seed=42)
    with open(rag_out / "rag-benchmark-v1.jsonl", "w", encoding="utf-8") as f:
        for r in rag:
            f.write(json.dumps(r) + "\n")
    print(f"Generated {rag_out}/rag-benchmark-v1.jsonl with {len(rag)} records")

    cop_out = Path("datasets/copilot-prompts")
    cop_out.mkdir(parents=True, exist_ok=True)
    cop = generate_copilot_prompts(n=300, seed=42)
    with open(cop_out / "copilot-prompts-v1.jsonl", "w", encoding="utf-8") as f:
        for r in cop:
            f.write(json.dumps(r) + "\n")
    print(f"Generated {cop_out}/copilot-prompts-v1.jsonl with {len(cop)} records")

    sim_out = Path("datasets/simulation-scenarios")
    sim_out.mkdir(parents=True, exist_ok=True)
    sim = generate_what_if_scenarios(n=150, seed=42)
    with open(sim_out / "what-if-scenarios-v1.jsonl", "w", encoding="utf-8") as f:
        for r in sim:
            f.write(json.dumps(r) + "\n")
    print(f"Generated {sim_out}/what-if-scenarios-v1.jsonl with {len(sim)} records")


if __name__ == "__main__":
    main()
