from pathlib import Path
import hashlib


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def compute_directory_checksums(directories: list[str]) -> dict[str, str]:
    checksums: dict[str, str] = {}
    for directory in directories:
        d = Path(directory)
        if not d.exists():
            continue
        for path in sorted(d.rglob("*")):
            if path.is_file() and not path.name.startswith("."):
                checksums[path.as_posix()] = sha256(path)
    return checksums
