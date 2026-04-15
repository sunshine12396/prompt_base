# Orchestration Workflow & Synthesis

## 1. Invocation Sequence

Logic order for complex feature implementation:
1. **explorer-agent**: Map affected areas.
2. **[domain-agent]**: Implementation or deep analysis.
3. **test-engineer**: Generate/update tests.
4. **security-auditor**: Review the changes.

---

## 2. Synthesis Report Template

Combine agent outputs into a unified report:

```markdown
## Orchestration Report: [Task Name]

### 🤖 Agents Invoked
- **agent-name**: [Key contribution]
- **agent-name**: [Key contribution]

### 🔍 Key Findings & Implementations
- Implementation detail 1 (Agent X)
- Implementation detail 2 (Agent Y)

### 🚀 Technical Decisions
- Why this approach?
- Trade-offs considered.

### 🏁 Next Steps
- [ ] Task 1
- [ ] Task 2
```

---

## 3. Communication Strategy

### Proactive Clarification
If the request is vague, ask about: **Scope, Priority, Tech Preference, Design Vision, Constraints.**

### The "No-Default" Rule
Do not use "popular" libraries (shadcn, Radix) or patterns (Bento, Hero Split) as defaults. Always ask or justify based on context.
