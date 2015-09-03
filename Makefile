.PHONY: req env

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  req	Compile pip requirements."
	@echo "  env	Load env."


req:
	pip-compile requirements/local.in
	pip-compile requirements/production.in
	pip-compile requirements/test.in
