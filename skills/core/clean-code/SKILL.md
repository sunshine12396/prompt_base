---
name: clean-code
description: Pragmatic coding standards - concise, direct, no over-engineering, modern tech stack
allowed-tools: Read, Write, Edit
version: 3.0
priority: CRITICAL
---

# Clean Code - Modern Development Standards

> **CRITICAL SKILL** - Write **clean, maintainable, production-ready** code using **latest technologies**.

---

## 1. Core Principles

| Principle | Rule |
|-----------|------|
| **SRP** | Single Responsibility - each function/class does ONE thing |
| **DRY** | Don't Repeat Yourself - extract duplicates, reuse |
| **KISS** | Keep It Simple - simplest solution that works |
| **YAGNI** | You Aren't Gonna Need It - don't build unused features |
| **Boy Scout** | Leave code cleaner than you found it |
| **Fail Fast** | Validate early, throw early, recover gracefully |

---

## 2. Modern Tech Stack (Priority Order)

### 2.1 Frontend Stack

| Category | Preferred | Alternative | Avoid |
|----------|-----------|-------------|-------|
| **Framework** | Next.js 15+ (App Router) | Remix, Astro | Create React App |
| **Styling** | Tailwind CSS v4 | CSS Modules | Styled-components |
| **State** | TanStack Query + Zustand | Jotai | Redux (legacy) |
| **Forms** | React Hook Form + Zod | Conform | Formik |
| **Animation** | Framer Motion | GSAP | CSS-only complex |
| **Components** | shadcn/ui + Radix | Headless UI | MUI, Ant Design |

### 2.2 Backend Stack

| Category | Preferred | Alternative | Avoid |
|----------|-----------|-------------|-------|
| **Runtime** | Bun | Node.js 22+ | Node < 20 |
| **Framework** | Hono (edge) | Fastify, Elysia | Express |
| **Validation** | Zod, Valibot | ArkType | Joi, Yup |
| **ORM** | Drizzle | Prisma | TypeORM, Sequelize |
| **Auth** | Better-Auth, Lucia | Auth.js | Passport.js |
| **API Style** | tRPC (internal), REST (public) | GraphQL | SOAP |

### 2.3 Database Stack

| Category | Preferred | Alternative | Avoid |
|----------|-----------|-------------|-------|
| **Serverless SQL** | Neon, Turso | PlanetScale | Local-only SQLite |
| **Local Dev** | SQLite + Drizzle | Docker Postgres | Manual SQL |
| **Vector DB** | pgvector | Pinecone | Weaviate |
| **Cache** | Upstash Redis | Vercel KV | Local Redis |
| **File Storage** | Cloudflare R2 | S3, Supabase | Local filesystem |

### 2.4 DevOps & Infrastructure

| Category | Preferred | Alternative | Avoid |
|----------|-----------|-------------|-------|
| **Hosting** | Vercel, Cloudflare | Railway, Fly.io | Heroku |
| **Edge** | Cloudflare Workers | Vercel Edge | Lambda (cold start) |
| **Containers** | Docker + Compose | Podman | Manual deployment |
| **CI/CD** | GitHub Actions | GitLab CI | Jenkins |
| **Monitoring** | Sentry, Axiom | Datadog | Console.log only |

### 2.5 Testing Stack

| Category | Preferred | Alternative | Avoid |
|----------|-----------|-------------|-------|
| **Unit** | Vitest | Jest | Mocha |
| **E2E** | Playwright | Cypress | Selenium |
| **API** | Bruno, Hoppscotch | Postman | curl scripts |
| **Component** | Testing Library | Enzyme | Manual testing |

---

## 3. TypeScript Standards

### 3.1 Strict Mode (MANDATORY)

```json
// tsconfig.json - MINIMUM settings
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "exactOptionalPropertyTypes": true
  }
}
```

### 3.2 Type Patterns

| Pattern | ✅ Do | ❌ Don't |
|---------|-------|---------|
| **Inference** | Let TS infer when obvious | Annotate everything |
| **any** | Never use | `any` anywhere |
| **unknown** | Use for external data | Trust external input |
| **as** | Avoid type assertions | `as Type` everywhere |
| **Generics** | Use for reusable code | Copy-paste types |
| **Zod** | Validate runtime + infer types | Manual type guards |

### 3.3 Import Organization

```typescript
// Order: external → internal → relative → types
import { useState } from 'react';           // 1. External packages
import { api } from '@/lib/api';            // 2. Internal aliases
import { Button } from './components';      // 3. Relative imports
import type { User } from '@/types';        // 4. Type imports (last)
```

---

## 4. Naming Conventions

### 4.1 General Rules

