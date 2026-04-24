---
name: project-memory
description: "Use when loading or managing persistent project-level context from global memory."
triggers:
  - session-start
  - "project"
  - "architecture"
  - "system overview"
  - "init-context"
---
# Project Memory & Context Loader

## Purpose
Loads pre-compiled architectural and domain context from `~/.gemini/antigravity/projects/<project-name>` to jump-start the agent with local knowledge without re-reading the entire codebase.

## Workflow
1. When triggered, identify the active project or `workspace` root path.
2. Resolve `<project-name>` by combining the parent directory and the leaf directory of the workspace path (e.g., `~/work/api` becomes `work-api`).
3. If `~/.gemini/antigravity/projects/<project-name>` exists:
   - Read `manifest.json` to verify freshness
   - Load `PROFILE.md` and `DOMAIN.md` content into `SLOT_MAP` memory slot
   - Provide summary to agent before proceeding
4. If it doesn't exist, instruct user to run `/init-context` or auto-generate `PROFILE.md` and `DOMAIN.md`.

## Memory Management
- Knowledge loaded by this skill must sit in **`SLOT_MAP`**.
- Keep only high-level conceptual knowledge loaded.
- Do not store raw code, full configs, or fast-changing data in project memory.
