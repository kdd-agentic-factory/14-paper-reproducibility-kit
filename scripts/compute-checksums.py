from pathlib import Path
import hashlib

TARGET_DIRS = [
    "datasets",
    "experiments",
    "paper/tables",
    "paper/figures",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def main() -> None:
    output = Path("reproducibility/checksums.sha256")
    output.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    for target in TARGET_DIRS:
        target_path = Path(target)
        if not target_path.exists():
            continue
        for path in sorted(target_path.rglob("*")):
            if path.is_file() and not path.name.startswith("."):
                lines.append(f"{sha256(path)}  {path.as_posix()}")

    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Checksums written to {output} ({len(lines)} files)")


if __name__ == "__main__":
    main()
