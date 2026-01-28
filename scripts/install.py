import os
import shutil
import sys
import argparse

def detect_target_ides(target_dir):
    """
    Detects which IDEs are in use by checking environment variables and target directory files.
    Returns a set of strings: {'cursor', 'vscode', ...}
    """
    detected = set()
    
    # 1. Environment Detection (Smart)
    term_program = os.environ.get('TERM_PROGRAM', '').lower()
    if 'cursor' in term_program:
        detected.add('cursor')
    elif 'vscode' in term_program:
        detected.add('vscode')

    # 2. File Marker Detection (Persistent)
    # Check for Cursor
    if os.path.exists(os.path.join(target_dir, ".cursor")) or os.path.exists(os.path.join(target_dir, ".cursorrules")):
        detected.add('cursor')
    
    # Check for VSCode
    if os.path.exists(os.path.join(target_dir, ".vscode")):
        detected.add('vscode')
        
    return detected

def install_prompt_base(target_dir, hidden_mode=False):
    """
    Installs the Prompt Base framework into the target directory.
    If hidden_mode is True, installs into .agent/ and moves helper dirs inside.
    """
    target_dir = os.path.abspath(target_dir)
    source_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Detect IDEs
    detected_ides = detect_target_ides(target_dir)
    
    # Default to ALL if nothing detected (safe fallback for new projects)
    if not detected_ides:
        should_install_cursor = True
        should_install_vscode = True
        print("ℹ️  No specific IDE detected. Installing support for ALL IDEs.")
    else:
        should_install_cursor = 'cursor' in detected_ides
        should_install_vscode = 'vscode' in detected_ides
        print(f"✨ Detected IDEs: {', '.join(detected_ides).upper()}")

    # Determine install root
    if hidden_mode:
        install_root = os.path.join(target_dir, ".agent")
        print(f"🕵️  Hidden Mode Enabled. Installing to: {install_root}")
    else:
        # Default behavior: agent/ at root, scripts/ at root, docs/ at root
        install_root = target_dir
        print(f"🚀 Installing Prompt Base to: {target_dir}")
    
    if not os.path.exists(install_root):
        os.makedirs(install_root)

    # 1. Copy Framework folder
    # Source is now '.agent'
    src_agent = os.path.join(source_root, ".agent")
    
    if hidden_mode:
        # We are installing INTO .agent, so we copy content of .agent/ into .agent/
        print(f"✅ Copying core framework to .agent/...")
        _copy_recursive(src_agent, install_root)
    else:
        # Normal mode: still uses .agent for the folder name
        dst_agent = os.path.join(install_root, ".agent")
        print(f"✅ Copying .agent/...")
        _copy_recursive(src_agent, dst_agent)

    # 2. Copy scripts and docs
    # In hidden mode: they go INSIDE .agent/scripts and .agent/docs
    # In normal mode: they go to target/scripts and target/docs
    
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
            print(f"✅ Copying {d}...")
            shutil.copytree(src, dst)

    # 3. Handle Cursor Configuration (.cursorrules and .cursor/rules)
    if should_install_cursor:
        cursor_rules_src = os.path.join(source_root, ".cursorrules")
        cursor_rules_dst = os.path.join(target_dir, ".cursorrules")
        
        # 3.1 Legacy .cursorrules
        if os.path.exists(cursor_rules_src):
            if hidden_mode:
                rules_content = "# Prompt Base (Hidden Mode)\n"
                rules_content += "ALWAYS Reference: .agent/GEMINI.md\n"
                
                if os.path.exists(cursor_rules_dst):
                    shutil.move(cursor_rules_dst, cursor_rules_dst + ".bak")
                
                with open(cursor_rules_dst, 'w') as f:
                    f.write(rules_content)
            else:
                if os.path.exists(cursor_rules_dst):
                     shutil.copy2(cursor_rules_dst, cursor_rules_dst + ".bak")
                shutil.copy2(cursor_rules_src, cursor_rules_dst)
            print("✅ Installed .cursorrules")

        # 3.2 Modern .cursor/rules/
        cursor_dir_src = os.path.join(source_root, ".cursor")
        cursor_dir_dst = os.path.join(target_dir, ".cursor")
        if os.path.exists(cursor_dir_src):
            print("✅ Installing modern Cursor Rules (.cursor/rules)...")
            _copy_recursive(cursor_dir_src, cursor_dir_dst)
    else:
        print("⏩ Skipping Cursor configuration (not detected)")

    # 4. VSCode Setup
    instructions_file = None # Initialize for path fixer
    
    if should_install_vscode:
        vscode_dir = os.path.join(target_dir, ".vscode")
        vscode_dir_src = os.path.join(source_root, ".vscode")
        if not os.path.exists(vscode_dir):
            os.makedirs(vscode_dir)
        
        # Copy settings.json if it exists in source
        settings_src = os.path.join(vscode_dir_src, "settings.json")
        settings_dst = os.path.join(vscode_dir, "settings.json")
        if os.path.exists(settings_src):
            if os.path.exists(settings_dst):
                 shutil.copy2(settings_dst, settings_dst + ".bak")
            shutil.copy2(settings_src, settings_dst)
            print("✅ Installed .vscode/settings.json")

        instructions_file = os.path.join(vscode_dir, "ai_instructions.md")
        if not os.path.exists(instructions_file):
            ref_path = ".agent/GEMINI.md"
            reg_path = ".agent/registry.json"
            
            with open(instructions_file, "w") as f:
                f.write("# Prompt Base Instructions\n\n")
                f.write("You are an AI assistant using the Prompt Base framework.\n")
                f.write(f"ALWAYS read '{ref_path}' before starting any task.\n")
                f.write(f"Use '{reg_path}' to find specialized skills.\n")
            print("✅ Created .vscode/ai_instructions.md")
    else:
        print("⏩ Skipping VSCode configuration (not detected)")

    # 5. Path Correction (Hidden Mode)
    # We always perform correction now to ensure no bare "agent/" paths exist
    print("🔧 Correcting paths in documentation...")
    # We need to replace "agent/" with ".agent/" and "scripts/" with ".agent/scripts/"
    # across all .md and .json files in the install_root and target .cursorrules
    
    files_to_fix = []
    for root, _, files in os.walk(install_root):
        for file in files:
            if file.endswith(('.md', '.json')):
                files_to_fix.append(os.path.join(root, file))
    
    # Also fix the target .cursorrules and ai_instructions.md if they were installed
    if should_install_cursor:
        files_to_fix.append(os.path.join(target_dir, ".cursorrules")) # Re-derive path
    
    if instructions_file and os.path.exists(instructions_file):
        files_to_fix.append(instructions_file)
    
    for file_path in files_to_fix:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replacements
                new_content = content.replace('agent/', '.agent/')
                new_content = new_content.replace('scripts/', '.agent/scripts/')
                # Fix cases where it might have doubled up if already partially correct
                new_content = new_content.replace('.agent/.agent/', '.agent/')
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
            except Exception as e:
                print(f"⚠️  Could not fix paths in {file_path}: {e}")

    # 6. Regenerate Registry (Crucial for Paths)
    gen_script = os.path.join(install_root, "scripts", "generate_registry.py")
    print("🔄 Updating Registry Paths...")
    try:
        import subprocess
        # Run from target_dir so paths are relative to project root
        target_relative_root = ".agent" if hidden_mode else "agent"
        subprocess.run([sys.executable, gen_script, target_relative_root], check=True, cwd=target_dir)
        print("✅ Registry paths updated.")
    except Exception as e:
        print(f"❌ Failed to update registry: {e}")

    print("\n🎉 Installation Complete!")
    print("👉 Next Steps:")
    print("1. Reload your IDE (Cursor/VSCode).")
    print("2. Run '/init-context' if available, or just say 'Plan a new feature'.")

def _copy_recursive(src, dst):
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
    parser = argparse.ArgumentParser(description="Install Prompt Base into a target project.")
    parser.add_argument("target", nargs="?", default=".", help="Target directory (default: current)")
    parser.add_argument("--hidden", action="store_true", help="Install into .agent/ directory (Hidden Mode)")
    args = parser.parse_args()
    
    
    # Auto-detect hidden mode preference if .agent exists in target
    target_hidden = os.path.exists(os.path.join(args.target, ".agent"))
    use_hidden = args.hidden or target_hidden
    
    install_prompt_base(args.target, hidden_mode=use_hidden)
