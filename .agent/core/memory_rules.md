# Memory Rules

## Intent
Manage the context window to prevent "token bloat" and maintain high performance.

## Rules
1.  **Pruning**: After each task completion, clear unnecessary context (e.g., `SKILL.md` content that is no longer relevant).
2.  **Summarization**: If the conversation history exceeds 20 turns, summarize the key decisions and current state.
3.  **Artifacts**: Rely on artifacts (e.g., `task.md`, `implementation_plan.md`) as the source of truth, not chat history.
4.  **No Repeats**: Do not repeat full file contents unless explicitly asked. Use diffs or summaries.
