req :
	pip-compile requirements/local.in
	pip-compile requirements/production.in
	pip-compile requirements/test.in
