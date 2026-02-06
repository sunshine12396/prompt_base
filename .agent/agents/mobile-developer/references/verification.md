# Mobile Build & Verification Protocols

## 1. 🔴 mandatory: Build First, Declare Done Later
"It works in my head" is NOT verification. You MUST run builds before finishing a task.

## 2. Framework Build Commands
- **React Native**: `cd android && ./gradlew assembleDebug` | `npx expo run:android`
- **Flutter**: `flutter build apk --debug` | `flutter build ios --debug`

## 3. Platform Paths (User-dependent)
- **Linux**: `~/Android/Sdk`
- **macOS**: `~/Library/Android/sdk`
- **Windows**: `%LOCALAPPDATA%\Android\Sdk`

## 4. Final Build Checklist
- [ ] App builds without errors.
- [ ] No console/runtime errors on launch.
- [ ] Critical flows (Nav, Auth) verified.
- [ ] Lists performance checked (No jank).
