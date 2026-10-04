# LocalSend Transfer Skill for AI coding agents

[English](README.md) | [简体中文](README.zh-CN.md)

A SKILL.md-compatible skill and cross-platform CLI for sending and receiving files over the
local network with [LocalSend](https://localsend.org). The Python package wraps
the LocalSend v2 protocol and packages code based on the MIT-licensed
[`localsend-cli`](https://github.com/Chordlini/localsend-cli).

No cloud account, relay service, or internet connection is required.

## Platform support

| Role | macOS | Linux | Windows | iOS / Android |
|---|---:|---:|---:|---:|
| Discover devices | ✅ | ✅ | ✅ | Use LocalSend app |
| Send files | ✅ | ✅ | ✅ | Use LocalSend app |
| Receive files | ✅ | ✅ | ✅ | ✅ |

The sender/receiver needs Python 3.8+. The `cryptography` package is installed
automatically by pip/pipx/uv and removes the standalone CLI's OpenSSL
dependency. Mobile devices only need the normal LocalSend app to receive files.

## Install the CLI

### pipx (recommended)

```bash
pipx install "localsend-codex-skill @ git+https://github.com/qybgh/localsend-codex-skill.git@v0.1.1"
```

### uv

```bash
uv tool install "localsend-codex-skill @ git+https://github.com/qybgh/localsend-codex-skill.git@v0.1.1"
```

### pip

macOS / Linux:

```bash
python3 -m pip install --user "localsend-codex-skill @ git+https://github.com/qybgh/localsend-codex-skill.git@v0.1.1"
```

Windows PowerShell:

```powershell
py -3 -m pip install --user "localsend-codex-skill @ git+https://github.com/qybgh/localsend-codex-skill.git@v0.1.1"
```

### From a local checkout

```bash
git clone https://github.com/qybgh/localsend-codex-skill.git
cd localsend-codex-skill
python -m pip install .
```

Windows PowerShell from a local checkout:

```powershell
git clone https://github.com/qybgh/localsend-codex-skill.git
cd localsend-codex-skill
.\scripts\install.ps1
```

After installation, the command is available as:

```bash
localsend-transfer --help
```

## Install as an agent skill

### Codex

macOS / Linux:

```bash
git clone https://github.com/qybgh/localsend-codex-skill.git ~/.codex/skills/localsend-transfer
```

Windows PowerShell:

```powershell
git clone https://github.com/qybgh/localsend-codex-skill.git "$env:USERPROFILE\.codex\skills\localsend-transfer"
```

Or use the bundled installer:

```bash
python scripts/install_skill.py --agent codex
```

### Claude Code

User scope:

```bash
git clone https://github.com/qybgh/localsend-codex-skill.git ~/.claude/skills/localsend-transfer
```

macOS PowerShell equivalent:

```powershell
git clone https://github.com/qybgh/localsend-codex-skill.git "$env:USERPROFILE\.claude\skills\localsend-transfer"
```

Project scope, run from the target repository:

```bash
git clone https://github.com/qybgh/localsend-codex-skill.git .claude/skills/localsend-transfer
```

Or use the bundled installer:

```bash
python scripts/install_skill.py --agent claude-code
# project scope:
python scripts/install_skill.py --agent claude-code --dir .claude/skills/localsend-transfer
```

### Other SKILL.md-compatible agents

If your product supports the SKILL.md convention, copy this repository to its
documented global or project skills directory. The core instruction and CLI are
not Codex-specific.

### CLI-only products

Agents that do not read skills can still use the transfer command after
installing the package with pipx, uv, or pip. Then ask or script against:

```bash
localsend-transfer discover --json -t 3
localsend-transfer send --to "iPhone" /path/to/file.pdf
localsend-transfer receive --save-dir ~/Downloads/localsend
```

## Command examples

Installed command:

```bash
localsend-transfer discover --json -t 3
localsend-transfer send --to "iPhone" /path/to/file.pdf
localsend-transfer receive --save-dir ~/Downloads/localsend
```

Windows PowerShell path syntax:

```powershell
localsend-transfer receive --save-dir "$HOME\Downloads\localsend"
```

Direct IP mode skips discovery:

```bash
localsend-transfer send --ip 192.168.5.30 /path/to/file.pdf
```

Custom advertised name:

```bash
localsend-transfer --alias "Work Mac" receive --save-dir ~/Downloads/localsend
```

## Use with an agent

Ask the agent naturally:

```text
Discover LocalSend devices on this network.
```

```text
Send /path/to/report.pdf to my phone with LocalSend.
```

```text
Receive a LocalSend transfer into ~/Downloads/localsend.
```

## Running without installing the CLI

From a repository checkout:

```bash
python -m localsend_transfer discover --json -t 3
```

Or use the standalone script:

```bash
python scripts/localsend-cli discover --json -t 3
```

Windows PowerShell:

```powershell
py -3 -m localsend_transfer discover --json -t 3
py -3 scripts\localsend-cli discover --json -t 3
```

The package installation installs `cryptography`; for the standalone script,
install it separately or ensure the OpenSSL command-line tool is available.

## Updating and removing

pipx:

```bash
pipx upgrade localsend-codex-skill
pipx uninstall localsend-codex-skill
```

pip:

```bash
python -m pip install --upgrade "localsend-codex-skill @ git+https://github.com/qybgh/localsend-codex-skill.git@v0.1.1"
python -m pip uninstall localsend-codex-skill
```

## Security notes

- Use this only on trusted local networks.
- Confirm target aliases and paths before sending.
- Do not enable auto-accept on untrusted machines or networks.
- Allow UDP/TCP port `53317`, and fallback ports `53318`–`53319`, through your
  firewall if discovery or transfer fails.

## Community

- [Linux.do](https://linux.do) — a friendly developer community. Thanks for the
  discussions, feedback, and inspiration that support projects like this one.

## License

This repository is released under the [MIT License](LICENSE). The CLI is based
on [`Chordlini/localsend-cli`](https://github.com/Chordlini/localsend-cli) and
remains MIT-licensed; see [`NOTICE.md`](NOTICE.md) and
[`NOTICE.localsend-cli`](NOTICE.localsend-cli).
