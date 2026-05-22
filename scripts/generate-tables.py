from pathlib import Path


def rows_to_latex_table(headers: list[str], rows: list[list[str]],
                        caption: str, label: str) -> str:
    col_spec = "l" * len(headers)
    header_row = " & ".join(f"\\textbf{{{h}}}" for h in headers) + " \\\\"
    data_rows = "\n".join(" & ".join(str(c) for c in row) + " \\\\" for row in rows)

    return (
        f"\\begin{{table}}[ht]\n"
        f"\\centering\n"
        f"\\caption{{{caption}}}\n"
        f"\\label{{{label}}}\n"
        f"\\begin{{tabular}}{{{col_spec}}}\n"
        f"\\toprule\n"
        f"{header_row}\n"
        f"\\midrule\n"
        f"{data_rows}\n"
        f"\\bottomrule\n"
        f"\\end{{tabular}}\n"
        f"\\end{{table}}\n"
    )


def generate_experiment_summary() -> None:
    headers = ["ID", "Experiment", "Hypothesis", "Primary Metric"]
    rows = [
        ["E01", "KDD governance traceability", "H1", "Traceability score"],
        ["E02", "SDD vs free generation", "H2", "SDD compliance rate"],
        ["E03", "MCP vs direct tools", "H3", "Audit coverage"],
        ["E04", "Skills vs free prompts", "H4", "Output consistency"],
        ["E05", "RAG/CAG vs no retrieval", "H5", "Groundedness"],
        ["E06", "Copilot evidence quality", "H6", "Evidence density"],
        ["E07", "Digital twin validation", "H7", "Block rate"],
        ["E08", "RCC usability", "H8", "SUS score"],
        ["E09", "End-to-end loop", "H1-H8", "Composite"],
    ]
    table = rows_to_latex_table(
        headers, rows,
        caption="Summary of experiments and primary metrics.",
        label="tab:experiment-summary",
    )
    out = Path("paper/tables/experiment-summary.tex")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(table, encoding="utf-8")
    print(f"Generated {out}")


def generate_metrics_catalog() -> None:
    headers = ["Metric", "Target"]
    rows = [
        ["Traceability Score", "$> 0.90$"],
        ["SDD Compliance Rate", "$> 0.95$"],
        ["Audit Coverage", "$> 0.99$"],
        ["Evidence Density", "$> 2.0$"],
        ["Groundedness", "$> 0.75$"],
        ["Citation Coverage", "$> 0.80$"],
        ["Block Rate", "measured"],
        ["Tool Precision", "$> 0.85$"],
    ]
    table = rows_to_latex_table(
        headers, rows,
        caption="Metrics catalog with target values.",
        label="tab:metrics-catalog",
    )
    out = Path("paper/tables/metrics-catalog.tex")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(table, encoding="utf-8")
    print(f"Generated {out}")


def main() -> None:
    generate_experiment_summary()
    generate_metrics_catalog()
    print("All tables generated.")


if __name__ == "__main__":
    main()
