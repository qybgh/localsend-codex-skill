# LocalSend Transfer — AI 编程代理文件传输 Skill

[English](README.md) | 简体中文

一个兼容 `SKILL.md` 约定的 AI 编程代理 Skill，同时提供跨平台 CLI。它基于
[LocalSend](https://localsend.org) 协议在局域网内发送和接收文件，Python 包封装自
MIT 协议的 [`localsend-cli`](https://github.com/Chordlini/localsend-cli)。

不需要云盘账号、中转服务或互联网连接。

## 平台支持

| 角色 | macOS | Linux | Windows | iOS / Android |
|---|---:|---:|---:|---:|
| 发现设备 | ✅ | ✅ | ✅ | 使用 LocalSend App |
| 发送文件 | ✅ | ✅ | ✅ | 使用 LocalSend App |
| 接收文件 | ✅ | ✅ | ✅ | ✅ |

发送端或桌面接收端需要 Python 3.8+。使用 pip、pipx 或 uv 安装时会自动安装
`cryptography`，因此不再强制依赖系统 OpenSSL。手机等移动端只需要安装普通
LocalSend App 即可接收文件。

## 安装 CLI

### pipx（推荐）

```bash
pipx install "localsend-codex-skill @ git+https://github.com/qybgh/localsend-codex-skill.git@v0.1.1"
```

### uv

```bash
uv tool install "localsend-codex-skill @ git+https://github.com/qybgh/localsend-codex-skill.git@v0.1.1"
```

### pip

macOS / Linux：

```bash
python3 -m pip install --user "localsend-codex-skill @ git+https://github.com/qybgh/localsend-codex-skill.git@v0.1.1"
```

Windows PowerShell：

```powershell
py -3 -m pip install --user "localsend-codex-skill @ git+https://github.com/qybgh/localsend-codex-skill.git@v0.1.1"
```

### 从本地代码安装

```bash
git clone https://github.com/qybgh/localsend-codex-skill.git
cd localsend-codex-skill
python -m pip install .
```

Windows PowerShell 本地安装：

```powershell
git clone https://github.com/qybgh/localsend-codex-skill.git
cd localsend-codex-skill
.\scripts\install.ps1
```

安装后可用命令：

```bash
localsend-transfer --help
```

## 安装为 Agent Skill

### Codex

macOS / Linux：

```bash
git clone https://github.com/qybgh/localsend-codex-skill.git ~/.codex/skills/localsend-transfer
```

Windows PowerShell：

```powershell
git clone https://github.com/qybgh/localsend-codex-skill.git "$env:USERPROFILE\.codex\skills\localsend-transfer"
```

或使用自带安装器：

```bash
python scripts/install_skill.py --agent codex
```

### Claude Code

用户级：

```bash
git clone https://github.com/qybgh/localsend-codex-skill.git ~/.claude/skills/localsend-transfer
```

Windows PowerShell：

```powershell
git clone https://github.com/qybgh/localsend-codex-skill.git "$env:USERPROFILE\.claude\skills\localsend-transfer"
```

项目级，在目标仓库根目录执行：

```bash
git clone https://github.com/qybgh/localsend-codex-skill.git .claude/skills/localsend-transfer
```

或使用自带安装器：

```bash
python scripts/install_skill.py --agent claude-code
# 项目级：
python scripts/install_skill.py --agent claude-code --dir .claude/skills/localsend-transfer
```

### 其他支持 SKILL.md 的产品

如果你的产品支持 `SKILL.md` 约定，可以把这个仓库复制到它文档指定的全局或项目
skills 目录。核心说明和 CLI 不依赖 Codex。

### 只想使用 CLI 的产品

不读取 Skill 的产品也可以先安装 Python 包，然后直接调用：

```bash
localsend-transfer discover --json -t 3
localsend-transfer send --to "iPhone" /path/to/file.pdf
localsend-transfer receive --save-dir ~/Downloads/localsend
```

## 命令示例

使用已安装命令：

```bash
localsend-transfer discover --json -t 3
localsend-transfer send --to "iPhone" /path/to/file.pdf
localsend-transfer receive --save-dir ~/Downloads/localsend
```

Windows PowerShell 路径写法：

```powershell
localsend-transfer receive --save-dir "$HOME\Downloads\localsend"
```

跳过设备发现，直接指定 IP：

```bash
localsend-transfer send --ip 192.168.5.30 /path/to/file.pdf
```

自定义本机广播名称：

```bash
localsend-transfer --alias "Work Mac" receive --save-dir ~/Downloads/localsend
```

## 在 Agent 中使用

可以直接用自然语言描述任务：

```text
发现局域网里的 LocalSend 设备。
```

```text
把 /path/to/report.pdf 通过 LocalSend 发送到我的手机。
```

```text
接收 LocalSend 传输，保存到 ~/Downloads/localsend。
```

## 不安装 CLI 直接运行

从仓库检出版本：

```bash
python -m localsend_transfer discover --json -t 3
```

或使用单文件脚本：

```bash
python scripts/localsend-cli discover --json -t 3
```

Windows PowerShell：

```powershell
py -3 -m localsend_transfer discover --json -t 3
py -3 scripts\localsend-cli discover --json -t 3
```

Python 包安装会自动带上 `cryptography`。如果使用单文件脚本，请单独安装
`cryptography`，或确保命令行 OpenSSL 可用。

## 更新与卸载

pipx：

```bash
pipx upgrade localsend-codex-skill
pipx uninstall localsend-codex-skill
```

pip：

```bash
python -m pip install --upgrade "localsend-codex-skill @ git+https://github.com/qybgh/localsend-codex-skill.git@v0.1.1"
python -m pip uninstall localsend-codex-skill
```

## 安全提示

- 只在可信局域网中使用。
- 发送前确认目标别名和文件路径。
- 不要在不可信设备或网络上随意开启自动接收。
- 如果发现或传输失败，请在防火墙中放行 UDP/TCP `53317`，以及回退端口
  `53318`–`53319`。

## 社区

- [Linux.do](https://linux.do) — 感谢社区里的讨论、反馈和灵感，对这类项目帮助很大。

## 许可证

本仓库基于 [MIT License](LICENSE) 发布。CLI 部分基于
[`Chordlini/localsend-cli`](https://github.com/Chordlini/localsend-cli)，仍遵循
MIT License；详见 [`NOTICE.md`](NOTICE.md) 和
[`NOTICE.localsend-cli`](NOTICE.localsend-cli)。
