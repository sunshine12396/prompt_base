# Prompt Base GUI Instructions

> **Guidelines for building and using Skills with a GUI interface**

---

## 📋 Overview

While standard Large Language Models (LLMs) like Gemini are powerful general-purpose tools, they lack specific project context or your team's unique standards. Loading every rule or tool into the agent's context window leads to "context bloat," higher costs, latency, and confusion.

**Prompt Base Skills** solves this through **Progressive Disclosure**. A skill is a specialized knowledge package that remains dormant until needed. This information is loaded into the agent's context only when your specific request matches the skill's description.

---

## 📁 Structure and Scope

Skills are directory-based packages. You can define scopes depending on your needs:

| Scope | Path | Description |
|-------|------|-------------|
| **Workspace** | `agent/skills/` | Available only within a specific project |

### Skill Directory Structure

```
my-skill/
├── SKILL.md      # (Required) Metadata & instructions
├── scripts/      # (Optional) Python or Bash scripts
├── references/   # (Optional) Text, documentation, templates
└── assets/       # (Optional) Images or logos
```

---

## 🔍 Example 1: Code Review Skill

This is an instruction-only skill, requiring only a `SKILL.md` file.

### Step 1: Create Directory

```bash
mkdir -p agent/skills/process/code-review
```

### Step 2: Create SKILL.md

```markdown
---
name: code-review
description: Reviews code changes for bugs, style issues, and best practices. Use when reviewing PRs or checking code quality.
---

# Code Review Skill

When reviewing code, follow these steps:

## Review checklist

1. **Correctness**: Does the code do what it's supposed to?
2. **Edge cases**: Are error conditions handled?
3. **Style**: Does it follow project conventions?
4. **Performance**: Are there obvious inefficiencies?

## How to provide feedback

- Be specific about what needs to change
- Explain why, not just what
- Suggest alternatives when possible
```

> **Note**: The `SKILL.md` file contains metadata (name, description) at the top, followed by instructions. The Agent will only read the metadata and load instructions when necessary.

### Try It Out

Create `demo_bad_code.py`:

```python
import time

def get_user_data(users, id):
    # Find user by ID
    for u in users:
        if u['id'] == id:
            return u
    return None

def process_payments(items):
    total = 0
    for i in items:
        # Calculate tax
        tax = i['price'] * 0.1
        total = total + i['price'] + tax
        time.sleep(0.1)  # Simulate slow network call
    return total

def run_batch():
    users = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    items = [{'price': 10}, {'price': 20}, {'price': 100}]
    
    u = get_user_data(users, 3)
    print("User found: " + u['name'])  # Will crash if None
    
    print("Total: " + str(process_payments(items)))

if __name__ == "__main__":
    run_batch()
```

**Prompt**: `review the @demo_bad_code.py file`

The Agent will automatically identify the `code-review` skill, load the information, and follow the instructions.

---

## 📄 Example 2: License Header Skill

This skill uses a reference file in a `resources/` directory.

### Step 1: Create Directory

```bash
mkdir -p agent/skills/custom/license-header-adder/resources
```

### Step 2: Create Template File

**`agent/skills/custom/license-header-adder/resources/HEADER.txt`**:

```
/*
 * Copyright (c) 2026 YOUR_COMPANY_NAME LLC.
 * All rights reserved.
 * This code is proprietary and confidential.
 */
```

### Step 3: Create SKILL.md

**`agent/skills/custom/license-header-adder/SKILL.md`**:

```markdown
---
name: license-header-adder
description: Adds the standard corporate license header to new source files.
---

# License Header Adder

This skill ensures that all new source files have the correct copyright header.

## Instructions

1. **Read the Template**: Read the content of `resources/HEADER.txt`.
2. **Apply to File**: When creating a new file, prepend this exact content.
3. **Adapt Syntax**: 
   - For C-style languages (Java, TS), keep the `/* */` block.
   - For Python/Shell, convert to `#` comments.
```

### Try It Out

**Prompt**: `Create a new Python script named data_processor.py that prints 'Hello World'.`

The Agent will read the template, convert comments to Python style, and automatically add the header to the file.

---

## 🎯 Conclusion

By creating Skills, you transform a general-purpose AI model into an expert for your project:

- ✅ Systemize best practices
- ✅ Adhere to code review rules
- ✅ Automatically add license headers
- ✅ Agent automatically knows how to work with your team

Instead of constantly reminding the AI to "remember to add license" or "fix commit format," the Agent will now do it automatically!