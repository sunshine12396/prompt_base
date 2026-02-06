# Prompt Base - Integration & Maintenance
# Supported: Antigravity, Cursor

.PHONY: init install audit test

# Get the current folder name (whatever the user named it)
CURRENT_DIR := $(notdir $(CURDIR))

# ============================================================
# INTEGRATION (One Command)
# ============================================================
# Usage:
#   git clone https://github.com/sunshine12396/prompt_base <any_folder_name>
#   cd <any_folder_name> && make init
#
# The temp folder is deleted automatically (whatever you named it).
# ============================================================

init:
	@echo "================================================================"
	@echo "🎭 Prompt Base Installer"
	@echo "   Supported: Antigravity + Cursor"
	@echo "================================================================"
	@python3 scripts/install.py .. --hidden
	@rm -rf ../.agent/.git 2>/dev/null || true
	@rm -rf ../.agent/scripts/__pycache__ 2>/dev/null || true
	@echo ""
	@echo "✅ Installation complete!"
	@echo "🧹 Cleaning up temp folder ($(CURRENT_DIR))..."
	@cd .. && rm -rf "$(CURRENT_DIR)"

# Alias
install: init

# Audit project
audit:
	@python3 scripts/checklist.py .

# Test
test:
	@python3 scripts/test_integration.py
