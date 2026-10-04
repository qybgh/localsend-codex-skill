#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
command -v python3 >/dev/null
command -v openssl >/dev/null
python3 -m py_compile "$root/scripts/localsend-cli"
"$root/scripts/localsend-cli" --help >/dev/null
echo "localsend-cli skill checks passed."
