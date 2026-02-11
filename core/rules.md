# Tier 0: Universal Rules (Always Active)

## Clean Code (Global Mandatory)

**ALL code MUST follow rules in `skills/core/clean-code/SKILL.md`. No exceptions.**

- **Self-Documentation**: Every agent is responsible for documenting their own changes in relevant `.md` files.
- **Global Testing Mandate**: Every agent is responsible for writing and running tests for their changes.
- **Infrastructure & Safety Mandate**: Follow the "5-Phase Deployment Process".
- **Modern Tech Mandate**: Always prioritize modern, high-performance libraries and stable, next-generation frameworks (e.g., Next.js 15, Tailwind v4, Biome, Shadcn). Reject legacy or deprecated patterns.
- **Quality Gate**: Every final output MUST be reviewed by the `quality-gatekeeper`.

## File Dependency Awareness

**Before modifying ANY file:**

1. Check `ARCHITECTURE.md` → File Dependencies
2. Identify dependent files
3. Update ALL affected files together

## System Map Read

> 🔴 **MANDATORY**: Read `ARCHITECTURE.md` and `registry.min.json` at session start.

**Path Awareness:**

- Agents: `[ROOT]/agents/`
- Skills: `[ROOT]/skills/{core|tech|process|custom}/`
- Core Config: `[ROOT]/core/`
- Registry: `[ROOT]/registry.min.json`

## ⚡ Token Efficiency Protocol
- **Snippet-Only Reading**: Avoid reading full files if a summary or specific sub-item exists. Use `StartLine/EndLine`.
- **MVC (Minimal Viable Context)**: Unload skills immediately after use.
- **No Conversational Bloat**: Do not ask "The user wants X?" or apologize for errors. State the action and execute.
- **Diffs over Full Writes**: When editing, only output the necessary changes.
