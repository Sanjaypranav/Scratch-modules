SYSTEM_PYTHON  = $(or $(shell which python3), $(shell which python))
PYTHON         = $(or $(wildcard nandini/bin/python3), $(SYSTEM_PYTHON))
venv:
	python -m venv nandini

activate:
	. nandini/bin/activate

install:
	$(PYTHON) setup.py install

run:
	python setup.py install

uninstall:
	pip uninstall nandini