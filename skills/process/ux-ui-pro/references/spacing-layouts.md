# Spacing & Layout Systems

## 8-Point Grid (Standard)

```css
:root {
  --space-0: 0;
  --space-1: 4px;    /* 0.25rem - micro */
  --space-2: 8px;    /* 0.5rem - tight */
  --space-3: 12px;   /* 0.75rem */
  --space-4: 16px;   /* 1rem - base */
  --space-5: 20px;   /* 1.25rem */
  --space-6: 24px;   /* 1.5rem - comfortable */
  --space-8: 32px;   /* 2rem - section */
  --space-10: 40px;  /* 2.5rem */
  --space-12: 48px;  /* 3rem - large */
  --space-16: 64px;  /* 4rem - hero */
  --space-20: 80px;  /* 5rem */
  --space-24: 96px;  /* 6rem - page */
}
```

## Component Sizing

### Buttons
```css
.btn-sm { height: 32px; padding: 0 12px; font-size: 14px; }
.btn-md { height: 40px; padding: 0 16px; font-size: 14px; }
.btn-lg { height: 48px; padding: 0 24px; font-size: 16px; }
.btn-xl { height: 56px; padding: 0 32px; font-size: 18px; }
```

### Inputs
```css
.input-sm { height: 32px; padding: 0 12px; }
.input-md { height: 40px; padding: 0 14px; }
.input-lg { height: 48px; padding: 0 16px; }
```

### Cards
```css
.card-compact { padding: 16px; gap: 12px; }
.card-default { padding: 24px; gap: 16px; }
.card-spacious { padding: 32px; gap: 24px; }
```

## Container Widths

```css
.container-xs { max-width: 480px; }   /* Forms, modals */
.container-sm { max-width: 640px; }   /* Blog posts */
.container-md { max-width: 768px; }   /* Content pages */
.container-lg { max-width: 1024px; }  /* Dashboards */
.container-xl { max-width: 1280px; }  /* Full layouts */
.container-2xl { max-width: 1536px; } /* Wide screens */
```

## Breakpoints

```css
/* Mobile First */
--bp-sm: 640px;   /* Small tablets */
--bp-md: 768px;   /* Tablets */
--bp-lg: 1024px;  /* Laptops */
--bp-xl: 1280px;  /* Desktops */
--bp-2xl: 1536px; /* Large screens */
```

## Common Layout Patterns

### Sidebar + Content
```css
.layout-sidebar {
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: 24px;
}

@media (max-width: 1024px) {
  .layout-sidebar {
    grid-template-columns: 1fr;
  }
}
```

### Golden Ratio Split
```css
.layout-golden {
  display: grid;
  grid-template-columns: 1fr 1.618fr;
  gap: 32px;
}
```

### Dashboard Grid
```css
.layout-dashboard {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
}
```
