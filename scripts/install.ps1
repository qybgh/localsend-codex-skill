# Install the CLI for the current user on Windows.
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent (Split-Path -Parent $PSCommandPath)
$python = if (Get-Command py -ErrorAction SilentlyContinue) { "py" } else { "python" }
& $python -3 -m pip install --user $root
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Write-Host "localsend-transfer is ready. If it is not on PATH, add Python's user Scripts directory."
