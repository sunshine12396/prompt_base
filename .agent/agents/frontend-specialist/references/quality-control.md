# Quality Control & Compliance

## 1. Quality Control Loop (MANDATORY)

After editing any file, you must:
1. **Run validation**: `npm run lint && npx tsc --noEmit`.
2. **Fix all errors**: TypeScript and linting must pass 100%.
3. **Verify functionality**: Test manually or run scripts if available.
4. **Report complete**: Only after quality checks pass.

---

## 2. Review Checklist

- [ ] **Accessibility**: ARIA labels, semantic HTML, keyboard accessible.
- [ ] **Performance**: GPU-accelerated animations, no waterfalls.
- [ ] **Responsive**: Mobile-first, breakpoint tested.
- [ ] **States**: Proper loading/error/empty states.
- [ ] **TypeScript**: No `any`, proper error handling.
- [ ] **Server Components**: Used wherever possible in Next.js.

---

## 3. Common Anti-Patterns (AVOID)

- ❌ **Prop Drilling**: Use composition or Context.
- ❌ **Giant Components**: Split by responsibility.
- ❌ **Premature Abstraction**: Wait for the 3rd use case.
- ❌ **Client Components by Default**: Next.js defaults should stay Server.
- ❌ **`any` Type**: Use `unknown` or specific interfaces.
- ❌ **Class Components**: Functional hooks only.
- ❌ **Swallowing Errors**: Always catch and report.

---

## 4. Security Checklist

- **Input Validation**: Mandatory Zod schemas at boundaries.
- **XSS**: No `dangerouslySetInnerHTML`.
- **Secrets**: Environment variables only.
- **SQLi**: Parameterized queries via ORM.
- **Sanitization**: Sanitize user-provided HTML.
