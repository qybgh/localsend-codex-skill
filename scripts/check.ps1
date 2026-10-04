# Run cross-platform checks on Windows.
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent (Split-Path -Parent $PSCommandPath)
$python = if (Get-Command py -ErrorAction SilentlyContinue) { "py" } else { "python" }
& $python -3 "$root\scripts\check.py"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
