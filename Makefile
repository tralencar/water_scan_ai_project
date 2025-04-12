.PHONY : lock, quality, run, doc, tests, test, build, end, clear_all

# --------------------------
# Automation Tasks with Makefile
# --------------------------

# --------------------------
# Generate the Poetry Lockfile
# --------------------------
lock:
	@echo "Starting the lock process ..."
	@python3 -m pip install -q poetry==1.8.3
	@poetry lock

# --------------------------
# Code Quality Check
# --------------------------
quality:
	@echo "Starting the quality process ..."
	@poetry install --with dev
	@poetry run pre-commit install
	@poetry run pre-commit run --all-files

# --------------------------
# Running the Web Scraper
# --------------------------
run:
	@echo "Starting the crawler service ..."
	@poetry install
	@poetry run python src/water_scan_main.py

# --------------------------
# Access online documentation via mkDocs
# --------------------------
doc:
	@echo "Loading documentation ..."
	@poetry run mkdocs serve

# --------------------------
# Tests with pytest
# --------------------------
test:
	@echo "Executando testes unitarios ..."
	@poetry install --with dev
	@poetry run pytest --cov=src --cov-fail-under=27

# --------------------------
# Automações para o docker
# --------------------------

DOCKER_COMPOSE = docker-compose -f mlflow-minio-setup/docker-compose.yml
# DOCKER_COMPOSE = docker-compose -f docker-compose.yml


build:
	@echo "Build the services..."
	@$(DOCKER_COMPOSE) up --build -d

end:
	@echo "Finish the services..."
	@$(DOCKER_COMPOSE) kill

clear_all:
	@echo "Removing all Docker containers..."
	@docker rm -f $$(docker ps -a -q) || true
