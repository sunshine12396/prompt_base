# Prompt Base - Subfolder Integration
# Supported: Antigravity, Cursor

# Audit project
audit:
	@python3 scripts/checklist.py .

# Test
test:
	@python3 scripts/test_integration.py

# Install Cursor Rules
cursor:
	@cp .cursorrules ../.cursorrules
	@echo "Cursor rules installed to project root."
