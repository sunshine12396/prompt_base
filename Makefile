# Prompt Base Lifecycle & Integration

.PHONY: init audit test cleanup

# Integration: Install to parent directory and cleanup temporary files
init:
	@echo "🚀 Initializing Prompt Base integration..."
	@python3 scripts/install.py .. --hidden
	@echo "✅ Integrated into parent directory."
	@echo "🧹 Removing unnecessary files from integrated framework..."
	@# Remove the .git folder from the target's .agent folder if it was mistakenly copied (it shouldn't be)
	@rm -rf ../.agent/.git
	@echo "✨ Setup complete. You can now delete this temporary folder."

# Internal maintenance
audit:
	@python3 scripts/checklist.py .

# Run integration tests
test:
	@python3 scripts/test_integration.py
