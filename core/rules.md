# Tier 0: Universal Rules (Always Active)

## Clean Code (Global Mandatory)

**ALL code MUST follow rules in `skills/core/clean-code/SKILL.md`. No exceptions.**

- **Self-Documentation**: Every agent is responsible for documenting their own changes in relevant `.md` files.
- **Global Testing Mandate**: Every agent is responsible for writing and running tests for their changes.
- **Infrastructure & Safety Mandate**: Follow the "5-Phase Deployment Process".
- **Quality Gate**: Every final output MUST be reviewed by the `quality-gatekeeper`.

## File Dependency Awareness

**Before modifying ANY file:**

1. Check `CODEBASE.md` → File Dependencies
2. Identify dependent files
3. Update ALL affected files together

## System Map Read

> 🔴 **MANDATORY**: Read `ARCHITECTURE.md` and `registry.min.json` at session start.

**Path Awareness:**

- Agents: `[ROOT]/agents/`
- Skills: `[ROOT]/skills/{core|tech|process|custom}/`
- Core Config: `[ROOT]/core/`
- Registry: `[ROOT]/registry.min.json`

_(Note: [ROOT] is usually `.agent`, `prompt_base`, or `.` depending on installation. Always check for `registry.min.json` to find the root.)_
