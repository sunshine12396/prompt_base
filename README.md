# 🎭 Prompt Base: The OS for AI Orchestration

> **"Simplicity is the ultimate sophistication."**  
> Empower your AI agents with the **Librarian Protocol**—a modular framework for JIT (Just-in-Time) knowledge management and multi-agent orchestration.

---

## 🏗️ The Framework at a Glance

Prompt Base is a production-grade configuration layer that transforms standard AI assistants into high-performance specialist teams. It utilizes **Progressive Disclosure** to keep context windows lean and reasoning sharp.

| Component | Count | Focus |
|-----------|-------|-------|
| 🤖 **Specialist Agents** | 14 | Role-based personas (Frontend, Security, DevOps, etc.) |
| 🧠 **Modular Skills** | 44 | JIT Knowledge modules (React v19, Go v1.23, OWASP 2025) |
| 🔄 **Smart Workflows** | 13 | Automated procedures for /debug, /create, and /orchestrate |
| 🛡️ **Quality Gates** | 3 | Automated check-scripts for Security, Linting, and UX |

---

## 🛠️ Supported Platforms

| Platform | Support | How It Works |
|----------|---------|--------------|
| **Antigravity** | ✅ Native | Reads `GEMINI.md` from `.agent/` folder automatically |
| **Cursor** | ✅ Native | Uses `.cursorrules` + `.cursor/rules/` (auto-configured) |

> 🚫 **Other IDEs are not officially supported.** This framework is optimized for Antigravity and Cursor.

---

## ⚡ Integration (One Command)

```bash
cd /path/to/your/project
git clone https://github.com/sunshine12396/prompt_base .pb_tmp && cd .pb_tmp && make init
```

That's it! `make init` installs the framework and cleans up automatically.

### Alternative: Manual Install

```bash
# If you prefer step-by-step:
git clone https://github.com/sunshine12396/prompt_base .pb_tmp
python3 .pb_tmp/scripts/install.py . --hidden
rm -rf .pb_tmp
```

---

## 📚 The Librarian Protocol

The core of Prompt Base is the **Discovery → Activation → Pruning** lifecycle:

1. **Discovery**: The AI analyzes your request and consults `registry.json`.
2. **Activation**: The exact `SKILL.md` needed (e.g., `tailwind-v4`) is loaded into context.
3. **Execution**: Specialist agents (e.g., `frontend-specialist`) perform the work.
4. **Pruning**: Knowledge is cleared after completion to prevent "token bloat."

---

## 📊 Core Standards

Every line of code generated via Prompt Base follows our **Tier 0 Universal Rules**:

* **Socratic Gate**: No complex code is written without clarifying requirements first.
* **Zero-Trust Security**: Every feature is scanned for vulnerabilities (OWASP 2025).
* **Unified Quality**: Integrated linting for Python, React, and Go.
* **Atomic Refactoring**: All dependent files are updated simultaneously.

---

## 📂 Documentation

* 🔌 **[Integration Guide](docs/INTEGRATION.md)**: Setup instructions for Antigravity and Cursor.
* 🏗️ **[Architecture Deep-Dive](.agent/ARCHITECTURE.md)**: How the Librarian actually works.
* 🧠 **[Skills Registry](.agent/registry.json)**: Explore the full library of 44 knowledge modules.

---

## 🚀 After Installation

Once installed, the framework is ready to use:

### For Antigravity
- The AI automatically reads `.agent/GEMINI.md` at session start
- Use slash commands like `/create`, `/debug`, `/orchestrate`, `/review`

### For Cursor
- Open your project in Cursor
- The `.cursorrules` file tells Cursor to read the framework
- Use Command+L (Chat) or Command+I (Composer) to interact

---

> **Built for the next generation of Agentic Coding.**  
> *Prompt Base — "The OS for AI Agents"*
