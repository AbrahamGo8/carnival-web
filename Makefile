SHELL := /bin/bash

.PHONY: help
help:
	@echo "Usage:"
	@echo " make lint   run code checker."
	@echo " make test   run test suite."
	@echo " make run    run application."

.PHONY: lint
.ONESHELL:
lint:
    cd carnival_web
	flake8

.PHONY: test
.ONESHELL:
test:
    cd carnival_web
	python manage.py test --settings=carnival_web.settings.test

.PHONY: run
.ONESHELL:
run:
    cd carnival_web
	python manage.py runserver --settings=carnival_web.settings.local