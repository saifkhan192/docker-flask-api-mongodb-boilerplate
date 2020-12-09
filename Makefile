.PHONY: _list
_list:
	@echo "Type make then a space then hit tab to see available commands"

build:
	cp -u .env.dist .env
	docker-compose --file docker/docker-compose.yml up -d --force-recreate --no-deps --build

up:
	docker-compose --file docker/docker-compose.yml up

recreate_all:
	docker-compose --file docker/docker-compose.yml up -d --force-recreate --no-deps --build mysqldb
	docker-compose --file docker/docker-compose.yml up -d --force-recreate --no-deps --build mongodb
	docker-compose --file docker/docker-compose.yml up -d --force-recreate --no-deps --build flask_app

run_all:
	docker container start mysqldb || true
	docker container start mongodb || true
	docker container start flask_app || true
	sleep 2
	google-chrome http://localhost

stop_all:
	docker container stop mysqldb || true
	docker container stop mongodb || true
	docker container stop flask_app || true

refresh_app:
	docker-compose --file docker/docker-compose.yml up --force-recreate --no-deps flask_app

bash_app:
	@docker exec -it flask_app /bin/bash

chrome_debug:
	/usr/bin/google-chrome http://localhost:3001 --remote-debugging-port=9222 --no-first-run --no-default-browser-check --user-data-dir=/home/saifullah/Desktop/vscode-chrome

run_app:
	docker-compose --file docker/docker-compose.yml up -d flask_app
	docker-compose --file docker/docker-compose.yml up -d mongodb
	docker-compose --file docker/docker-compose.yml up -d mysqldb
	sleep 1
	google-chrome http://localhost

follow_logs:
	docker logs --follow flask_app

build_react_container:
	# docker-compose --file docker/docker-compose.yml up --force-recreate --no-deps --build react_app
	docker-compose --file docker/docker-compose.yml build react_app

run_dev:
	docker rm -f watch_react_files | true
	docker run -t --rm --name watch_react_files \
	-v ${PWD}/react:/app \
	-v /app/node_modules \
	docker_react_app
	npm run watch

run_prod:
	docker rm -f watch_react_files | true
	docker run -t --rm --name watch_react_files \
	-v ${PWD}/react:/app \
	-v /app/node_modules \
	docker_react_app
	npm run production


git_push:
	git push origin master
	notify-send "Done"

print_docker_env:
	@docker-compose --file docker/docker-compose.yml run flask_app printenv

run_tests:
	docker exec -it flask_app pytest

run_tests_with_details:
	docker exec -it flask_app pytest -v
