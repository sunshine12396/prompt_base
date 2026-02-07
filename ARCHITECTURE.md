# Prompt Base Architecture

## 📋 Overview

Prompt Base is a modular system consisting of:

- **19 Specialist Agents** - Role-based AI personas
- **44 Skills** - Categorized knowledge modules
- **13 Workflows** - Slash command procedures

---

## 🏗️ Directory Structure (Sidekick Mode)

Prompt Base lives in a hidden subfolder (`.agent/`) within your project.

```
<project-root>/
├── .agent/               # Framework Subfolder (Cloned here)
│   ├── core/             # Global rules and orchestration logic
│   ├── agents/           # 19 Specialist Agents
│   ├── skills/           # Categorized Skills
│   ├── workflows/        # Slash commands
│   ├── registry.min.json # Unified metadata index
│   └── GEMINI.md         # Global governance
├── .cursorrules          # Pointer to .agent/GEMINI.md
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

## 🤖 Agents (19)

| Category            | Agents                                                                                             |
| ------------------- | -------------------------------------------------------------------------------------------------- |
| **Core**            | `orchestrator`, `project-planner`, `explorer-agent`, `skill-librarian`, `context-architect`        |
| **Dev**             | `frontend-specialist`, `backend-specialist`, `mobile-developer`, `game-developer`                  |
| **Quality**         | `test-engineer`, `debugger`, `performance-optimizer`, `documentation-writer`, `quality-gatekeeper` |
| **Infra/Sec**       | `devops-engineer`, `security-auditor`, `penetration-tester`, `database-architect`                  |
| **Growth & Search** | `seo-specialist`                                                                                   |

---

## 🧠 Skills (40)

### Core

| Skill                | Description               |
| -------------------- | ------------------------- |
| `clean-code`         | Coding standards          |
| `brainstorming`      | Socratic discovery        |
| `plan-writing`       | Task breakdown            |
| `architecture`       | System design             |
| `skill-loading`      | JIT Knowledge discovery   |
| `context-management` | Context efficiency (MVC)  |
| `reasoning`          | Deductive problem-solving |

### Technology

| Category    | Skills                                                                              |
| ----------- | ----------------------------------------------------------------------------------- |
| **Web**     | `react-patterns`, `nextjs-best-practices`, `tailwind-patterns`, `typescript-expert` |
| **Backend** | `nodejs-best-practices`, `python-patterns`, `prisma-expert`, `nestjs-expert`        |
| **Mobile**  | `mobile-design`                                                                     |
| **Other**   | `database-design`, `docker-expert`, `game-development`                              |

### Process

- `testing-patterns`, `tdd-workflow`, `vulnerability-scanner`, `automation-testing`.
- `seo-fundamentals`, `geo-fundamentals`, `i18n-localization`.
- `bash-linux`, `powershell-windows`, `server-management`.

---

## 🔄 Workflows (10)

| Command         | Description                   |
| --------------- | ----------------------------- |
| `/brainstorm`   | Socratic discovery            |
| `/create`       | Create new features           |
| `/debug`        | Debug issues                  |
| `/deploy`       | Deploy application            |
| `/enhance`      | Improve existing code         |
| `/orchestrate`  | Multi-agent coordination      |
| `/plan`         | Task breakdown                |
| `/preview`      | Preview changes               |
| `/status`       | Check project status          |
| `/test`         | Run tests                     |
| `/init-context` | Initialize MVC                |
| `/deep-solve`   | JIT Knowledge workflow        |
| `/restructure`  | Maintenance & registry update |

---

## 📊 Statistics

| Metric              | Value |
| ------------------- | ----- |
| **Total Agents**    | 19    |
| **Total Skills**    | 44    |
| **Total Workflows** | 13    |

---

## 🔗 Quick Reference

| Need        | Agent                 | Category       |
| ----------- | --------------------- | -------------- |
| Web App     | `frontend-specialist` | UI/UX & Growth |
| API         | `backend-specialist`  | API & Logic    |
| JIT Loading | `skill-librarian`     | Discovery      |
| Context     | `context-architect`   | Efficiency     |
| Quality     | `quality-gatekeeper`  | Final Review   |
