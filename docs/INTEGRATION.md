# 🔌 Integration Guide

This guide details how to integrate **Prompt Base** into your existing projects using various IDEs.

---

## ⚡ Standard Integration Workflow (The "Maestro" Way)

This is the recommended path for production projects.

1.  **Clone & Init**:
    ```bash
    git clone https://github.com/your-org/prompt_base .pb_tmp
    cd .pb_tmp && make init
    ```
2.  **Cleanup**:
    ```bash
    cd .. && rm -rf .pb_tmp
    ```

## ⚡ Manual Installation (Reference)

### 1. Standard Installation
Installs everything into `.agent/` (or `agent/`) at the root.
```bash
python3 scripts/install.py /path/to/target
```

### 2. Hidden Mode Installation
Installs specifically into `.agent/` to keep your project root clean.
```bash
python3 scripts/install.py /path/to/target --hidden
```

**What it does**:
- Copies the framework.
- Updates paths in `registry.json` to match the new location.
- Automatically corrects documentation file references (`.agent/` vs `..agent/`).
- Installs `.cursorrules` pointing to the correct `GEMINI.md`.
- Sets up `.vscode/ai_instructions.md`.

---

## 🟢 Antigravity / Maestro

If using the **Antigravity** IDE or extension:

1.  **Native Support**: Antigravity automatically detects the `.agent/` folder.
2.  **Verify**: Open the Command Palette and type `Prompt Base: Check Status`.
3.  **Manual Load**: If not detected, ensure `.agent/GEMINI.md` exists at the project root.

---

## 🔵 Cursor (The AI Editor)

Cursor is our primary supported platform. The **Librarian Protocol** is optimized for Cursor's context window.

### Configuration
The installer sets up `.cursorrules` automatically. If doing it manually:

1.  **File**: Ensure `.cursorrules` in your project root contains:
    ```markdown
    # Include the Master Config
    This project uses the Prompt Base framework.
    ALWAYS Reference: .agent/GEMINI.md
    ```
2.  **Indexing**: Go to `Cursor Settings` -> `General` -> `Codebase Indexing` and ensure "Include .agent/" is enabled.

### Usage
- **Command K**: Best for small edits (Status: Tier 1).
- **Command L (Chat)**: Best for planning/architecting (Status: Tier 0).
- **Composer (Command I)**: Good for multi-file edits (Status: Tier 1).

---

## 🟠 VS Code (Copilot / Cline / Roo)

Standard VS Code requires explicit context instructions.

### GitHub Copilot
1.  **Instructions**: Add explicit instructions in `.github/copilot-instructions.md` (or `.vscode/settings.json` "github.copilot.chat.codeGeneration.instructions").
    ```text
    Reference .agent/GEMINI.md for all coding standards.
    Reference .agent/registry.json for available skills.
    ```

### Cline / Roo Code / Autonomous Agents
1.  **Custom Instructions**:
    > "You are the Orchestrator. Read `.agent/GEMINI.md` immediately. Use `.agent/registry.json` to look up skills before answering."

---

## 🟣 JetBrains / IntelliJ

1.  **Context**: You must manually add `.agent/GEMINI.md` to the AI Assistant context context for every session.
2.  **Prompt**: "Act as the Prompt Base Orchestrator. Read the attached GEMINI.md file."
