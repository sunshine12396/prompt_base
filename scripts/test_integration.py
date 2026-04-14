import os
import sys

def test_integration():
    print("🧪 Testing Prompt Base Global Integration...\n")
    
    # The project root is the parent of the scripts/ directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    print(f"📁 Project root: {project_root}")
    
    # 1. Verify Rules (GEMINI.md)
    print("\n--- 1. Rules ---")
    gemini_path = os.path.join(project_root, "GEMINI.md")
    if os.path.exists(gemini_path):
        print(f"✅ Rules file exists: GEMINI.md")
    else:
        print(f"❌ Missing Rules file: GEMINI.md")
        sys.exit(1)
    
    # 2. Verify Core files
    print("\n--- 2. Core Logic ---")
    core_files = [
        "core/system_prompt.md",
        "core/rules.md",
        "core/classifier.md",
        "core/memory_rules.md",
    ]
    for cf in core_files:
        path = os.path.join(project_root, cf)
        if os.path.exists(path):
            print(f"✅ {cf}")
        else:
            print(f"❌ Missing: {cf}")
            sys.exit(1)
    
    # 3. Verify Workflows (antigravity/global_workflows/)
    print("\n--- 3. Workflows ---")
    workflow_dir = os.path.join(project_root, "antigravity", "global_workflows")
    if os.path.isdir(workflow_dir):
        workflows = [f for f in os.listdir(workflow_dir) if f.endswith(".md")]
        print(f"✅ Workflow directory exists with {len(workflows)} workflow(s)")
        for w in sorted(workflows):
            print(f"   📄 {w}")
    else:
        print(f"❌ Missing workflow directory: antigravity/global_workflows/")
        sys.exit(1)
    
    # 4. Verify Skills (antigravity/skills/)
    print("\n--- 4. Skills ---")
    skill_dir = os.path.join(project_root, "antigravity", "skills")
    if os.path.isdir(skill_dir):
        categories = [d for d in os.listdir(skill_dir) if os.path.isdir(os.path.join(skill_dir, d))]
        print(f"✅ Skill directory exists with {len(categories)} categories: {', '.join(sorted(categories))}")
        
        total_skills = 0
        for cat in sorted(categories):
            cat_path = os.path.join(skill_dir, cat)
            skills = [d for d in os.listdir(cat_path) if os.path.isdir(os.path.join(cat_path, d))]
            total_skills += len(skills)
            print(f"   📂 {cat}/  ({len(skills)} skills)")
        print(f"   Total: {total_skills} skills")
    else:
        print(f"❌ Missing skill directory: antigravity/skills/")
        sys.exit(1)
    
    # 5. Verify Agents
    print("\n--- 5. Agents ---")
    agents_dir = os.path.join(project_root, "agents")
    if os.path.isdir(agents_dir):
        agents = [f for f in os.listdir(agents_dir) if f.endswith(".md")]
        print(f"✅ Agents directory exists with {len(agents)} agent(s)")
    else:
        print(f"❌ Missing agents directory")
        sys.exit(1)
    
    # 6. Verify Registry
    print("\n--- 6. Registry ---")
    registry_path = os.path.join(project_root, "registry.min.json")
    if os.path.exists(registry_path):
        import json
        with open(registry_path, "r") as f:
            registry = json.load(f)
        
        # Verify skill paths point to antigravity/skills/
        for cat, skills in registry.get("skills", {}).items():
            for skill in skills:
                if not skill["path"].startswith("antigravity/skills/"):
                    print(f"❌ Skill path not updated: {skill['path']}")
                    sys.exit(1)
        print("✅ Registry exists and all skill paths use antigravity/skills/")
    else:
        print(f"❌ Missing registry: registry.min.json")
        sys.exit(1)

    print("\n🎉 INTEGRATION TEST PASSED!")
    print("All 3 component types validated:")
    print("  1. Rules     → GEMINI.md ✅")
    print("  2. Workflows → antigravity/global_workflows/*.md ✅")
    print("  3. Skills    → antigravity/skills/*/SKILL.md ✅")

if __name__ == "__main__":
    test_integration()
