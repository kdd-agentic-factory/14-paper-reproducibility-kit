from pathlib import Path


def rows_to_latex(headers: list[str], rows: list[list[str]],
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


def write_table(headers: list[str], rows: list[list[str]],
                caption: str, label: str, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rows_to_latex(headers, rows, caption, label), encoding="utf-8")
