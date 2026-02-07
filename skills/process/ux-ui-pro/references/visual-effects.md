# Visual Effects Library

## Shadow System

### Light Mode Shadows
```css
--shadow-xs: 0 1px 2px rgba(0, 0, 0, 0.05);
--shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.1), 0 1px 2px rgba(0, 0, 0, 0.06);
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
--shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
--shadow-2xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
```

### Dark Mode Shadows (Glow)
```css
--glow-sm: 0 0 10px rgba(255, 255, 255, 0.1);
--glow-md: 0 0 20px rgba(255, 255, 255, 0.15);
--glow-lg: 0 0 30px rgba(255, 255, 255, 0.2);
--glow-primary: 0 0 20px rgba(59, 130, 246, 0.5);
--glow-accent: 0 0 20px rgba(245, 158, 11, 0.5);
```

### Colored Shadows
```css
--shadow-primary: 0 4px 14px rgba(59, 130, 246, 0.4);
--shadow-success: 0 4px 14px rgba(34, 197, 94, 0.4);
--shadow-warning: 0 4px 14px rgba(245, 158, 11, 0.4);
--shadow-error: 0 4px 14px rgba(239, 68, 68, 0.4);
```

## Border Radius

```css
--radius-none: 0;
--radius-sm: 4px;
--radius-md: 8px;
--radius-lg: 12px;
--radius-xl: 16px;
--radius-2xl: 24px;
--radius-full: 9999px;
```

## Glassmorphism

### Standard Glass
```css
.glass {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}
```

### Dark Glass
```css
.glass-dark {
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.1);
}
```

### Frosted Glass
```css
.glass-frosted {
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.3);
}
```

## Gradients

### Linear Gradients
```css
/* Subtle */
--gradient-subtle: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Warm */
--gradient-warm: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);

/* Cool */
--gradient-cool: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);

/* Dark */
--gradient-dark: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 100%);

/* Mesh (use sparingly) */
--gradient-mesh: radial-gradient(at 40% 20%, #4f46e5 0px, transparent 50%),
                 radial-gradient(at 80% 0%, #f472b6 0px, transparent 50%),
                 radial-gradient(at 0% 50%, #22d3ee 0px, transparent 50%);
```

### Text Gradients
```css
.text-gradient {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

## Borders

```css
/* Subtle */
--border-subtle: 1px solid rgba(0, 0, 0, 0.05);

/* Default */
--border-default: 1px solid rgba(0, 0, 0, 0.1);

/* Strong */
--border-strong: 1px solid rgba(0, 0, 0, 0.2);

/* Dark mode */
--border-dark-subtle: 1px solid rgba(255, 255, 255, 0.05);
--border-dark-default: 1px solid rgba(255, 255, 255, 0.1);
--border-dark-strong: 1px solid rgba(255, 255, 255, 0.2);
```

## Transitions

```css
--transition-fast: 100ms ease-out;
--transition-base: 150ms ease-out;
--transition-slow: 300ms ease-out;
--transition-slower: 500ms ease-out;

/* Spring */
--transition-spring: 500ms cubic-bezier(0.34, 1.56, 0.64, 1);

/* Bounce */
--transition-bounce: 600ms cubic-bezier(0.68, -0.55, 0.265, 1.55);
```
