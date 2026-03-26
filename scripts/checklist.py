import json
import os
import sys
import re

def check_structure():
    print("📋 Prompt Base - Final Audit\n")
    issues = []
    
    # 0. Root Detection
    root_dir = "agent"
    
    # Try common locations relative to project root
    if os.path.exists(os.path.expanduser("~/.gemini")):
        root_dir = os.path.expanduser("~/.gemini")
    elif os.path.exists(".agents"):
        root_dir = ".agents"
    elif os.path.exists("GEMINI.md"):
        root_dir = "."
        
    # Allow override via arg (for testing)
    if "--root" in sys.argv:
        idx = sys.argv.index("--root")
        if idx + 1 < len(sys.argv):
            root_dir = sys.argv[idx + 1]

    print(f"🔍 Checking structure using root: {root_dir}")

    # 1. Critical Files
    critical_files = [
        f"{root_dir}/ARCHITECTURE.md",
        f"{root_dir}/GEMINI.md",
        f"{root_dir}/registry.min.json",
        f"{root_dir}/core/system_prompt.md",
        f"{root_dir}/core/memory_rules.md",
        f"{root_dir}/core/classifier.md",
        f"{root_dir}/core/rules.md",
        ]
    
    for f in critical_files:
        if os.path.exists(f):
            print(f"✅ {f} found.")
        else:
            issues.append(f"❌ Missing critical file: {f}")

    # 2. Directory Structure
    dirs = [
        f"{root_dir}/core",
        f"{root_dir}/agents",
        f"{root_dir}/skills/core",
        f"{root_dir}/skills/tech",
        f"{root_dir}/skills/process",
        f"{root_dir}/skills/custom",
        f"{root_dir}/workflows"
    ]
    
    for d in dirs:
        if os.path.isdir(d):
            print(f"✅ Directory {d} exists.")
        else:
            issues.append(f"❌ Missing directory: {d}")

    # 3. Registry Consistency
    registry_path = f"{root_dir}/registry.min.json"
    if os.path.exists(registry_path):
        with open(registry_path, "r") as f:
            registry = json.load(f)
            
            # Check Agents
            for agent in registry.get("agents", []):
                # Paths in registry might be relative to root or full paths. 
                # We assume they are relative strings like "agent/agents/..."
                # If we are in ".agents" mode, the registry should probably say "agents/..."
                # BUT, if we just blindly check existence, it should work.
                
                full_path = os.path.join(root_dir, agent["path"])
                if not os.path.exists(full_path):
                    issues.append(f"❌ Registry points to non-existent agent: {full_path}")
            
            # Check Skills
            for cat, skills in registry.get("skills", {}).items():
                for skill in skills:
                    full_path = os.path.join(root_dir, skill["path"])
                    if not os.path.exists(full_path):
                        issues.append(f"❌ Registry points to non-existent skill ({cat}): {full_path}")
        print("✅ Registry consistency check complete.")

    # 4. Deep Skill Verification & Orphans
    print("🔍 Performing deep skill verification...")
    skill_root = f"{root_dir}/skills"
    registered_paths = set()
    
    # Collect all registered paths
    if os.path.exists(registry_path):
        with open(registry_path, "r") as f:
            registry = json.load(f)
            for cat, skills in registry.get("skills", {}).items():
                for skill in skills:
                    skill_path = os.path.join(root_dir, skill["path"])
                    registered_paths.add(os.path.abspath(skill_path))
                    
                    if not skill.get("description"):
                        issues.append(f"⚠️ Skill missing description ({cat}): {skill['id']}")
                    
                    # Check for SKILL.md
                    if os.path.isdir(skill_path):
                        if not os.path.exists(os.path.join(skill_path, "SKILL.md")):
                            issues.append(f"❌ Skill directory missing SKILL.md ({cat}): {skill_path}")
    
    # Check for Orphans
    skill_categories = ["core", "tech", "process", "custom"]
    for cat in skill_categories:
        cat_dir = os.path.join(skill_root, cat)
        if os.path.exists(cat_dir):
            for d in os.listdir(cat_dir):
                d_path = os.path.join(cat_dir, d)
                if os.path.isdir(d_path):
                    if os.path.exists(os.path.join(d_path, "SKILL.md")):
                        if os.path.abspath(d_path) not in registered_paths:
                             issues.append(f"⚠️ Orphaned skill found: {d_path}")

    # 6. Orphaned Agents Check
    agents_dir = f"{root_dir}/agents"
    if os.path.exists(agents_dir):
        agent_ids = set()
        if os.path.exists(registry_path):
            with open(registry_path, "r") as f:
                reg = json.load(f)
                for a in reg.get("agents", []):
                    agent_path = os.path.join(root_dir, a["path"])
                    agent_ids.add(os.path.abspath(agent_path))
                    if not a.get("description"):
                         issues.append(f"⚠️ Agent missing description: {a['name']}")

        for f in os.listdir(agents_dir):
            if f.endswith(".md"):
                f_path = os.path.abspath(os.path.join(agents_dir, f))
                if f_path not in agent_ids:
                    issues.append(f"⚠️ Orphaned agent found: {os.path.join(agents_dir, f)}")

    # 7. Branding Check
    forbidden_terms = ["agent"] #  is now allowed
    # Note:  is now allowed as a directory, but maybe we shouldn't find it in content as "branding"?
    # For now, let's keep the check but maybe relax it or ignore if it's the root.
    
    files_to_check = critical_files
    for f_path in files_to_check:
        if os.path.exists(f_path):
            with open(f_path, "r") as f:
                content = f.read()
                for term in forbidden_terms:
                    if term == "agent":
                        # Use regex to find 'agent/' that is NOT preceded by a dot
                        if re.search(r'(?<!\.)agent/', content):
                            issues.append(f"⚠️ Visible 'agent/' reference found in {f_path} (use '' or relative paths)")
                        continue
                    if term in content:
                        issues.append(f"⚠️ Forbidden term '{term}' found in {f_path}")

    # Summary
    print("\n--- Audit Result ---")
    if not issues:
        print("🚀 ALL SYSTEMS NOMINAL. Prompt Base is ready.")
        sys.exit(0)
    else:
        print(f"Found {len(issues)} issues:")
        for issue in issues:
            print(issue)
        sys.exit(1)

if __name__ == "__main__":
    check_structure()
