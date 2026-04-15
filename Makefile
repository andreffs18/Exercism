.PHONY: lint test help

# Default target - show help
help:
	@echo "Available targets:"
	@echo "  make lint        - Format and fix Python code using ruff"
	@echo "  make test        - Run Python tests (use TEST=folder to specify location)"
	@echo "  make help        - Show this help message"
	@echo ""
	@echo "Examples:"
	@echo "  make test                     # Run all tests"
	@echo "  make test TEST=python/bob     # Run tests in python/bob"

# Lint target - format and check Python code with ruff
lint:
	@echo "Formatting Python code with ruff..."
	uv run ruff format .
	@echo "Checking Python code with ruff..."
	uv run ruff check . --fix
	@echo "✅ Linting complete!"

# Test target - run Python tests with pytest
# Usage: make test [TEST=path/to/tests]
test:
ifdef TEST
	@echo "Running tests in $(TEST)..."
	uv run pytest -vv $(TEST)
else
	@echo "Running all tests..."
	uv run pytest -vv
endif
