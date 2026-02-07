# PLAN: Sidekick Integration Support

> Goal: Allow "Just Clone" integration where the framework lives in a subfolder without being copied/deleted.

## 📋 Objectives

1. Support for **Framework-as-a-Subfolder** (Sidekick Mode).
2. Keep paths in `registry.min.json` correct relative to the Workspace Root.
3. Seamless integration for Antigravity and Cursor.

## 🛠️ Proposed Changes

### 1. `scripts/generate_registry.py` Enhancements

- Detect the "base path" of the framework relative to the current working directory.
- Allow generating paths prefixed with the current folder name if integrated as a subfolder.

### 2. New `bridge.sh` (or `setup.sh`)

- A simple interactive script to "bridge" the subfolder to the root.
- Actions:
  - Symlink `prompt_base` (or current folder) to `.agent`.
  - Create/Append to `.cursorrules` in the parent directory.
  - Create modern `.cursor/rules/` in the parent directory.

### 3. `GEMINI.md` Path Normalization

- Update "Universal Rules" to be aware that files might be in a subfolder.
- Define a "Search Order" for paths.

### 4. `Makefile` Updates

- Add `make sidekick` command to perform the bridge actions.

## 🔄 User Workflow (New)

```bash
cd my-project
git clone https://github.com/sunshine12396/prompt_base
cd prompt_base
make sidekick  # Bridges to global project
```

## 🏗️ Technical Details

### Registry Paths

If `prompt_base` is at `./libs/pb`, `registry.min.json` paths should be `libs/pb/skills/...`.
The `generate_registry.py` will:

1. Find its own root.
2. Determine its path relative to the process CWD (Workspace Root).
3. Prefix all paths in `registry.min.json` accordingly.

### Antigravity Support

Antigravity looks for `.agent/GEMINI.md`.
The `sidekick` command will create a symlink: `ln -s prompt_base .agent`.
This is the "Zero-Copy" way to support Antigravity while keeping the folder.

### Cursor Support

The `sidekick` command will write a `.cursorrules` to `../.cursorrules` that points to the subfolder.

---

## 📅 Task List

- [ ] Modify `generate_registry.py` to support path prefixing.
- [ ] Create `scripts/bridge.py` to handle symlinking and rule creation in parent dir.
- [ ] Update `Makefile` with `make sidekick` and `make integrate` (aliased).
- [ ] Update `GEMINI.md` with "Sidekick Mode" instructions.
- [ ] Update `docs/INTEGRATION.md` to document the new "Clone-n-Bridge" method.
