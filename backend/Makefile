.DEFAULT_GOAL := help

BACKEND_CONTAINER_NAME=backend_backend_1
CURRENT_BRANCH=`git rev-parse --abbrev-ref HEAD`

.PHONY: backend-shell
backend-shell:  ## Run docker shell for backend service
	docker exec -it $(BACKEND_CONTAINER_NAME) /bin/bash

.PHONY: check
check:  ## Check code formatting and import sorting
	./scripts/check.sh

.PHONY: coverage
coverage:  ## Run coverage
	./scripts/coverage.sh

.PHONY: fix
fix:  ## Fix code formatting, linting and sorting imports
	python3 -m black .
	python3 -m isort .
	python3 -m flake8
	python3 -m mypy .

.PHONY: local
local: pip_update  ## Install local requirements and dependencies
	python3 -m piptools sync requirements/local.txt

.PHONY: outdated
outdated:  ## Check outdated requirements and dependencies
	python3 -m pip list --outdated

.PHONY: pip
pip: pip_update  ## Compile requirements
	python3 -m piptools compile --generate-hashes --no-header --quiet --upgrade --output-file requirements/base.txt requirements/base.in
	python3 -m piptools compile --generate-hashes --no-header --quiet --upgrade --output-file requirements/common.txt requirements/common.in
	python3 -m piptools compile --generate-hashes --no-header --quiet --upgrade --output-file requirements/local.txt requirements/local.in
	python3 -m piptools compile --generate-hashes --no-header --quiet --upgrade --output-file requirements/remote.txt requirements/remote.in
	python3 -m piptools compile --generate-hashes --no-header --quiet --upgrade --output-file requirements/test.txt requirements/test.in\

.PHONY: pip_update
pip_update:  ## Update requirements and dependencies
	python3 -m pip install --quiet --upgrade pip~=22.3.0 pip-tools~=6.9.0 setuptools~=65.5.0 wheel~=0.37.0

.PHONY: precommit
precommit:  ## Fix code formatting, linting and sorting imports
	python3 -m pre_commit run --all-files

.PHONY: remote
remote: pip_update  ## Install remote requirements and dependencies
	python3 -m piptools sync requirements/remote.txt

.PHONY: report
report:  ## Run coverage report
	./scripts/report.sh

.PHONY: run
run:  ## Run server with gunicorn
	gunicorn app.main:app

.PHONY: run_local
run_local:  ## Run server with uvicorn for local development
	uvicorn app.main:app --reload --host 0 --port 8000

ifeq (simpletest,$(firstword $(MAKECMDGOALS)))
  simpletestargs := $(wordlist 2, $(words $(MAKECMDGOALS)), $(MAKECMDGOALS))
  $(eval $(simpletestargs):;@true)
endif

.PHONY: simpletest
simpletest:  ## Run debugging test
	pytest -vv $(simpletestargs)

.PHONY: test
test:  ## Run test
	./scripts/test.sh

.PHONY: help
help:
	@echo "[Help] Makefile list commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'