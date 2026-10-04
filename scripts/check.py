#!/usr/bin/env python3
import importlib.machinery
import importlib.util
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
if sys.version_info < (3, 8):
    raise SystemExit("Python 3.8+ is required")
try:
    import cryptography  # noqa: F401
except ImportError as exc:
    raise SystemExit("The cryptography package is required; install with pip/pipx/uv") from exc
loader = importlib.machinery.SourceFileLoader("localsend_cli", str(root / "scripts" / "localsend-cli"))
spec = importlib.util.spec_from_loader(loader.name, loader)
module = importlib.util.module_from_spec(spec)
loader.exec_module(module)
print("localsend-transfer cross-platform checks passed.")
