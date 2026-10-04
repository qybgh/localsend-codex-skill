---
name: localsend-transfer
description: Send, discover, or receive files over the local network with LocalSend. Use when the user asks to share files with a nearby device, find LocalSend receivers, or accept an incoming LAN transfer.
metadata:
  upstream: https://github.com/Chordlini/localsend-cli
  protocol: https://github.com/localsend/protocol
---

# LocalSend Transfer

Transfer files over the local network with LocalSend. Prefer the installed
`localsend-transfer` command. If it is unavailable, use the bundled standalone
CLI from this skill.

## Choosing the command

First try:

```bash
localsend-transfer --help
```

If unavailable, resolve `skill_dir` as the directory containing this
`SKILL.md` and use the bundled script:

- macOS / Linux:
  ```bash
  python3 "$skill_dir/scripts/localsend-cli" --help
  ```
- Windows PowerShell:
  ```powershell
  py -3 "$skill_dir\scripts\localsend-cli" --help
  ```

The installed package automatically provides the `cryptography` dependency.
For the standalone script, install `cryptography` or ensure OpenSSL is on PATH.

## Discover receivers

Prefer machine-readable output:

```bash
localsend-transfer discover --json -t 3
```

If no device appears, ask the receiver to open LocalSend, keep it foregrounded,
and confirm both devices are on the same local network.

## Send files

Before sending, confirm the target and that every path exists. Then send:

```bash
localsend-transfer send --to "DEVICE_ALIAS" /path/to/file1 /path/to/file2
```

For direct IP mode without discovery:

```bash
localsend-transfer send --ip 192.168.1.50 /path/to/file.pdf
```

`--to` is a case-insensitive substring match. Do not guess when multiple
receivers match; run discovery and ask the user to choose one.

## Receive files

Start receiving only when the user wants this machine to accept a transfer:

```bash
localsend-transfer receive --save-dir ~/Downloads/localsend
```

Auto-accept is security-sensitive and must be explicitly requested:

```bash
localsend-transfer receive -y --save-dir ~/Downloads/localsend
```

Report saved paths after transfer. If the user supplies an expected checksum,
verify it.

## Troubleshooting

- `No devices found`: LocalSend must be running on the target, both devices must
  be on the same LAN, and the screen may need to be unlocked.
- Firewall: allow UDP/TCP `53317`; the CLI also tries `53318` and `53319`.
- Ambiguous alias: rerun discovery and ask the user to select the exact target.
- `--alias` is global and must come before the subcommand.
- On Windows, run `py -3` if the `python` launcher is not configured.

## Attribution

The CLI is based on [`Chordlini/localsend-cli`](https://github.com/Chordlini/localsend-cli)
under MIT; see `NOTICE.localsend-cli` and `NOTICE.md`.
