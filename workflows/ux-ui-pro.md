---
description: Execute a professional UX/UI design workflow using the UX/UI Pro Max design intelligence system.
---

# `/ux-ui-pro` — Professional Design Workflow

`$ARGUMENTS`

---

## Objective

This workflow leverages the **UX/UI Pro Max** intelligence system to deliver premium, accessible, and fully responsive interfaces. It uses a data-driven approach to select style guides, color palettes, and typography based on the specific industry and product type.

---

## Workflow Steps

### 1. Discovery & Requirement Analysis

- **Identify Core Context**
  - **Product Type**: SaaS, e-commerce, portfolio, dashboard, etc.
  - **Industry**: Health, Fintech, Gaming, Education, etc.
  - **Keywords**: Minimal, luxury, playful, glassmorphism, bold, etc.
  - **Stack**: Default to `html-tailwind` unless specified (e.g., React, Next.js).

---

### 2. Design System Generation (Intelligence Step)

- **Execute Design System Search**
  - Run the `ux-ui-pro-max` search script to generate a comprehensive design system recommendation.
  // turbo
  - Command: `python3 skills/tech/ux-ui-pro-max/scripts/search.py "<product_type> <industry> <keywords>" --design-system -p "<Project Name>" --persist`

- **Analyze Results**
  - Review the generated `design-system/MASTER.md`.
  - Check recommended **Pattern**, **Style**, **Colors**, **Typography**, and **Key Effects**.
  - Note the **Anti-patterns** list to avoid common UI mistakes.

---

### 3. Foundation & Token Implementation

- **Set Up Global Styles**
  - Implement the recommended color palette and typography from the design system.
  - Apply the **60-30-10 color distribution** rule (60% background, 30% secondary, 10% accent/CTA).
  - Use the tokens (CSS variables) defined in `design-system/MASTER.md`.

- **Responsive Grid Foundation**
  - Establish an **8pt grid system**.
  - Set up standard breakpoints (375px, 768px, 1024px, 1440px).

---

### 4. Component Implementation

- **Build Core Components**
  - Use the `ux-ui-pro-max` stack guidelines if needed:
    `python3 skills/tech/ux-ui-pro-max/scripts/search.py "<component>" --stack <stack_name>`
  - Ensure all clickable elements have `cursor-pointer`.
  - Implement hover/focus transitions (150-300ms) as specified in the "Key Effects".

- **Visual Polish**
  - Apply effects (shadows, gradients, glassmorphism) according to the generated style guide.
  - Ensure **no emojis** are used as icons; use SVG libraries (Heroicons, Lucide).

---

### 5. Quality Gate (Pre-Delivery)

- **Accessibility Check**
  - WCAG 2.1 AA contrast compliance (minimum 4.5:1 for body text).
  - Visible focus rings and keyboard-friendly navigation.
  - `prefers-reduced-motion` support.

- **Responsive Review**
  - Verify layout at all 4 breakpoints.
  - Check touch target sizes (minimum 44x44px for mobile).
  - Ensure no horizontal scroll on mobile devices.

---

### 6. Final Delivery

- **Documentation Handoff**
  - Provide the `design-system/MASTER.md` to the user as the design source of truth.
  - Explain the reasoning behind the chosen style and hierarchy.

---

## Final Checklist

Before marking the task as complete, verify:

- [ ] **Intelligence**: Was the design system generated via `search.py --design-system`?
- [ ] **Persistence**: Is the `design-system/MASTER.md` file created?
- [ ] **Color**: Is the 60-30-10 rule applied with industry-correct colors?
- [ ] **Icons**: Are icons SVG-based (no emojis)?
- [ ] **Interaction**: Do all interactive elements have `cursor-pointer` and transitions?
- [ ] **Accessibility**: Is contrast WCAG AA compliant?
- [ ] **Responsive**: Is it verified from 375px up to 1440px?
- [ ] **Dark Mode**: If applicable, does it follow the neutrals/slate guide?

---
