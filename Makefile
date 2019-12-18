.PHONY: init
init:
	python3 -m pip install tox black pip-tools wheel twine bumpversion
	pip-compile
	pip install -rrequirements.txt

.PHONY: format
format:
	python3 -m black .

.PHONY: test
test:
	python3 -m tox -p auto