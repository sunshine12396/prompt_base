import os
import shutil
import sys
import argparse

def detect_target_ides(target_dir):
    """
    Detects which supported IDEs are in use.
    Returns a set of strings: {'cursor', 'antigravity'}
    
    Supported: Antigravity, Cursor
    """
    detected = set()
    
    # Antigravity detection
    # Antigravity looks for .agent/GEMINI.md automatically
    if os.path.exists(os.path.join(target_dir, ".agent")):
        detected.add('antigravity')
    
    # Cursor detection
    term_program = os.environ.get('TERM_PROGRAM', '').lower()
    if 'cursor' in term_program:
        detected.add('cursor')
    
    if os.path.exists(os.path.join(target_dir, ".cursor")) or os.path.exists(os.path.join(target_dir, ".cursorrules")):
        detected.add('cursor')
        
    return detected

def install_prompt_base(target_dir, hidden_mode=False):
    """
    Installs the Prompt Base framework into the target directory.
    Supports only Antigravity and Cursor.
    
    If hidden_mode is True, installs into .agent/ and moves helper dirs inside.
    """
    target_dir = os.path.abspath(target_dir)
    source_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    print("=" * 50)
    print("🎭 Prompt Base Installer")
    print("   Supported: Antigravity, Cursor")
    print("=" * 50)
    
    # Detect IDEs
    detected_ides = detect_target_ides(target_dir)
    
    # Always install both Antigravity and Cursor support
    # (they share the same .agent/ folder, just different entry points)
    print("✨ Installing support for: Antigravity + Cursor")

    # Determine install root
    if hidden_mode:
        install_root = os.path.join(target_dir, ".agent")
        print(f"🕵️  Hidden Mode: Installing to {install_root}")
    else:
        install_root = target_dir
        print(f"🚀 Installing to: {target_dir}")
    
    if not os.path.exists(install_root):
        os.makedirs(install_root)

    # 1. Copy Framework folder (.agent/)
    src_agent = os.path.join(source_root, ".agent")
    
    if hidden_mode:
        print("📁 Copying core framework to .agent/...")
        _copy_recursive(src_agent, install_root)
    else:
        dst_agent = os.path.join(install_root, ".agent")
        print("📁 Copying .agent/...")
        _copy_recursive(src_agent, dst_agent)

    # 2. Copy scripts and docs
    dirs_to_copy = ["docs", "scripts"]
    for d in dirs_to_copy:
        src = os.path.join(source_root, d)
        
        if hidden_mode:
            dst = os.path.join(install_root, d)
        else:
            dst = os.path.join(install_root, d)

        if os.path.exists(dst):
            print(f"⚠️  Directory {d} already exists. Merging...")
            _copy_recursive(src, dst)
        else:
            print(f"📁 Copying {d}/...")
            shutil.copytree(src, dst)

    # 3. Setup Cursor Configuration
    print("\n🔵 Setting up Cursor...")
    
    # 3.1 Create/update .cursorrules
    cursor_rules_dst = os.path.join(target_dir, ".cursorrules")
    rules_content = """# Prompt Base Configuration

> 🔴 **MANDATORY**: You MUST read `.agent/GEMINI.md` at the start of every session to understand your role and rules.

This file (`.cursorrules`) is a pointer. The actual intelligence is in:
- **Rules**: `.agent/GEMINI.md`
- **Skills**: `.agent/registry.json`
"""
    
    if os.path.exists(cursor_rules_dst):
        shutil.move(cursor_rules_dst, cursor_rules_dst + ".bak")
        print("   📄 Backed up existing .cursorrules")
    
    with open(cursor_rules_dst, 'w') as f:
        f.write(rules_content)
    print("   ✅ Created .cursorrules")

    # 3.2 Install modern .cursor/rules/
    cursor_dir_src = os.path.join(source_root, ".cursor")
    cursor_dir_dst = os.path.join(target_dir, ".cursor")
    if os.path.exists(cursor_dir_src):
        print("   📁 Installing .cursor/rules/...")
        _copy_recursive(cursor_dir_src, cursor_dir_dst)
        print("   ✅ Created .cursor/rules/prompt-base.mdc")

    # 4. Antigravity Setup (automatic via .agent/GEMINI.md)
    print("\n🟢 Antigravity support enabled automatically")
    print("   → Antigravity reads .agent/GEMINI.md on session start")

    # 5. Path Correction
    print("\n🔧 Correcting paths in documentation...")
    files_to_fix = []
    for root, _, files in os.walk(install_root):
        for file in files:
            if file.endswith(('.md', '.json')):
                files_to_fix.append(os.path.join(root, file))
    
    files_to_fix.append(os.path.join(target_dir, ".cursorrules"))
    
    for file_path in files_to_fix:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replacements
                new_content = content.replace('agent/', '.agent/')
                new_content = new_content.replace('scripts/', '.agent/scripts/')
                # Fix doubled paths
                new_content = new_content.replace('.agent/.agent/', '.agent/')
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
            except Exception as e:
                print(f"   ⚠️  Could not fix paths in {file_path}: {e}")

    # 6. Regenerate Registry
    gen_script = os.path.join(install_root, "scripts", "generate_registry.py")
    print("🔄 Updating Registry Paths...")
    try:
        import subprocess
        target_relative_root = ".agent" if hidden_mode else "agent"
        subprocess.run([sys.executable, gen_script, target_relative_root], check=True, cwd=target_dir)
        print("   ✅ Registry paths updated")
    except Exception as e:
        print(f"   ❌ Failed to update registry: {e}")

    # 7. Summary
    print("\n" + "=" * 50)
    print("🎉 Installation Complete!")
    print("=" * 50)
    print("\n📁 Installed components:")
    print("   • .agent/           → Framework core")
    print("   • .agent/GEMINI.md  → Main configuration")
    print("   • .cursorrules      → Cursor entry point")
    print("   • .cursor/rules/    → Modern Cursor rules")
    
    print("\n🚀 Next Steps:")
    print("   1. Delete this temp folder (if using make init)")
    print("   2. Open your project in Antigravity or Cursor")
    print("   3. Start with: 'What can you help me with?'")
    print("\n💡 Tip: Use /status to check framework status")

def _copy_recursive(src, dst):
    """Recursively copy files from src to dst, creating directories as needed."""
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            _copy_recursive(s, d)
        else:
            shutil.copy2(s, d)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Install Prompt Base into a target project.",
        epilog="Supported IDEs: Antigravity, Cursor"
    )
    parser.add_argument("target", nargs="?", default=".", help="Target directory (default: current)")
    parser.add_argument("--hidden", action="store_true", help="Install into .agent/ directory (Hidden Mode)")
    args = parser.parse_args()
    
    # Auto-detect hidden mode preference if .agent exists in target
    target_hidden = os.path.exists(os.path.join(args.target, ".agent"))
    use_hidden = args.hidden or target_hidden
    
    install_prompt_base(args.target, hidden_mode=use_hidden)
