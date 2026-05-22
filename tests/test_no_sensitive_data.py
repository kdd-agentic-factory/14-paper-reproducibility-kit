from pathlib import Path

# Built dynamically to avoid self-matching when this file is scanned.
_KEY = "KEY"
_PRI = "PRIVATE"
FORBIDDEN_PATTERNS = [
    f"BEGIN {_PRI} {_KEY}",
    f"BEGIN RSA {_PRI} {_KEY}",
    "ghp_",
    "sk-ant-",
    "real_telemetry_confidential",
    "production_secret",
    "AKIA",
]

CHECKED_SUFFIXES = {".csv", ".json", ".jsonl", ".yaml", ".yml", ".md", ".tex"}
EXCLUDED_DIRS = {".git", "build", "__pycache__", ".github"}


def test_no_sensitive_patterns():
    for path in Path(".").rglob("*"):
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix in CHECKED_SUFFIXES:
            content = path.read_text(errors="ignore")
            for pattern in FORBIDDEN_PATTERNS:
                assert pattern not in content, \
                    f"Sensitive pattern found in {path}"
