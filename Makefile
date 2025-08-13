.RECIPEPREFIX := >
.PHONY: up down test harvest build

up:
> docker compose up -d

down:
> docker compose down

harvest:
> python python_service/app/harvest.py $(DIR)

test:
> cargo test --manifest-path rust_service/Cargo.toml
> pytest python_service/tests

build:
> docker compose build
