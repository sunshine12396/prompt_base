import os
import json
import yaml

def get_frontmatter(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        if content.startswith('---'):
            try:
                parts = content.split('---')
                return yaml.safe_load(parts[1])
            except:
                return {}
    return {}

def build_registry(root_dir="agent"):
    registry = {
        "agents": [],
        "skills": {
            "core": [],
            "tech": [],
            "process": [],
            "custom": []
        }
    }

    # Agents
    agent_dir = os.path.join(root_dir, "agents")
    if os.path.exists(agent_dir):
        for f in os.listdir(agent_dir):
            if f.endswith('.md'):
                meta = get_frontmatter(os.path.join(agent_dir, f))
                registry["agents"].append({
                    "id": f.replace('.md', ''),
                    "name": meta.get('name', f),
                    "description": meta.get('description', ''),
                    "path": os.path.join(agent_dir, f)  # Path relative to project root
                })

    # Skills
    skill_categories = ["core", "tech", "process", "custom"]
    for cat in skill_categories:
        cat_path = os.path.join(root_dir, "skills", cat)
        if os.path.exists(cat_path):
            for d in os.listdir(cat_path):
                skill_dir = os.path.join(cat_path, d)
                skill_md = os.path.join(skill_dir, "SKILL.md")
                if os.path.isdir(skill_dir) and os.path.exists(skill_md):
                    meta = get_frontmatter(skill_md)
                    registry["skills"][cat].append({
                        "id": d,
                        "name": meta.get('name', d),
                        "description": meta.get('description', ''),
                        "path": skill_dir
                    })

    # Write registry to the root_dir
    registry_file = os.path.join(root_dir, "registry.json")
    with open(registry_file, "w") as f:
        json.dump(registry, f, indent=2)
    print(f"✅ Generated registry at: {registry_file}")

if __name__ == "__main__":
    import sys
    # Default to "agent" but allow override
    target_root = ".agent"
    
    # Simple check for .agent existence preference
    if os.path.exists(".agent") and not os.path.exists("agent"):
        target_root = ".agent"
        
    if len(sys.argv) > 1:
        target_root = sys.argv[1]
        
    build_registry(target_root)
