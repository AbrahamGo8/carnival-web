SHELL := /bin/bash

.PHONY: help
help:
	@echo "Usage:"
	@echo " make lint   run code checker."
	@echo " make test   run test suite."

.PHONY: lint
.ONESHELL:
lint:
	flake8

.PHONY: test
.ONESHELL:
test:
	python manage.py test