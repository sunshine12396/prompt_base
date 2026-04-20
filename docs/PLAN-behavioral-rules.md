# PLAN-behavioral-rules.md: Behavioral Excellence Integration

Integration of `CLAUDE.md` behavioral guidelines into the `prompt_base` project core.

## 🎯 Objectives
- Implement "Think Before Coding", "Simplicity First", "Surgical Changes", and "Goal-Driven Execution".
- Ensure rules are project-local but integrated into the TIER 0/TIER 1 hierarchy.
- Maintain the "Fix immediately and document" override for adjacent bugs.

## 🛠️ Proposed Changes

### 1. `core/rules.md` (Local)
- **Add Section**: `## 🧠 Intellectual Integrity (Think Before Coding)`
  - Explicit assumptions, surfacing tradeoffs, and pushing back on complexity.
- **Enhance `## Clean Code`**:
  - Add "Simplicity First" (Minimum code, no speculative abstractions).
- **Add Section**: `## ✂️ Surgical Changes & Adjacent Integrity`
  - Touch only what's necessary. 
  - **Override**: If adjacent bugs/vulnerabilities are found, fix immediately and document.
- **Enhance `## Global Testing Mandate`**:
  - Transform into `## 🎯 Goal-Driven Execution`.
  - Define success criteria BEFORE coding.

### 2. `GEMINI.md` (Local)
- Update **Core Logic Files** table to refer to local `./core/` paths.
- Add a summary of Behavioral Excellence to TIER 0 summary.

## ✅ Verification Plan
- **Self-Audit**: Check that new rules do not contradict existing TIER 0 safety rules.
- **Reference Check**: Ensure paths in `GEMINI.md` correctly point to the local overrides.
