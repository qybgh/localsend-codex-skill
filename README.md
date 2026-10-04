# LocalSend Transfer Skill for Codex

A Codex skill for sending and receiving files over the local network with
[LocalSend](https://localsend.org). It packages the MIT-licensed
[`localsend-cli`](https://github.com/Chordlini/localsend-cli) and gives Codex
deterministic workflows for discovery, sending, and receiving.

## Features

- Discover LocalSend receivers on the LAN.
- Send one or more files with alias-based targeting.
- Receive files into a chosen directory.
- Uses LocalSend v2 protocol; no internet service or account is required.
- Single-file Python CLI with only Python 3.8+ and `openssl` as runtime requirements.

## Install this skill

Copy this repository into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/qybgh/localsend-codex-skill.git ~/.codex/skills/localsend-transfer
```

Optionally install the CLI on your PATH:

```bash
~/.codex/skills/localsend-transfer/scripts/install.sh
```

## Use with Codex

Ask Codex to:

```text
Send /path/to/report.pdf to my phone with LocalSend.
```

```text
Discover LocalSend devices on this network.
```

```text
Receive a LocalSend file into ~/Downloads/localsend.
```

## Manual CLI examples

From the skill directory:

```bash
./scripts/localsend-cli discover --json -t 3
./scripts/localsend-cli send --to "iPhone" /path/to/file
./scripts/localsend-cli receive --save-dir "$HOME/Downloads/localsend"
```

`--alias NAME` is a global flag and must appear before the subcommand:

```bash
./scripts/localsend-cli --alias "Work Mac" receive --save-dir "$HOME/Downloads/localsend"
```

## Security notes

- Transfers are intended for trusted local networks.
- Avoid auto-accepting incoming transfers unless the machine and network are trusted.
- Confirm target aliases and file paths before sending.

## License

This repository is released under the [MIT License](LICENSE). The vendored CLI
comes from [`Chordlini/localsend-cli`](https://github.com/Chordlini/localsend-cli)
and remains MIT-licensed; see [`NOTICE.md`](NOTICE.md) and
[`NOTICE.localsend-cli`](NOTICE.localsend-cli).
