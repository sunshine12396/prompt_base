# Typography Presets

## 🏢 Corporate / Professional
```css
:root {
  --font-heading: 'Inter', system-ui, sans-serif;
  --font-body: 'Inter', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  
  /* Scale: 1.25 (Major Third) */
  --text-xs: 0.75rem;    /* 12px */
  --text-sm: 0.875rem;   /* 14px */
  --text-base: 1rem;     /* 16px */
  --text-lg: 1.25rem;    /* 20px */
  --text-xl: 1.563rem;   /* 25px */
  --text-2xl: 1.953rem;  /* 31px */
  --text-3xl: 2.441rem;  /* 39px */
  --text-4xl: 3.052rem;  /* 49px */
}
```

## 🎨 Creative / Bold
```css
:root {
  --font-heading: 'Outfit', sans-serif;
  --font-body: 'DM Sans', sans-serif;
  --font-mono: 'Fira Code', monospace;
  
  /* Scale: 1.333 (Perfect Fourth) */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.333rem;
  --text-xl: 1.777rem;
  --text-2xl: 2.369rem;
  --text-3xl: 3.157rem;
  --text-4xl: 4.209rem;
}
```

## 📰 Editorial / Content
```css
:root {
  --font-heading: 'Playfair Display', serif;
  --font-body: 'Source Serif Pro', serif;
  --font-mono: 'IBM Plex Mono', monospace;
  
  /* Scale: 1.2 (Minor Third) */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1.125rem;  /* 18px for readability */
  --text-lg: 1.35rem;
  --text-xl: 1.62rem;
  --text-2xl: 1.944rem;
  --text-3xl: 2.333rem;
  --text-4xl: 2.799rem;
}
```

## 🚀 Tech / Startup
```css
:root {
  --font-heading: 'Geist', system-ui, sans-serif;
  --font-body: 'Geist', system-ui, sans-serif;
  --font-mono: 'Geist Mono', monospace;
  
  /* Scale: 1.25 */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.25rem;
  --text-xl: 1.5rem;
  --text-2xl: 1.875rem;
  --text-3xl: 2.25rem;
  --text-4xl: 3rem;
}
```

## 💎 Luxury / Elegant
```css
:root {
  --font-heading: 'Cormorant Garamond', serif;
  --font-body: 'Lato', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  
  /* Scale: 1.618 (Golden Ratio) */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.618rem;
  --text-xl: 2.618rem;
  --text-2xl: 4.236rem;
  --text-3xl: 6.854rem;
  --text-4xl: 11.089rem;
}
```

## 📱 Mobile-First / Compact
```css
:root {
  --font-heading: 'Plus Jakarta Sans', sans-serif;
  --font-body: 'Plus Jakarta Sans', sans-serif;
  --font-mono: 'Fira Code', monospace;
  
  /* Scale: 1.125 (Major Second) - Compact */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.266rem;
  --text-2xl: 1.424rem;
  --text-3xl: 1.602rem;
  --text-4xl: 1.802rem;
}
```

## Line Heights & Letter Spacing

```css
/* Body text */
.body { line-height: 1.6; letter-spacing: 0; }

/* Headings */
.heading { line-height: 1.2; letter-spacing: -0.02em; }

/* Display (large) */
.display { line-height: 1.1; letter-spacing: -0.03em; }

/* Small/Caption */
.caption { line-height: 1.4; letter-spacing: 0.02em; }

/* Mono/Code */
.code { line-height: 1.5; letter-spacing: 0; }
```
