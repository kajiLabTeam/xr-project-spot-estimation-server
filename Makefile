-include .env

build:
	docker compose build

up:
	docker compose up

db:
	docker exec -it $(POSTGRES_CONTAINER_HOST) psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)
