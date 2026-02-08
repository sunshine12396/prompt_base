---
description: Execute a professional UX/UI design workflow to deliver premium, accessible, and fully responsive interfaces using the UX/UI Pro design system.
---

# `/ux-ui-pro` — Professional Design Workflow

`$ARGUMENTS`

---

## Objective

This workflow defines a structured, high-quality process for designing modern user interfaces. It ensures visual consistency, accessibility compliance, responsiveness, and a premium aesthetic across platforms.

---

## Workflow Steps

### 1. Discovery & Context

- **Analyze the Request**
  - Identify:
    - Industry (Fintech, Health, Gaming, SaaS, etc.)
    - Platform (Web, Mobile, Desktop)
    - Visual direction (Minimal, Bold, Luxury, Playful, etc.)

- **Clarify Requirements** _(ask only if missing)_
  - Target industry?
  - Light mode, dark mode, or both?
  - Mobile-first or desktop-first?
  - Primary goal (conversion, engagement, productivity)?

---

### 2. Resource Selection (Selective Loading)

- **Follow the loading protocol** in  
  `skills/process/ux-ui-pro/SKILL.md`

- **Load only required references**
  - `references/color-palettes.md` — Color systems
  - `references/typography-presets.md` — Type scales & hierarchy
  - `references/spacing-layouts.md` — Grid & spacing systems
  - `references/components.md` — UI components & patterns
  - _(Optional)_ `visual-effects.md` or `animations.md` when needed

> ⚠️ **Do not load all resources by default.** Load only what the task requires.

---

### 3. Foundation Strategy

- **Color Palette**
  - Select an industry-appropriate palette from references
  - Apply the 60-30-10 color distribution rule

- **Design Tokens**
  - Define CSS variables for:
    - Colors
    - Typography
    - Spacing
  - Use the token template from `SKILL.md`

- **Layout System**
  - Establish an 8pt grid system
  - Define breakpoints and max-widths early

---

### 4. Component & Layout Design

- **Component Creation**
  - Use standardized patterns from `components.md`
  - Ensure consistency across states (hover, focus, disabled)

- **Visual Styling**
  - Apply shadows, gradients, or glassmorphism sparingly
  - Prioritize clarity over decoration

- **Responsive Behavior**
  - **Mobile-first**
    - Fluid widths
    - Touch targets ≥ 44px
  - **Desktop**
    - Grid-based layouts
    - Controlled max-widths

---

### 5. Quality Assurance (Design Gate)

- **Accessibility**
  - WCAG 2.1 AA contrast compliance
  - Keyboard-friendly interactions
  - Clear focus states

- **Dark Mode**
  - Avoid pure black
  - Use neutral slate/gray scales

- **Anti-Pattern Review**
  - No visual noise
  - No excessive effects
  - No inconsistent spacing or typography

---

### 6. Deliverables & Handoff

- **Design Specification** (if requested)
  - Create a markdown summary of choices (Palette, Typography, Strategy)
  - Explain _why_ certain decisions were made

- **Implementation Plan** (if coding)
  - Update `index.css` or equivalent first
  - Create reusable component files
  - Assemble pages/screens

---

## Final Checklist

Before marking the task as complete, verify:

- [ ] **Context**: Is the industry & goal clear?
- [ ] **Resources**: Are only necessary references loaded?
- [ ] **Color**: Is the 60-30-10 rule applied?
- [ ] **Typography**: Is the hierarchy distinct?
- [ ] **Mobile**: Are touch targets ≥ 44px?
- [ ] **Accessibility**: Is contrast WCAG AA compliant?
- [ ] **Dark Mode**: Are backgrounds slate/gray (not black)?

---
