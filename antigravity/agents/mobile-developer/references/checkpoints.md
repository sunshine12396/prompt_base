# Mobile Anti-Patterns & Checkpoints

## 1. 🚫 Forbidden AI Defaults (Anti-Patterns)
- **ScrollView for lists**: Use `FlatList` (RN) or `ListView.builder` (Flutter).
- **Inline renderItem**: Use `useCallback` + `React.memo`.
- **AsyncStorage for tokens**: Use `SecureStore` / `KeyChain`.
- **Hardcoded font sizes**: Use platform dynamic type scales.

## 2. 🧠 Mandatory Checkpoint
Before any coding, verify:
- **Platform**: [iOS / Android / Both]
- **Framework**: [RN / Flutter / Native]
- **Skills Read**: [List relevant skill modules loaded]

## 3. Security & UX Sins
- **Touch target < 44px**: FORBIDDEN.
- **No loading states**: FORBIDDEN.
- **Tokens in plain storage**: FORBIDDEN.
- **Logging sensitive info**: FORBIDDEN.
