---
name: mobile-design
description: Mobile-first design thinking and decision-making for iOS and Android apps. Touch interaction, performance patterns, platform conventions. Teaches principles, not fixed values. Use when building React Native, Flutter, or native mobile apps.
allowed-tools: Read, Glob, Grep, Bash
references: [mobile-design-thinking.md, touch-psychology.md, performance-universal.md, performance-react-native.md, performance-flutter.md, mobile-backend.md, mobile-testing.md, mobile-debugging.md, mobile-navigation.md, mobile-typography.md, mobile-color-system.md, decision-trees.md, ios-design-system.md, ios-patterns-and-components.md, android-material-3.md, android-patterns-and-components.md]
---

# Mobile Design System

> **Philosophy:** Touch-first. Battery-conscious. Platform-respectful. Offline-capable.
> **Core Principle:** Mobile is NOT a small desktop. THINK mobile constraints, ASK platform choice.

---

## 🎯 Selective Loading Rule (MANDATORY)

**Load ONLY the reference files you need for the current task.**

### 1. General Principles
| Reference File | When to Load |
|----------------|--------------|
| `references/mobile-design-thinking.md` | **Read FIRST** for any mobile task. Prevents safe desktop habits. |
| `references/touch-psychology.md` | Touch targets, gestures, thumb zone design. |
| `references/performance-universal.md` | General battery, network, and memory optimization. |
| `references/decision-trees.md` | Framework, state management, or storage selection. |

### 2. Implementation & Platform
| Reference File | When to Load |
|----------------|--------------|
| `references/ios-design-system.md` | iOS colors, typography, and HIG philosophy. |
| `references/ios-patterns-and-components.md` | iOS navigation, gestures, and native components. |
| `references/android-material-3.md` | Android Material 3, dynamic color, and M3 type scale. |
| `references/android-patterns-and-components.md` | Android navigation, FAB patterns, and Snackbars. |

### 3. Framework Specifics
| Reference File | When to Load |
|----------------|--------------|
| `references/performance-react-native.md` | Optimizing FlatList, Reanimated, and JS thread. |
| `references/performance-flutter.md` | Optimizing build methods, const widgets, and Flutter lists. |

### 4. Engineering & Lifecycle
| Reference File | When to Load |
|----------------|--------------|
| `references/mobile-backend.md` | APIs, push notifications, offline sync logic. |
| `references/mobile-testing.md` | Unit/E2E testing strategies. |
| `references/mobile-debugging.md` | Troubleshooting native or JS issues. |

---

## ⚠️ CRITICAL: ASK BEFORE ASSUMING

| Aspect | Mandatory Question |
|--------|--------------------|
| **Platform** | "iOS, Android, or both?" |
| **Framework** | "React Native, Flutter, or native (Swift/Kotlin)?" |
| **State** | "Zustand, Redux, Riverpod, or BLoC?" |

---

## ⛔ FORBIDDEN AI DEFAULTS (ANTI-PATTERNS)

- ❌ `ScrollView` for long lists (Use `FlatList` / `ListView.builder`).
- ❌ Inline `renderItem` functions (Use `useCallback` + `React.memo`).
- ❌ Touch targets < 44px (iOS) or 48px (Android).
- ❌ `AsyncStorage` for sensitive tokens (Use `SecureStore` / `KeyChain`).

---

> **Note:** This skill is a high-level orchestrator. Always load the specific `references/*.md` files for detailed implementation instructions. Use `performance-universal.md` with your specific framework reference.
