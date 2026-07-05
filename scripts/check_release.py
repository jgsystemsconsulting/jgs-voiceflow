# Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE.
# SPDX-License-Identifier: LicenseRef-JGSystemsConsulting-Proprietary
"""Release gate (RR-B-15): required files, forbidden paths, forbidden
content, headers present. Exits non-zero on any failure.

jgs-voiceflow is a public, docs-only release repo (Base profile, no
MCP/skills-pack artifacts, no first-party .py source to ship)."""
import pathlib
import re
import subprocess
import sys

fails: list[str] = []

REQUIRED = [
    "LICENSE", "COPYRIGHT", "NOTICE", "README.md", "CHANGELOG.md",
    "RELEASE-INFO.txt", "CITATION.cff", "SECURITY.md", ".gitignore",
]
for f in REQUIRED:
    if not pathlib.Path(f).is_file():
        fails.append(f"required file missing: {f}")

# forbidden paths: judge the TRACKED tree (local gitignored dirs are fine)
tracked = subprocess.run(["git", "ls-files"], capture_output=True, text=True,
                         check=True).stdout.splitlines()
FORBIDDEN_PATH_PARTS = ["__pycache__", ".venv", ".worktrees", ".pytest_cache",
                        ".ruff_cache", ".bak", ".playwright-mcp"]
for f in tracked:
    if any(part in f for part in FORBIDDEN_PATH_PARTS):
        fails.append(f"forbidden tracked path: {f}")

FORBIDDEN_CONTENT = [re.compile(r"BEGIN [A-Z ]*PRIVATE KEY"),
                     re.compile(r"CONFIDENTIAL\s+[-—]\s+Not for external distribution")]
SCAN_GLOBS = ["docs/**/*.md", "docs/**/*.html", "*.md", "*.txt", "*.cff"]
for g in SCAN_GLOBS:
    for path in pathlib.Path(".").glob(g):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for rx in FORBIDDEN_CONTENT:
            if rx.search(text):
                fails.append(f"forbidden content in {path}: {rx.pattern}")

# version consistency across the single sources of truth (RR-B-09)
def top_changelog_version() -> str | None:
    text = pathlib.Path("CHANGELOG.md").read_text(encoding="utf-8")
    for line in text.splitlines():
        m = re.match(r"^## \[([^\]]+)\]", line)
        if m and m.group(1) != "Unreleased":
            return m.group(1)
    return None

def release_info_version() -> str | None:
    text = pathlib.Path("RELEASE-INFO.txt").read_text(encoding="utf-8")
    m = re.search(r"^Version:\s*(\S+)", text, re.M)
    return m.group(1) if m else None

def citation_version() -> str | None:
    text = pathlib.Path("CITATION.cff").read_text(encoding="utf-8")
    m = re.search(r'^version:\s*"?([^"\s]+)"?', text, re.M)
    return m.group(1) if m else None

versions = {
    "CHANGELOG.md": top_changelog_version(),
    "RELEASE-INFO.txt": release_info_version(),
    "CITATION.cff": citation_version(),
}
uniq = {v for v in versions.values() if v}
if len(uniq) != 1:
    fails.append(f"version mismatch across single sources of truth: {versions}")

if fails:
    print("RELEASE GATE FAILED:")
    for f in fails:
        print(f"  - {f}")
    sys.exit(1)
print("release gate: PASS")
