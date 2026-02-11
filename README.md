# Prompt Base (Sidekick Mode)

Prompt Base is a modular AI development framework designed to run as a **subfolder** (Sidekick) within your projects. It transforms your AI assistant into a specialized team of experts with deep domain knowledge.

## 🚀 Quick Setup

1.  **Clone** this repository into your project root as `.agent`:
    ```bash
    git clone https://github.com/sunshine12396/prompt_base .agent
    ```
2.  **Enable the AI**: Run the setup command:
    ```bash
    make -C .agent cursor
    ```

## 📖 Usage Guide

Prompt Base uses **Progressive Disclosure** (the "Librarian Protocol"). Skills remain dormant until you need them, keeping your context window clean and efficient.

### 1. How to Use Skills
You don't need to manually load skills. Simply describe what you want to do, and the orchestrator will activate the relevant skill based on your intent.

*   **Trigger**: Use keywords like "design", "build", "fix", "analyze", or specific tech stacks like "React" or "Python".
*   **Example**: "I need to design a landing page" -> Triggers `ux-ui-pro-max`
*   **Example**: "Refactor this API for performance" -> Triggers `backend-specialist` + `performance-optimizer`
*   **Example**: "Write unit tests for this module" -> Triggers `test-engineer` + `testing-patterns`

### 2. Specialized Skill: UX/UI Pro Max
This is a high-level design intelligence library for building premium interfaces. 

*   **Generate Design Systems**: Ask the AI to `Generate a design system for a [Product Type] [Industry]`.
*   **Design Tools**: The AI can search through styles, palettes, and typography pairs stored in `.agent/skills/tech/ux-ui-pro-max/assets/`.
*   **Persistence**: Use the `--persist` flag when generating designs to create a `MASTER.md` file in your `design-system/` folder. This ensures consistency as you build more pages.

### 3. Slash Commands (Workflows)
Slash commands are pre-defined automation scripts that orchestrate multiple Specialist Agents for complex tasks. They follow a logical development lifecycle:

*   **/brainstorm [topic]**
    *   **What it does**: Activates a structured exploration mode to provide at least 3 different approaches to a problem with pros, cons, and effort estimates.
    *   **When to use**: When you need to explore architectural or design options before committing to a specific implementation.
*   **/plan [task]**
    *   **What it does**: Triggers `project-planner` to analyze requirements via the Socratic Gate and generate a technical blueprint.
    *   **Output**: Creates a structured plan at `docs/PLAN-[task-slug].md`.
    *   **When to use**: Before starting any complex feature or new project. **No code is written in this mode.**
*   **/create [feature]**
    *   **What it does**: Orchestrates `App Builder` to coordinate expert agents (Database, Backend, Frontend) for full-stack implementation.
    *   **When to use**: When you're ready to build a functional prototype or a major new feature.
*   **/enhance [feature]**
    *   **What it does**: Iteratively adds or updates features in an existing application, focusing on dependency management and minimal disruption.
    *   **When to use**: For ongoing development and adding specific modules (e.g., "Add search", "Build admin panel").
*   **/test [file/feature]**
    *   **What it does**: Generates unit/integration tests following the Arrange-Act-Assert pattern, runs existing tests, or checks code coverage.
    *   **When to use**: To ensure code reliability or when fixing bugs via TDD (Test-Driven Development).
*   **/debug [issue]**
    *   **What it does**: Activates the `debugger` specialist to perform systematic root-cause analysis and evidence-based verification.
    *   **When to use**: For tricky bugs that require more than just a quick fix.
*   **/review**
    *   **What it does**: Performs a formal audit of your `staged changes` against project standards, security rules, and performance patterns.
    *   **When to use**: Right before committing code to ensure high quality and consistency.
*   **/deploy**
    *   **What it does**: Handles production deployment with mandatory pre-flight checks (linting, tests, security audit) and verification.
    *   **When to use**: When releasing a new version of the application to production or staging.
*   **/status**
    *   **What it does**: Provides a project-wide health check, showing current focus, pending tasks, and agent assignments.

### 4. Session Management FAQ
*   **Do I need to run `/init-context` every time?**  
    *   Yes, it is a recommended best practice at the start of every new conversation. This ensures the AI is immediately aligned with your specific project architecture and tech stack.
*   **Are Core Rules always active?**  
    *   Yes. The `.agent/core/` folder (including `rules.md` and `memory_rules.md`) contains **Tier 0: Universal Rules**. These act as the framework's "Operating System" and are **always active**, governing every turn to maintain safety, quality, and token efficiency.

## 🛠️ Framework Features

- **14 Specialist Agents**: Role-based AI personas (Frontend, Backend, Security, etc.).
- **40 Skills**: JIT knowledge modules (React, Go, SQL, UX, etc.).
- **⚡ Token Efficiency**: Optimized "Lean Agent Profiles" and JIT Knowledge Loading to minimize cost and maximize reasoning precision.
- **🛡️ Socratic Gate**: Mandatory clarification protocol for complex tasks to ensure intent alignment before coding.

## 🔗 Documentation

- [Architecture](ARCHITECTURE.md) - Deep dive into how the system works.
- [Governance (GEMINI.md)](GEMINI.md) - Operational rules and request classification logic.
- [Skills Guide](docs/skills-guide.md) - Detailed guide on building and customizing your own skills.
