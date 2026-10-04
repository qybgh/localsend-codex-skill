#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
target="${1:-$HOME/.local/bin}"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required" >&2
  exit 1
fi
if ! command -v openssl >/dev/null 2>&1; then
  echo "openssl is required" >&2
  exit 1
fi

mkdir -p "$target"
install -m 0755 "$root/scripts/localsend-cli" "$target/localsend-cli"
"$target/localsend-cli" --help >/dev/null

case ":$PATH:" in
  *":$target:"*) ;;
  *)
    echo "Installed: $target/localsend-cli"
    echo "Add this directory to PATH if needed:"
    echo "  export PATH=\"$target:\$PATH\""
    ;;
esac

echo "localsend-cli is ready."
