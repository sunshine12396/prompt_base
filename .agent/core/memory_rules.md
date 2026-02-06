# Memory & Context Slot System

## 🎯 Intent
Prevent "token bloat" and maintain reasoning precision by enforcing a strictly modular context window.

## 📥 Slot Management (QUOTA: 1 per Slot)
To prevent rules from bleeding into each other, the AI MUST manage its memory using these "Slots":

| Slot Label | Domain Coverage |
|------------|-----------------|
| `SLOT_UX`  | Frontend, Mobile Design, UI, Styling, UX Psychology. |
| `SLOT_APP` | Business Logic, API, Backend, TypeScript Expert, Python Patterns. |
| `SLOT_OPS` | Docker, DevOps, CI/CD, Security, Cloud Infra. |
| `SLOT_QA`  | Unit Testing, E2E, Quality Gates, Debugging logs. |
| `SLOT_MAP` | Registry, Architecture, Plan, Task status. (Permanently Fixed) |

---

## 🏗️ The Slot Protocol (MANDATORY)

1. **Activation**: When loading a skill, assign it to a slot (e.g., "Loading `mobile-design` into `SLOT_UX`").
2. **Conflict Check**: If a slot is occupied, you MUST declare an `UNLOAD` before loading the new skill.
   - *Example*: "Unloading `frontend-design` from `SLOT_UX` to load `mobile-design`."
3. **Sub-task Pruning**: Once a specific sub-task (e.g., "Style the button") ends, immediately clear the reference materials from that slot.
4. **Context Summary**: Every 5 tool calls, verify if current loaded skills are still needed. If not, PRUNE.

---

## 🧹 General Memory Rules
1. **No Repeats**: Do not repeat full file contents. Use diffs.
2. **Artifact Truth**: Rely on `PLAN.md` and `task.md` for state, not chat history.
3. **History Summarization**: If history > 20 turns, stop and provide a "Context Snapshot".
