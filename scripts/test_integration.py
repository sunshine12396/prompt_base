import os
import shutil
import subprocess
import sys

def test_integration():
    print("🧪 Testing Prompt Base Integration Workflow...")
    
    # 1. Setup a mock project
    test_dir = "/tmp/pb_integration_test"
    mock_project = os.path.join(test_dir, "my_project")
    cloned_pb = os.path.join(mock_project, "prompt_base_tmp")
    
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    
    os.makedirs(mock_project)
    print(f"✅ Created mock project: {mock_project}")
    
    # 2. Simulate "git clone" by copying current project to tmp
    current_pb = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    shutil.copytree(current_pb, cloned_pb, ignore=shutil.ignore_patterns('.git', '__pycache__'))
    print(f"✅ Simulated 'git clone' into: {cloned_pb}")
    
    # 3. Run 'make init' from within the cloned folder
    try:
        print("🚀 Running 'make init'...")
        subprocess.run(["make", "init"], cwd=cloned_pb, check=True)
    except Exception as e:
        print(f"❌ Integration failed: {e}")
        sys.exit(1)
        
    # 4. Verify installation in parent (mock_project)
    checks = [
        os.path.join(mock_project, ".agent", "GEMINI.md"),
        os.path.join(mock_project, ".agent", "registry.json"),
        os.path.join(mock_project, ".cursorrules"),
        os.path.join(mock_project, ".vscode", "settings.json")
    ]
    
    for path in checks:
        if os.path.exists(path):
            print(f"✅ Verified: {path}")
        else:
            print(f"❌ Missing: {path}")
            sys.exit(1)
            
    # 5. Verify path correction
    with open(os.path.join(mock_project, ".agent", "GEMINI.md"), "r") as f:
        content = f.read()
        if ".agent/registry.json" in content:
            print("✅ Verified Path Correction (Hidden Mode active in docs)")
        else:
            print("❌ Path Correction Failed in GEMINI.md")
            sys.exit(1)

    print("\n🎉 INTEGRATION TEST PASSED!")
    print("The 'clone -> cd -> make init' workflow is robust.")

if __name__ == "__main__":
    test_integration()
