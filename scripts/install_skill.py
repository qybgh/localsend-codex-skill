#!/usr/bin/env python3
"""Install the LocalSend skill files for supported AI coding agents."""

import argparse
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "localsend-transfer"
IGNORED = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
IGNORED_SUFFIXES = {".pyc", ".egg-info"}


def default_target(agent: str) -> Path:
    home = Path.home()
    if agent == "codex":
        base = Path(os.environ.get("CODEX_HOME", home / ".codex")) / "skills"
    elif agent == "claude-code":
        base = Path(os.environ.get("CLAUDE_CONFIG_DIR", home / ".claude")) / "skills"
    else:
        raise ValueError(f"No default directory for agent: {agent}")
    return base / SKILL_NAME


def copy_tree(destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    for source in ROOT.rglob("*"):
        relative = source.relative_to(ROOT)
        if any(part in IGNORED for part in relative.parts):
            continue
        if any(relative.suffix == suffix or str(relative).endswith(suffix) for suffix in IGNORED_SUFFIXES):
            continue
        target = destination / relative
        if source.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        elif source.is_file():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)


def main() -> None:
    parser = argparse.ArgumentParser(description="Install the LocalSend skill for an AI coding agent.")
    parser.add_argument(
        "--agent",
        choices=("codex", "claude-code"),
        default="codex",
        help="Target product (default: codex)",
    )
    parser.add_argument(
        "--dir",
        type=Path,
        help="Custom skill destination. Overrides the product default.",
    )
    parser.add_argument(
        "--replace",
        action="store_true",
        help="Remove an existing destination before installing.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show the destination without copying files.",
    )
    args = parser.parse_args()

    destination = args.dir.expanduser() if args.dir else default_target(args.agent)
    print(f"Installing {SKILL_NAME} for {args.agent}:")
    print(f"  source: {ROOT}")
    print(f"  target: {destination}")

    if destination.exists() and args.replace:
        if args.dry_run:
            print("dry-run: would replace existing destination")
        else:
            shutil.rmtree(destination)

    if args.dry_run:
        return
    if destination.exists():
        raise SystemExit(
            f"Destination already exists: {destination}\n"
            "Use --replace to update it, or choose another --dir."
        )

    copy_tree(destination)
    print("Installed successfully.")
    print("The bundled CLI can be run from the copied scripts directory.")
    print("For the recommended installed command, also run:")
    print('  pipx install "localsend-codex-skill @ git+https://github.com/qybgh/localsend-codex-skill.git@v0.1.1"')


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
