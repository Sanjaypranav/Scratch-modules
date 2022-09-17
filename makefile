venv:
	python -m venv nandini

activate:
	nandini/bin/activate

install:
	pip install virtualenv
	venv
	activate
	python setup.py install

run:
	python setup.py install

uninstall:
	pip uninstall nandini