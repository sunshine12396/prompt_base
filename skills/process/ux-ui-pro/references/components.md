# Component Patterns

## Buttons

### Primary Button

```tsx
<button
  className="
  h-10 px-4 
  bg-primary text-white 
  rounded-lg font-medium
  hover:bg-primary/90 
  active:scale-[0.98]
  focus-visible:ring-2 focus-visible:ring-primary/50 focus-visible:ring-offset-2
  transition-all duration-150
  disabled:opacity-50 disabled:cursor-not-allowed
"
>
  Button Text
</button>
```

### Ghost Button

```tsx
<button
  className="
  h-10 px-4
  bg-transparent text-primary
  rounded-lg font-medium
  hover:bg-primary/10
  active:bg-primary/20
  transition-colors duration-150
"
>
  Ghost Button
</button>
```

### Icon Button

```tsx
<button
  className="
  h-10 w-10
  flex items-center justify-center
  rounded-lg
  text-muted hover:text-foreground
  hover:bg-muted/10
  transition-colors duration-150
"
  aria-label="Action description"
>
  <Icon className="h-5 w-5" />
</button>
```

## Cards

### Standard Card

```tsx
<div
  className="
  p-6 
  bg-card rounded-xl
  border border-border
  shadow-sm
"
>
  <h3 className="text-lg font-semibold">Title</h3>
  <p className="mt-2 text-muted">Description text.</p>
</div>
```

### Interactive Card

```tsx
<div
  className="
  p-6 
  bg-card rounded-xl
  border border-border
  shadow-sm
  hover:shadow-md hover:border-primary/20
  transition-all duration-200
  cursor-pointer
"
>
  <h3 className="text-lg font-semibold">Clickable Card</h3>
</div>
```

### Glass Card

```tsx
<div
  className="
  p-6 
  bg-white/10 backdrop-blur-md
  rounded-xl
  border border-white/20
"
>
  <h3 className="text-lg font-semibold text-white">Glass Card</h3>
</div>
```

## Inputs

### Text Input

```tsx
<div className="space-y-2">
  <label className="text-sm font-medium">Email</label>
  <input
    type="email"
    className="
      w-full h-10 px-3
      bg-background
      border border-border rounded-lg
      text-foreground placeholder:text-muted
      focus:outline-none focus:ring-2 focus:ring-primary/20 focus:border-primary
      transition-colors duration-150
    "
    placeholder="you@example.com"
  />
</div>
```

### Input with Error

```tsx
<div className="space-y-2">
  <label className="text-sm font-medium">Email</label>
  <input
    className="
      w-full h-10 px-3
      bg-background
      border border-red-500 rounded-lg
      text-foreground
      focus:outline-none focus:ring-2 focus:ring-red-500/20
    "
  />
  <p className="text-sm text-red-500">Please enter a valid email.</p>
</div>
```

## Badges

```tsx
{/* Status badges */}
<span className="px-2 py-1 text-xs font-medium rounded-full bg-green-100 text-green-700">
  Active
</span>

<span className="px-2 py-1 text-xs font-medium rounded-full bg-yellow-100 text-yellow-700">
  Pending
</span>

<span className="px-2 py-1 text-xs font-medium rounded-full bg-red-100 text-red-700">
  Error
</span>
```

## Modals

### Modal Container

```tsx
{
  /* Backdrop */
}
<div className="fixed inset-0 bg-black/50 backdrop-blur-sm z-50" />;

{
  /* Modal */
}
<div
  className="
  fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2
  w-full max-w-md
  p-6
  bg-card rounded-xl
  shadow-xl
  z-50
  animate-in fade-in slide-in-from-bottom-4 duration-300
"
>
  <h2 className="text-xl font-semibold">Modal Title</h2>
  <p className="mt-2 text-muted">Modal content.</p>
  <div className="mt-6 flex justify-end gap-3">
    <button className="btn-ghost">Cancel</button>
    <button className="btn-primary">Confirm</button>
  </div>
</div>;
```

## Navigation

### Top Nav

```tsx
<nav
  className="
  h-16 px-6
  flex items-center justify-between
  bg-background/80 backdrop-blur-md
  border-b border-border
  sticky top-0 z-40
"
>
  <Logo />
  <div className="flex items-center gap-6">
    <NavLinks />
    <UserMenu />
  </div>
</nav>
```

### Sidebar

```tsx
<aside
  className="
  w-64 h-screen
  p-4
  bg-card
  border-r border-border
  flex flex-col
  sticky top-0
"
>
  <Logo className="mb-8" />
  <nav className="flex-1 space-y-1">
    <SidebarLinks />
  </nav>
  <UserProfile />
</aside>
```

### Mobile Bottom Navigation (Responsive Pattern)

```tsx
<nav
  className="
  md:hidden
  fixed bottom-0 left-0 right-0
  h-16 px-6
  flex items-center justify-around
  bg-card/90 backdrop-blur-lg
  border-t border-border
  z-50
  safe-area-bottom
"
>
  <NavLink icon={<Home />} label="Home" />
  <NavLink icon={<Search />} label="Search" />
  <NavLink icon={<User />} label="Profile" />
</nav>
```

## Lists

### List Item with Hover

```tsx
<div
  className="
  p-4
  flex items-center gap-4
  hover:bg-muted/5
  rounded-lg
  cursor-pointer
  transition-colors duration-150
"
>
  <Avatar />
  <div className="flex-1 min-w-0">
    <p className="font-medium truncate">Item Title</p>
    <p className="text-sm text-muted truncate">Description</p>
  </div>
  <ChevronRight className="text-muted" />
</div>
```
