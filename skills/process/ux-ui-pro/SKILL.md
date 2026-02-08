---
name: ux-ui-pro
description: Advanced UI/UX design standards for "Pro" level aesthetics. Triggers on "design", "ui", "ux", "pro design", "modern interface".
references:
  [
    color-palettes.md,
    typography-presets.md,
    spacing-layouts.md,
    visual-effects.md,
    animations.md,
    components.md,
  ]
---

# UX/UI Pro - Modular Design System

> **Philosophy:** Every pixel has purpose. Restraint is luxury.

---

## 🔴 SELECTIVE LOADING (MANDATORY)

**Load ONLY the reference files you need. Do NOT load all files at once.**

| Reference File                     | When to Load                       |
| ---------------------------------- | ---------------------------------- |
| `references/color-palettes.md`     | Color selection, palette decisions |
| `references/typography-presets.md` | Font pairing, type scale           |
| `references/spacing-layouts.md`    | Layout, grid, spacing              |
| `references/visual-effects.md`     | Shadows, glass, gradients          |
| `references/animations.md`         | Motion, transitions                |
| `references/components.md`         | Button, card, input patterns       |

### Loading Protocol

```
USER: "Design a fintech dashboard"
                ↓
LOAD: color-palettes.md → Find "Finance" section
LOAD: typography-presets.md → Find "Corporate" section
LOAD: components.md → Only if implementing UI
                ↓
DO NOT LOAD: animations.md (not requested)
```

---

## 1. Quick Reference (Always Available)

### 60-30-10 Color Rule

```
60% → Background (neutral)
30% → Secondary (structure)
10% → Accent (CTAs, highlights)
```

### 8-Point Grid

```
4px → Micro gap
8px → Tight
16px → Base
24px → Comfortable
32px → Section
48px+ → Hero
```

### Typography Hierarchy

```
Display → 48-72px, weight 700+
H1 → 36-48px, weight 700
H2 → 24-30px, weight 600
Body → 16-18px, weight 400
Caption → 12-14px, weight 400-500
```

---

## 2. Project Type → Style Mapping

| Project Type    | Load These Files                                    |
| --------------- | --------------------------------------------------- |
| **Fintech/B2B** | color-palettes (Finance), typography (Corporate)    |
| **E-commerce**  | color-palettes (Retail), components                 |
| **Gaming**      | color-palettes (Gaming), visual-effects, animations |
| **Healthcare**  | color-palettes (Healthcare), spacing-layouts        |
| **Luxury**      | color-palettes (Luxury), typography (Elegant)       |
| **Startup**     | color-palettes (Corporate), typography (Tech)       |
| **Creative**    | color-palettes (Creative), visual-effects           |

---

## 3. Before Starting Any Design

**Ask user or determine from context:**

| Question                 | Why                      |
| ------------------------ | ------------------------ |
| What industry?           | Determines color palette |
| Light or dark mode?      | Foundation decision      |
| Desktop or mobile first? | Layout approach          |
| Minimal or bold?         | Typography scale         |

---

## 4. Core Principles (Memorize)

### Accessibility (WCAG AA)

- Text contrast: 4.5:1 minimum
- Large text: 3:1 minimum
- Touch targets: 44px minimum
- Focus states: Always visible

### Dark Mode

- Never pure black (#000000)
- Use rich grays (#0F172A, #111827)
- Reduce contrast slightly
- Replace shadows with glows

### Anti-Patterns (AVOID)

- ❌ Bento grids everywhere
- ❌ Mesh gradient blobs
- ❌ Purple/violet default
- ❌ Same layout every project
- ❌ Glassmorphism everywhere

### Always Responsive (Mobile-First)

- **Fluid Layouts**: Use `%`, `vw/vh`, or `fr` units. Avoid fixed `px` widths.
- **Touch Targets**: Min 44px for ALL interactive elements on mobile.
- **Text Scaling**: Use `clamp()` for fluid typography (e.g. `clamp(1rem, 5vw, 2rem)`).
- **Stacking**: Grid columns must collapse to 1 column on mobile (`grid-template-columns: 1fr`).
- **Hidden Content**: Avoid hiding core functionality on mobile; adapt it (e.g., hamburger menu).
- **Testing**: Verify: 320px (SE), 375px (iPhone), 768px (iPad), 1280px+ (Desktop).

---

## 5. Implementation

### CSS Variables Template (Copy This)

```css
:root {
  /* Load from color-palettes.md based on industry */
  --color-bg: #0f172a;
  --color-surface: #1e293b;
  --color-primary: #3b82f6;
  --color-accent: #f59e0b;
  --color-text: #f1f5f9;
  --color-muted: #94a3b8;

  /* Load from typography-presets.md */
  --font-sans: "Inter", system-ui, sans-serif;

  /* From spacing-layouts.md */
  --space-unit: 8px;

  /* From visual-effects.md */
  --radius-md: 8px;
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);

  /* From animations.md */
  --transition-base: 150ms ease-out;
}
```

---

## 6. Reference File Index

| File                    | Size   | Contents                     |
| ----------------------- | ------ | ---------------------------- |
| `color-palettes.md`     | ~2KB   | 10 industry palettes         |
| `typography-presets.md` | ~1.5KB | 6 typography systems         |
| `spacing-layouts.md`    | ~1.5KB | Grid, sizing, breakpoints    |
| `visual-effects.md`     | ~2KB   | Shadows, glass, gradients    |
| `animations.md`         | ~2KB   | Micro-interactions, loading  |
| `components.md`         | ~2.5KB | Button, card, input patterns |

---

> **Remember:** Load selectively. A fintech app doesn't need gaming colors. Premium design comes from restraint, not from loading everything.
