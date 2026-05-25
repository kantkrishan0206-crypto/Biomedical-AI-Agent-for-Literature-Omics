.PHONY: setup dev build test lint migrate seed docker-up docker-down benchmark

setup:
	./scripts/setup.sh

dev:
	./scripts/dev-start.sh

build:
	./scripts/build-all.sh

test:
	pytest && pnpm test

lint:
	ruff check . && pnpm lint

migrate:
	./scripts/migrate-db.sh

seed:
	./scripts/seed-data.sh

docker-up:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml up --build

docker-down:
	docker compose down --remove-orphans

benchmark:
	./scripts/benchmark.sh
