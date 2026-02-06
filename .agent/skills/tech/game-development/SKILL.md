---
name: game-development
description: Game development best practices, engine selection, and core patterns.
---

# Game Development Core Skill

## Core Philosophy

> "Games are about experience, not technology. Choose tools that serve the game, not the trend."

## Your Mindset

- **Gameplay first**: Technology serves the experience
- **Performance is a feature**: 60fps is the baseline expectation
- **Iterate fast**: Prototype before polish
- **Profile before optimize**: Measure, don't guess
- **Platform-aware**: Each platform has unique constraints

---

## 1. Platform & Engine Selection

**Selection Principles:**

| Factor | Unity | Godot | Unreal |
|--------|-------|-------|--------|
| **Best for** | Cross-platform, mobile | Indies, 2D, open source | AAA, realistic graphics |
| **Learning** | Medium | Low | High |
| **2D support** | Good | Excellent | Limited |
| **3D quality** | Good | Good | Excellent |
| **Cost** | Revenue share | Free | 5% after $1M |
| **Team size** | Any | Solo to medium | Medium to large |

**Decision Tree:**
- **2D / Web / Indie** → Godot or Phaser
- **3D / Mobile / Cross-platform** → Unity
- **AAA High-Fidelity 3D** → Unreal

---

## 2. Core Game Loop

Every game follows this cycle:
1. **Input** → Read player actions
2. **Update** → Process game logic
3. **Render** → Draw the frame

**Frame Budgets (Target 60fps):**
- **Allowable time per frame:** 16.67ms
- **Safe generic budget:** ~10ms (leaving room for overhead)

---

## 3. Critical Design Patterns

| Pattern | Use When |
|---------|----------|
| **State Machine** | Managing character states (Idle → Walk → Jump) |
| **Object Pooling** | Frequent spawning (bullets, particles) to avoid GC spikes |
| **Observer/Events** | Decoupling systems (UI listens to PlayerHP events) |
| **ECS** | Massive scale (thousands of entities) |
| **Command** | Replay systems, undo/redo, input abstraction |

---

## 4. Optimization Strategy

1. **Profile First**: Never guess. Use the engine profiler.
2. **Algo Fixes**: O(n^2) loops are the first killer.
3. **Draw Calls**: Batch meshes, use texture atlases.
4. **Memory**: Object pool everything spawned frequently.
5. **Physics**: Simplify colliders (Sphere > Box > Mesh).

## 5. Anti-Patterns

- **Optimize Prematurely**: "I need ECS for my Pong game." (No you don't).
- **Polish Before Fun**: Spending weeks on art before the core loop is fun.
- **Hardcoding**: Using magic numbers instead of exposed variables.
- **Inputs**: Checking specific keys (`if key == 'W'`) instead of actions (`if action == 'MoveForward'`).
