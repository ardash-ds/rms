# ============================================VARIABLES===========================================

compose_directory = docker/compose
# application_directory = apps
# core_directory = core
# fixtures_directory = fixtures
# code_directory = $(application_directory) $(core_directory) $(fixtures_directory)

docker_v2 = docker compose

main_container = -f $(compose_directory)/main.yml
app_container = -f $(compose_directory)/app.yml
db_container = -f $(compose_directory)/db.yml
migrations_container = -f $(compose_directory)/migrations.yml
population_container = -f $(compose_directory)/dbpopulation.yml
tests_container = -f $(compose_directory)/tests.yml

capture_exit_code = --abort-on-container-exit --exit-code-from
exit_code_population = db_population
exit_code_migrations = db_migrations
exit_code_tests = tests

compose_application := $(docker_v2) $(main_container) $(db_container) $(app_container) --env-file .env
compose_db := $(docker_v2) $(main_container) $(db_container) --env-file .env
compose_migrations := $(docker_v2) $(main_container) $(db_container) $(migrations_container) --env-file .env
compose_population := $(docker_v2) $(main_container) $(db_container) $(population_container) --env-file .env
compose_tests := $(docker_v2) $(main_container) $(db_container) $(tests_container) --env-file .env


# ============================================VARIABLES===========================================


# ===================================DOCKER(MANAGE APPLICATION)===================================

.PHONY: build
build:
	$(compose_application) build


.PHONY: app
app:
	$(compose_application) up

.PHONY: down
down:
	$(compose_application) down
	$(compose_population) down

.PHONY: stop
stop:
	$(compose_application) stop
	$(compose_population) stop

.PHONY: restart
restart:
	$(compose_application) stop
	$(compose_application) up

.PHONY: destroy
destroy:
	$(compose_application) down -v
	$(compose_migrations) down -v
	$(compose_population) down -v
	$(compose_tests) down -v

.PHONY: logs
logs:
	$(compose_application) logs -f

# ===================================DOCKER(MANAGE APPLICATION)===================================

# ========================================DOCKER(POPULATION)======================================

.PHONY: population
population:
	$(compose_population) up $(capture_exit_code) $(exit_code_population)

# ========================================DOCKER(POPULATION)======================================


# ========================================DOCKER(MIGRATIONS)======================================

.PHONY: migrations
migrations:
	$(compose_migrations) up $(capture_exit_code) $(exit_code_migrations)

# ========================================DOCKER(MIGRATIONS)======================================


# ==========================================DOCKER(TESTS)=========================================

.PHONY: build-tests
tests:
	$(compose_tests) build

.PHONY: tests
tests:
	$(compose_tests) up $(capture_exit_code) $(exit_code_tests)

# ==========================================DOCKER(TESTS)=========================================
