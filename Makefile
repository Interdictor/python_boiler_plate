awake:
	docker-compose up --build

up:
	docker-compose up

down:
	docker-compose down

build:
	docker-compose build

test:
	docker-compose exec boiler pipenv run mamba --format=documentation

lock:
	docker-compose run --rm boiler pipenv lock
