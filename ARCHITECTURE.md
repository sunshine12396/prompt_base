# Prompt Base Architecture

## 📋 Overview

Prompt Base is a modular system consisting of:

- **14 Specialist Agents** - Role-based AI personas
- **40 Skills** - Categorized knowledge modules
- **14 Workflows** - Slash command procedures

---

## 🏗️ Directory Structure

Prompt Base can be installed **globally** (`~/.gemini/`) or as a **workspace subfolder** (`.agents/`). All documentation uses `{FRAMEWORK_ROOT}` as a placeholder that resolves based on installation type.

| Install Type     | Clone Target | `{FRAMEWORK_ROOT}` resolves to |
| ---------------- | ------------ | ------------------------------ |
| **Global Rules** | `~/.gemini`  | `~/.gemini`                    |
| **Workspace**    | `.agents`    | `.agents`                      |

```
{FRAMEWORK_ROOT}/
├── core/             # Global rules and orchestration logic
├── agents/           # 14 Specialist Agents
├── skills/           # Categorized Skills
├── workflows/        # Slash commands
├── registry.min.json # Unified metadata index
└── GEMINI.md         # Global governance
```

When using **workspace mode**, the layout within your project looks like:

```
<project-root>/
├── .agents/              # {FRAMEWORK_ROOT} (Cloned here)
│   ├── core/
│   ├── agents/
│   ├── skills/
│   ├── workflows/
│   ├── registry.min.json
│   └── GEMINI.md
├── docs/                 # Task plans (docs/PLAN-*.md)
├── .cursorrules          # Pointer to .agents/GEMINI.md
└── ...                   # Your project files
```

---

## 📚 The "Librarian" Pattern

Prompt Base uses **Progressive Disclosure** to manage complexity. Skills remain dormant until activated.

1. **Discovery**: Orchestrator consults `registry.min.json`.
2. **Activation**: The system loads the specific `SKILL.md` required for the task.
3. **Execution**: The specialized agent performs the task.
4. **Pruning**: Knowledge is cleared after task completion to maintain context window efficiency.

---

## 🤖 Agents (14)

| Category            | Agents                                                                                             |
| ------------------- | -------------------------------------------------------------------------------------------------- |
| **Core**            | `orchestrator`, `project-planner`, `explorer-agent`                                                |
| **Dev**             | `frontend-specialist`, `backend-specialist`, `mobile-developer`                                    |
| **Quality**         | `test-engineer`, `debugger`, `performance-optimizer`, `documentation-writer`                       |
| **Infra/Sec**       | `devops-engineer`, `security-auditor`, `database-architect`                                        |
| **Growth & Search** | `seo-specialist`                                                                                   |

---

## 🧠 Skills (40)

### Core (8)

| Skill                | Description               |
| -------------------- | ------------------------- |
| `clean-code`         | Coding standards          |
| `brainstorming`      | Socratic discovery        |
| `plan-writing`       | Task breakdown            |
| `architecture`       | System design             |
| `skill-loading`      | JIT Knowledge discovery   |
| `context-management` | Context efficiency (MVC)  |
| `behavioral-modes`   | Operational personas      |
| `parallel-agents`    | Multi-perspective analysis|

### Technology (16)

| Category    | Skills                                                                              |
| ----------- | ----------------------------------------------------------------------------------- |
| **Web**     | `react-patterns`, `nextjs-best-practices`, `tailwind-patterns`, `typescript-expert` |
| **Backend** | `nodejs-best-practices`, `python-patterns`, `prisma-expert`, `nestjs-expert`, `golang-best-practices`, `api-patterns` |
| **Mobile**  | `mobile-design`                                                                     |
| **Other**   | `database-design`, `docker-expert`, `game-development`, `ux-ui-pro-max`, `mcp-builder` |

### Process (16)

| Category    | Skills                                                                              |
| ----------- | ----------------------------------------------------------------------------------- |
| **Testing** | `testing-patterns`, `tdd-workflow`, `webapp-testing`, `lint-and-validate`           |
| **Security**| `vulnerability-scanner`, `red-team-tactics`, `red-teaming`                           |
| **Growth**  | `seo-fundamentals`, `geo-fundamentals`                                              |
| **Ops**     | `deployment-procedures`, `server-management`, `bash-linux`, `powershell-windows`    |
| **Meta**    | `code-review-checklist`, `documentation-templates`, `review-pre-commit-git`, `i18n-localization` |

---

## 🔄 Workflows (14)

| Command         | Description                   |
| --------------- | ----------------------------- |
| `/brainstorm`   | Socratic discovery            |
| `/create`       | Create new features           |
| `/debug`        | Debug issues                  |
| `/deploy`       | Deploy application            |
| `/enhance`      | Improve existing code         |
| `/orchestrate`  | Multi-agent coordination      |
| `/plan`         | Task breakdown                |
| `/status`       | Check project status          |
| `/test`         | Run tests                     |
| `/init-context` | Initialize MVC                |
| `/deep-solve`   | JIT Knowledge workflow        |
| `/restructure`  | Maintenance & registry update |
| `/review`       | Pre-commit audit              |
| `/ux-ui-pro`    | Design intelligence           |

---

## 📊 Statistics

| Metric              | Value |
| ------------------- | ----- |
| **Total Agents**    | 14    |
| **Total Skills**    | 40    |
| **Total Workflows** | 14    |

---

## � Critical File Dependencies

| File | Depends On | Why? |
| ---- | ---------- | ---- |
| `{FRAMEWORK_ROOT}/registry.min.json` | All `.md` files in `{FRAMEWORK_ROOT}/agents/` and `{FRAMEWORK_ROOT}/skills/` | Source of truth for paths and descriptions. |
| `{FRAMEWORK_ROOT}/GEMINI.md` | `{FRAMEWORK_ROOT}/core/*.md` | Governance and rule enforcement. |
| `ARCHITECTURE.md` | `{FRAMEWORK_ROOT}/registry.min.json` | Statistics and module overview. |
| `README.md` | `ARCHITECTURE.md` | General project overview and setup. |

---

## �🔗 Quick Reference

| Need        | Agent                 | Category       |
| ----------- | --------------------- | -------------- |
| Web App     | `frontend-specialist` | UI/UX & Growth |
| API         | `backend-specialist`  | API & Logic    |
| Discovery   | `orchestrator`        | Orchestration  |
| Efficiency  | `orchestrator`        | Orchestration  |
| Quality     | `test-engineer`       | Quality        |
