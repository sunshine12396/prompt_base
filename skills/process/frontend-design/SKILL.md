---
name: frontend-design
description: Design thinking and decision-making for web UI. Use when designing components, layouts, color schemes, typography, or creating aesthetic interfaces. Teaches principles, not fixed values.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
references: [ux-psychology.md, color-system.md, typography-system.md, visual-effects.md, animation-guide.md, motion-graphics.md, decision-trees.md]
---

# Frontend Design System

> **Philosophy:** Every pixel has purpose. Restraint is luxury. User psychology drives decisions.
> **Core Principle:** THINK, don't memorize. ASK, don't assume.

---

## 🎯 Selective Loading Rule (MANDATORY)

**Load ONLY the reference files you need for the current task. do NOT load all files.**

| Reference File | When to Load |
|----------------|--------------|
| `references/ux-psychology.md` | **REQUIRED** for any design task. Read first. |
| `references/color-system.md` | Color selection, palette decisions, accessibility. |
| `references/typography-system.md` | Font selection, pairing, and scale decisions. |
| `references/visual-effects.md` | Shadows, gradients, texture and depth. |
| `references/animation-guide.md` | General motion design principles. |
| `references/motion-graphics.md` | Advanced: Lottie, GSAP, SVG, 3D, Particles. |
| `references/decision-trees.md` | Context-specific templates and logic. |

---

## 🔧 Runtime Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `scripts/ux_audit.py` | UX Psychology & Accessibility Audit | `python scripts/ux_audit.py <project_path>` |

---

## ⚠️ CRITICAL: ASK BEFORE ASSUMING

| Aspect | Mandatory Question |
|--------|--------------------|
| **Color** | "What color palette do you prefer? (blue/green/orange/neutral?)" |
| **Style** | "What style are you going for? (minimal/bold/retro/futuristic/organic?)" |
| **Layout** | "Do you have a layout preference? (single column/grid/asymmetric?)" |

---

## ⛔ FORBIDDEN AI DEFAULTS (ANTI-SAFE HARBOR)

- ❌ Bento Grids (unless truly complex data).
- ❌ Hero Split (Left/Right) as default.
- ❌ Mesh/Aurora Gradients.
- ❌ Simple Glassmorphism.
- ❌ Deep Cyan / Fintech Blue as "safe" escape.
- ❌ Generic Copy (Empower, Elevate, Seamless).

---

## 🎨 Design trinity

1. **60-30-10 Rule**: 60% Background, 30% Structure, 10% Accent.
2. **8-Point Grid**: All spacing in multiples of 8 (4, 8, 16, 24...).
3. **Psychology First**: Apply Hick's, Fitts', and Miller's laws before aesthetics.

---

> **Note:** This skill is focused on design thinking. For implementation technicalities, use corresponding tech skills. Refer to `references/` for detailed guidelines.
