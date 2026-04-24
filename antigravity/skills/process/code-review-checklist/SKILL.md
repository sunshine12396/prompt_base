---
name: code-review-checklist
description: "Use when completing tasks, implementing major features, or before merging to verify work meets requirements and code quality standards."
allowed-tools: Read, Glob, Grep, Bash
---

# Requesting Code Review

## Overview

Dispatch a code reviewer to catch issues before they cascade. The reviewer gets precisely crafted context — never your session's history.

**Core principle:** Review early, review often. Two stages: spec compliance first, then code quality.

## When to Request Review

**Mandatory:**
- After each task in subagent-driven development
- After completing major feature
- Before merge to main

**Optional but valuable:**
- When stuck (fresh perspective)
- Before refactoring (baseline check)
- After fixing complex bug

## Two-Stage Review Process

```
Stage 1: SPEC COMPLIANCE
  → Did we build what was requested? Nothing more, nothing less?
  → ✅ Pass → Stage 2
  → ❌ Fail → Fix → Re-review Stage 1

Stage 2: CODE QUALITY
  → Is the implementation well-built? Clean, tested, maintainable?
  → ✅ Pass → Proceed
  → ❌ Fail → Fix → Re-review Stage 2
```

**CRITICAL: Never start Stage 2 before Stage 1 passes.**

## How to Request

**1. Get git SHAs:**
```bash
BASE_SHA=$(git rev-parse HEAD~1)  # or origin/main
HEAD_SHA=$(git rev-parse HEAD)
```

**2. Dispatch reviewer with context:**
- `{WHAT_WAS_IMPLEMENTED}` — What you just built
- `{PLAN_OR_REQUIREMENTS}` — What it should do
- `{BASE_SHA}` — Starting commit
- `{HEAD_SHA}` — Ending commit

**3. Act on feedback:**
- Fix Critical issues immediately
- Fix Important issues before proceeding
- Note Minor issues for later
- Push back if reviewer is wrong (with reasoning)

## Quick Review Checklist

### Spec Compliance
- [ ] All requirements from the plan implemented
- [ ] Nothing extra built that wasn't requested (YAGNI)
- [ ] No requirements misinterpreted
- [ ] Edge cases from spec handled

### Code Quality
- [ ] Clear naming — intent obvious from names
- [ ] DRY — no duplicate code
- [ ] SOLID principles followed
- [ ] Error handling in place
- [ ] No hardcoded secrets or sensitive credentials
- [ ] Input validated and sanitized
- [ ] No SQL/NoSQL injection vulnerabilities

### Testing
- [ ] Unit tests for new code
- [ ] Edge cases tested
- [ ] Tests verify behavior, not mocks
- [ ] All tests pass (verified, not assumed)

### Documentation
- [ ] Complex logic commented
- [ ] Public APIs documented
- [ ] README updated if needed

## Review Comments Guide

```
🔴 CRITICAL: Must fix before proceeding (security, data loss, broken functionality)
🟡 IMPORTANT: Should fix before proceeding (bugs, missing edge cases)
🟢 MINOR: Nice to have (naming, style, minor improvements)
❓ QUESTION: Needs clarification before deciding
```

## Anti-Patterns to Flag

```typescript
// ❌ Magic numbers
if (status === 3) { ... }
// ✅ Named constants
if (status === Status.ACTIVE) { ... }

// ❌ Deep nesting
if (a) { if (b) { if (c) { ... } } }
// ✅ Early returns
if (!a) return;
if (!b) return;

// ❌ any type
const data: any = ...
// ✅ Proper types
const data: UserData = ...
```

## Red Flags

**Never:**
- Skip review because "it's simple"
- Ignore Critical issues
- Proceed with unfixed Important issues
- Start quality review before spec compliance passes

**If reviewer wrong:**
- Push back with technical reasoning
- Show code/tests that prove it works
- Request clarification
