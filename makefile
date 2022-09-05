venv:
	python -m venv nandini

activate:
	nandini/bin/activate
	

install:
	venv
	activate
	pip install -r requirements.txt

run:
	pip install -r requirements.txt