| Element | Convention | Example |
|---------|------------|---------|
| **Variables** | camelCase, descriptive | `userCount`, `isLoading` |
| **Functions** | camelCase, verb+noun | `getUserById()`, `handleSubmit()` |
| **Components** | PascalCase | `UserProfile`, `NavBar` |
| **Hooks** | use + camelCase | `useAuth`, `useLocalStorage` |
| **Constants** | SCREAMING_SNAKE | `MAX_RETRY_COUNT`, `API_URL` |
| **Types/Interfaces** | PascalCase | `User`, `ApiResponse<T>` |
| **Enums** | PascalCase + PascalCase members | `Status.Active` |
| **Files** | kebab-case or match export | `user-profile.tsx`, `Button.tsx` |

### 4.2 Boolean Naming

```typescript
// ✅ Good - Question form
const isLoading = true;
const hasPermission = false;
const canEdit = user.role === 'admin';
const shouldRefetch = staleTime > 0;

// ❌ Bad
const loading = true;
const permission = false;
const edit = true;
```

### 4.3 Function Naming

```typescript
// ✅ Good - Action + Target
function getUserById(id: string) { }
function validateEmail(email: string) { }
function handleFormSubmit(data: FormData) { }
function createPaymentIntent(amount: number) { }

// ❌ Bad - Vague
function process(data: any) { }
function doStuff() { }
function helper() { }
```

---

## 5. Function Rules

### 5.1 Size & Complexity

| Rule | Limit |
|------|-------|
| **Lines** | Max 20-30, ideal 5-15 |
| **Arguments** | Max 3, prefer 0-2 |
| **Nesting** | Max 2 levels |
| **Cyclomatic complexity** | Max 10 |

### 5.2 Guard Clauses (Early Returns)

```typescript
// ✅ Good - Guard clauses first
function processUser(user: User | null) {
  if (!user) return null;
  if (!user.isActive) return { error: 'inactive' };
  if (!user.hasPermission) return { error: 'forbidden' };
  
  // Happy path - no nesting
  return processValidUser(user);
}

// ❌ Bad - Deep nesting
function processUser(user: User | null) {
  if (user) {
    if (user.isActive) {
      if (user.hasPermission) {
        return processValidUser(user);
      }
    }
  }
  return null;
}
```

### 5.3 Pure Functions (Prefer)

```typescript
// ✅ Good - Pure function (same input → same output)
function calculateTotal(items: Item[]): number {
  return items.reduce((sum, item) => sum + item.price, 0);
}

// ❌ Bad - Side effects, mutations
function calculateTotal(items: Item[]): number {
  let total = 0;
  items.forEach(item => {
    total += item.price;
    item.processed = true; // Mutation!
  });
  globalTotal = total; // Side effect!
  return total;
}
```

---

## 6. Error Handling

### 6.1 Result Pattern (Preferred)

```typescript
// Define result types
type Result<T, E = Error> = 
  | { success: true; data: T }
  | { success: false; error: E };

// Usage
async function fetchUser(id: string): Promise<Result<User>> {
  try {
    const user = await db.users.findUnique({ where: { id } });
    if (!user) return { success: false, error: new Error('Not found') };
    return { success: true, data: user };
  } catch (error) {
    return { success: false, error: error as Error };
  }
}

// Consuming
const result = await fetchUser('123');
if (!result.success) {
  console.error(result.error.message);
  return;
}
console.log(result.data.name); // Type-safe!
```

### 6.2 Never Swallow Errors

```typescript
// ❌ Bad - Silent failure
try {
  await riskyOperation();
} catch (e) {
  // Nothing here - NEVER DO THIS
}

// ✅ Good - Handle or rethrow
try {
  await riskyOperation();
} catch (error) {
  logger.error('Operation failed', { error });
  throw new AppError('OPERATION_FAILED', { cause: error });
}
```

---

## 7. File & Folder Structure

### 7.1 Feature-Based (Recommended)

```
src/
├── features/
│   ├── auth/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── api.ts
│   │   ├── types.ts
│   │   └── index.ts
│   └── products/
│       ├── components/
│       ├── hooks/
│       └── ...
├── shared/
│   ├── components/
│   ├── hooks/
│   └── utils/
└── lib/
    ├── db.ts
    └── api.ts
```

### 7.2 Colocation Rules

| File Type | Location |
|-----------|----------|
| **Component-specific hook** | Same folder as component |
| **Component-specific types** | Same file or `.types.ts` |
| **Shared utilities** | `lib/` or `utils/` |
| **API routes** | `app/api/` (Next.js) |
| **Tests** | `__tests__/` or `.test.ts` suffix |

---

## 8. Comments & Documentation

### 8.1 When to Comment

