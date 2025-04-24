ifeq ($(OS),Windows_NT)
CUR_DIR=$(shell echo %CD%)
else
CUR_DIR=$(shell pwd)
endif

APP_IMAGE=recommendations_local
APP_TAG=latest
DB_IMAGE=recommendations-db
DB_TAG=latest
RELEASE_NAME=recommendations
DC_FILE=-f ${CUR_DIR}/docker-compose.yaml

.PHONY: compile compile-db deploy delete

compile:
	docker build --no-cache -f Dockerfile -t ${APP_IMAGE}:${APP_TAG} .

compile-db:
	docker build --no-cache -f PGDockerfile -t ${DB_IMAGE}:${DB_TAG} .

deploy:
	docker compose ${DC_FILE} -p ${RELEASE_NAME} up -d

delete:
	docker compose ${DC_FILE} -p ${RELEASE_NAME} rm -sf
