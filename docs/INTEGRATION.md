# 🔌 Integration Guide

This guide details how to integrate **Prompt Base** into your existing projects.

> ✅ **Supported Platforms**: Antigravity, Cursor  
> 🚫 **Not Supported**: VS Code, JetBrains, other IDEs

---

## ⚡ Quick Integration (One Command)

```bash
cd /path/to/your/project
git clone https://github.com/sunshine12396/prompt_base .pb_tmp && cd .pb_tmp && make init
```

**What this does:**
- Clones the framework to a temp folder
- Copies `.agent/` folder to your project
- Installs `.cursorrules` for Cursor support
- Installs `.cursor/rules/` for modern Cursor rules
- **Automatically cleans up the temp folder**

---

## 🟢 Antigravity Setup

Antigravity has **native support** for Prompt Base.

### Automatic Detection
1. Antigravity automatically detects the `.agent/` folder in your project
2. It reads `.agent/GEMINI.md` at session start
3. No additional configuration needed

### Manual Verification
If Antigravity doesn't detect the framework:
1. Ensure `.agent/GEMINI.md` exists at your project root
2. Check that the file contains valid Markdown
3. Restart your Antigravity session

### How Antigravity Uses the Framework
```
Session Start
    ↓
Read .agent/GEMINI.md (rules, tiers, agents)
    ↓
On User Request → Consult .agent/registry.json
    ↓
Load relevant SKILL.md from .agent/skills/
    ↓
Execute with specialist agent
    ↓
Prune knowledge after task
```

---

## 🔵 Cursor Setup

Cursor uses `.cursorrules` and `.cursor/rules/` for configuration.

### Automatic Configuration
The installer sets up both:
1. **`.cursorrules`** (legacy) - Simple pointer to GEMINI.md
2. **`.cursor/rules/prompt-base.mdc`** (modern) - Detailed rules with glob patterns

### Manual Setup (if needed)

#### Option A: Minimal .cursorrules
Create `.cursorrules` in your project root:
```markdown
# Prompt Base Configuration

> 🔴 **MANDATORY**: You MUST read `.agent/GEMINI.md` at the start of every session.

This file (`.cursorrules`) is a pointer. The actual intelligence is in:
- **Rules**: `.agent/GEMINI.md`
- **Skills**: `.agent/registry.json`
```

#### Option B: Modern .cursor/rules/ (Recommended)
Create `.cursor/rules/prompt-base.mdc`:
```markdown
---
description: Core Prompt Base behavior and Librarian Protocol
globs: **/*
---

# Prompt Base Core Rules

You are the **AI Orchestrator** using the Prompt Base framework.

## 📚 THE LIBRARIAN PROTOCOL
- **Discovery**: Analyze intent and search `.agent/registry.json`.
- **Activation**: Load necessary `SKILL.md` files from `.agent/skills/`.
- **Pruning**: Clear dormant knowledge after task completion.

## 🛑 MANDATORY STEP 0
Before starting any significant task, you MUST:
1. Read `.agent/GEMINI.md` for full context.
2. If it's a new feature or complex edit, ask at least 3 Socratic questions.

## 📁 PATH AWARENESS
- Agents: `.agent/agents/`
- Skills: `.agent/skills/`
- Workflows: `.agent/workflows/`
```

### Cursor Settings
1. Go to `Cursor Settings` → `General` → `Codebase Indexing`
2. Ensure `.agent/` folder is included in indexing

### Cursor Usage Modes
| Mode | Shortcut | Best For |
|------|----------|----------|
| **Chat** | Cmd+L | Planning, architecture, asking questions |
| **Composer** | Cmd+I | Multi-file edits, feature implementation |
| **Inline Edit** | Cmd+K | Single-file quick edits |

---

## 📁 Project Structure After Installation

```
your-project/
├── .agent/                    # ← Prompt Base Framework
│   ├── GEMINI.md              # Main configuration (read by both IDEs)
│   ├── ARCHITECTURE.md        # System documentation
│   ├── registry.json          # Skill discovery index
│   ├── agents/                # 19 specialist agents
│   ├── skills/                # 44 knowledge modules
│   ├── workflows/             # 13 slash commands
│   ├── core/                  # Core rules
│   ├── docs/                  # Documentation
│   └── scripts/               # Utility scripts
├── .cursorrules               # ← Cursor pointer (auto-created)
├── .cursor/
│   └── rules/
│       └── prompt-base.mdc    # ← Modern Cursor rules (auto-created)
└── ... your project files
```

---

## 🔧 Manual Installation Options

### Standard Install
```bash
python3 scripts/install.py /path/to/target
```

### Hidden Mode (Recommended)
Installs everything inside `.agent/` to keep project root clean:
```bash
python3 scripts/install.py /path/to/target --hidden
```

---

## ✅ Verification

After installation, verify the setup:

### For Antigravity
1. Start a new session in your project
2. Ask: "What agents are available?"
3. The AI should reference `.agent/GEMINI.md` and list the 19 agents

### For Cursor
1. Open your project in Cursor
2. Press Cmd+L and ask: "Read the project configuration"
3. Cursor should mention GEMINI.md and the Librarian Protocol

---

## 🔄 Updating Prompt Base

To update to the latest version:

```bash
# Navigate to your project
cd /path/to/your/project

# Remove old framework (keep your customizations in .agent/custom/)
rm -rf .agent/agents .agent/skills/core .agent/skills/tech .agent/skills/process

# Re-install
git clone https://github.com/sunshine12396/prompt_base .pb_tmp
cd .pb_tmp && make init
cd .. && rm -rf .pb_tmp
```

> 💡 **Tip**: Custom skills in `.agent/skills/custom/` are preserved during updates.

---

## ❓ Troubleshooting

### Antigravity doesn't read GEMINI.md
- Ensure the file exists at `.agent/GEMINI.md`
- Check file permissions
- Restart your session

### Cursor ignores .cursorrules
- Ensure the file is at project root (not inside a folder)
- Check Cursor's indexing settings
- Try the modern `.cursor/rules/` approach instead

### Skills not loading
- Verify `.agent/registry.json` exists and is valid JSON
- Check that skill paths in registry match actual file locations
- Run `python3 .agent/scripts/generate_registry.py .agent` to regenerate

---

> **Need help?** Open an issue on GitHub or check the [Architecture Guide](.agent/ARCHITECTURE.md).