| ✅ Comment | ❌ Don't Comment |
|-----------|-----------------|
| **Why** (business logic reason) | **What** (code already shows) |
| Complex algorithms | Obvious operations |
| Workarounds (with ticket/issue #) | Every line |
| Public API (JSDoc) | Private internals |
| Non-obvious side effects | Getters/setters |

### 8.2 JSDoc for Public APIs

```typescript
/**
 * Fetches user by ID with optional relations.
 * 
 * @param id - User's unique identifier
 * @param options - Query options
 * @returns User object or null if not found
 * @throws {AuthError} If not authenticated
 * 
 * @example
 * const user = await getUser('123', { include: ['posts'] });
 */
export async function getUser(
  id: string, 
  options?: UserQueryOptions
): Promise<User | null> {
  // ...
}
```

---

## 9. Performance Patterns

### 9.1 React Optimization

```typescript
// ✅ Server Components first (Next.js)
// Only use 'use client' when necessary

// ✅ Lazy load heavy components
const HeavyChart = lazy(() => import('./HeavyChart'));

// ✅ Memoize expensive computations
const sortedData = useMemo(() => 
  data.sort((a, b) => b.score - a.score), 
  [data]
);

// ✅ Debounce user input
const debouncedSearch = useDebouncedCallback(search, 300);
```

### 9.2 Data Fetching

```typescript
// ✅ Use TanStack Query for caching
const { data, isLoading } = useQuery({
  queryKey: ['users', userId],
  queryFn: () => fetchUser(userId),
  staleTime: 5 * 60 * 1000, // 5 minutes
});

// ✅ Parallel fetching
const [users, products] = await Promise.all([
  fetchUsers(),
  fetchProducts(),
]);

// ❌ Avoid - Waterfall requests
const users = await fetchUsers();
const products = await fetchProducts(); // Waits for users!
```

---

## 10. Security Checklist

### 10.1 Input Validation

```typescript
// ✅ Always validate with Zod
const UserSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8).max(100),
  age: z.number().int().positive().max(150),
});

// ✅ Validate at boundaries
export async function POST(req: Request) {
  const body = await req.json();
  const result = UserSchema.safeParse(body);
  
  if (!result.success) {
    return Response.json({ error: result.error }, { status: 400 });
  }
  
  // result.data is now typed and validated
}
```

### 10.2 Security Rules

| Rule | Implementation |
|------|----------------|
| **Sanitize HTML** | Use `DOMPurify` for user content |
| **SQL Injection** | Always use parameterized queries (ORM handles) |
| **XSS** | React auto-escapes, avoid `dangerouslySetInnerHTML` |
| **CSRF** | Use tokens for mutations |
| **Secrets** | Environment variables only, never commit |
| **Headers** | Set security headers (CSP, HSTS) |

---

## 11. Dependency Guidelines

### 11.1 Before Adding a Package

| Check | Action |
|-------|--------|
| **Bundle size** | Check bundlephobia.com |
| **Maintenance** | Last commit < 6 months? |
| **Downloads** | > 10k weekly? |
| **Types** | Has TypeScript types? |
| **Tree-shaking** | Supports ESM? |
| **Alternatives** | Can you write it in < 50 lines? |

### 11.2 Package Hygiene

```bash
# Check for updates
npx npm-check-updates

# Check bundle impact
npx bundle-analyzer

# Audit vulnerabilities
npm audit --production
```

---

## 12. Before Completing (MANDATORY)

### 12.1 Self-Check

| Check | Question |
|-------|----------|
| ✅ **Goal met?** | Did I do exactly what user asked? |
| ✅ **Modern stack?** | Using latest recommended tech? |
| ✅ **Type-safe?** | No `any`, proper types? |
| ✅ **No errors?** | Lint + TypeScript pass? |
| ✅ **Tested?** | Basic functionality verified? |
| ✅ **Dependencies?** | All affected files updated? |

### 12.2 Validation Commands

```bash
# TypeScript check
npx tsc --noEmit

# Lint check  
npm run lint

# Run tests
npm test

# Build check
npm run build
```

---

## 13. Quick Reference

### 13.1 File Header Template

```typescript
/**
 * @fileoverview Brief description of this file's purpose
 * @module feature/component-name
 */

'use client'; // Only if needed

import { ... } from 'react';
// ... rest of imports
```

### 13.2 Component Template

```typescript
import type { ComponentProps } from 'react';

interface ButtonProps extends ComponentProps<'button'> {
  variant?: 'primary' | 'secondary';
  isLoading?: boolean;
}

export function Button({ 
  variant = 'primary',
  isLoading = false,
  children,
  ...props 
}: ButtonProps) {
  if (isLoading) {
    return <LoadingButton />;
  }
  
  return (
    <button className={styles[variant]} {...props}>
      {children}
    </button>
  );
}
```

---

> **Remember:** Clean code is not about following rules blindly. It's about making code **easy to read, easy to change, and hard to break**. Use modern tools that help you achieve this with less effort.
