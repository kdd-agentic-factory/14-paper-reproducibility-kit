from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def generate_results_summary() -> None:
    experiments = ["E01\nTraceability", "E03\nAudit Cov.", "E05\nGroundedness", "E07\nBlock Rate"]
    baseline = [0.41, 0.38, 0.52, 0.0]
    variant = [0.94, 0.99, 0.81, 0.23]

    x = np.arange(len(experiments))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(x - width / 2, baseline, width, label="Baseline", color="#4e79a7", alpha=0.85)
    ax.bar(x + width / 2, variant, width, label="Variant", color="#f28e2b", alpha=0.85)

    ax.set_ylabel("Score")
    ax.set_title("Key Experiment Results: Baseline vs Variant")
    ax.set_xticks(x)
    ax.set_xticklabels(experiments)
    ax.set_ylim(0, 1.1)
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    fig.tight_layout()

    out = Path("paper/figures/results-summary.pdf")
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out)
    plt.close(fig)
    print(f"Generated {out}")


def generate_experimental_design() -> None:
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.axis("off")

    steps = [
        "Synthetic\nDataset",
        "Baseline\nCondition",
        "Variant\nCondition",
        "10 Runs\nPer Cond.",
        "Statistical\nTest",
        "Paper\nResult",
    ]
    for i, step in enumerate(steps):
        ax.annotate(
            step,
            xy=(i / (len(steps) - 1), 0.5),
            fontsize=10,
            ha="center",
            va="center",
            bbox=dict(boxstyle="round,pad=0.4", fc="#dce9f5", ec="#4e79a7", lw=1.5),
        )
        if i < len(steps) - 1:
            ax.annotate(
                "",
                xy=((i + 1) / (len(steps) - 1) - 0.03, 0.5),
                xytext=(i / (len(steps) - 1) + 0.03, 0.5),
                arrowprops=dict(arrowstyle="->", color="#4e79a7", lw=1.5),
            )

    ax.set_title("Experimental Design Pipeline", fontsize=12, fontweight="bold")
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(0, 1)
    fig.tight_layout()

    out = Path("paper/figures/experimental-design.pdf")
    fig.savefig(out)
    plt.close(fig)
    print(f"Generated {out}")


def main() -> None:
    generate_results_summary()
    generate_experimental_design()
    print("All figures generated.")


if __name__ == "__main__":
    main()
