# Frontend Architecture & Decision Framework

## 1. State Management Hierarchy

1. **Server State** → TanStack Query (caching, deduplication).
2. **URL State** → `searchParams` (for shareable/bookmarkable states).
3. **Global State** → Zustand (only if truly global).
4. **Context** → For scoped shared state.
5. **Local State** → Default choice (`useState`).

---

## 2. Rendering Strategy (Next.js)

- **Static/Data Fetching** → Server Components (Default).
- **Interaction/Browser APIs** → Client Components.
- **Mutations** → Server Actions.
- **Progressive Rendering** → Suspense + Loading boundaries.

---

## 3. Component Decision Flow

1. **Reusable vs One-off?**
   - One-off: Co-locate.
   - Reusable: `src/shared/components`.
2. **Where does state belong?**
   - Local vs Lifted vs Context.
3. **Re-render Optimization?**
   - React.memo/useMemo/useCallback *only* after profiling.
4. **Accessibility Built-in?**
   - Semantic tags + Keyboard + SR support.

---

## 4. Expertise & Expertise Areas

### React & Next.js
- **Hooks**: Transition, DeferredValue, Custom Hooks.
- **Performance**: Code splitting, Virtualization, Bundle analysis.
- **Next.js**: App Router, Image optimization, Middleware.

### TypeScript Standards
- **Strict Mode**: `any` is forbidden.
- **Generics**: For reusable typed logic.
- **Utility Types**: `Omit`, `Pick`, `Partial`, `Awaited`.
- **Zod**: Mandatory for runtime validation + type inference.

---

## 5. Performance Optimization Mandate

- **GPU Acceleration**: Animate only `transform` and `opacity`.
- **Layout Shifts**: Prevent CLS with aspect-ratio and skeletons.
- **Bundle Hygiene**: Check bundlephobia before adding packages.
- **Parallel Fetching**: Use `Promise.all` to avoid waterfalls.
