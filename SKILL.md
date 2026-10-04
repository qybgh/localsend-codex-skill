---
name: localsend-transfer
description: Send, discover, or receive files over the local network with LocalSend through the bundled localsend-cli. Use when the user asks to share files with a nearby device, find LocalSend receivers, or accept an incoming LAN transfer.
metadata:
  upstream: https://github.com/Chordlini/localsend-cli
  protocol: https://github.com/localsend/protocol
---

# LocalSend Transfer

Use the bundled zero-dependency CLI to transfer files over the local network with LocalSend. Python 3.8+ and `openssl` are required.

## Setup

Resolve `skill_dir` as the directory containing this `SKILL.md`, then use the bundled CLI:

```bash
cli="$skill_dir/scripts/localsend-cli"
"$cli" --help
```

To make it available as `localsend-cli`, install the vendored copy:

```bash
"$skill_dir/scripts/install.sh"
```

## Discover receivers

Run a short scan and prefer machine-readable output:

```bash
"$cli" discover --json -t 3
```

For a human-readable scan, omit `--json`. If no device appears, ask the receiver to open LocalSend, keep the screen unlocked, and confirm both devices are on the same local network.

## Send files

Before sending, confirm:

1. The target alias or discovered device.
2. Every requested path exists and is the intended file.
3. The user understands the transfer happens over the local network.

Then send one or more files:

```bash
"$cli" send --to "DEVICE_ALIAS" /path/to/file1 /path/to/file2
```

`--to` is a case-insensitive substring match. Use enough of the alias to avoid sending to the wrong receiver. Do not guess a receiver if discovery returns multiple candidates.

## Receive files

Receiving is an interactive operation. Start it only when the user wants this machine to accept a transfer:

```bash
mkdir -p "$HOME/Downloads/localsend"
"$cli" receive --save-dir "$HOME/Downloads/localsend"
```

For unattended use, the receiver can auto-accept, but treat that as a security-sensitive choice and confirm it explicitly:

```bash
"$cli" receive -y --save-dir "$HOME/Downloads/localsend"
```

Stop the receiver with `Ctrl+C`. Report the saved paths and verify that each received file matches the expected name or checksum when one is available.

## Troubleshooting

- `No devices found`: open LocalSend on the other device, keep it foregrounded, and retry discovery.
- Ambiguous alias: run discovery again and ask the user to choose the exact receiver.
- `Transfer declined`: the receiver rejected the transfer; retry only after the user accepts it.
- `--alias` placement: it is a global flag, so put it before the subcommand.
- Port conflicts: the CLI automatically tries LocalSend fallback ports.

## Attribution

The CLI is vendored from [`Chordlini/localsend-cli`](https://github.com/Chordlini/localsend-cli) under MIT; see [`NOTICE.localsend-cli`](NOTICE.localsend-cli) and [`NOTICE.md`](NOTICE.md).
