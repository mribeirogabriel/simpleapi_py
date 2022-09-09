prepare-env:
	python3 -m pip install --user virtualenv
	python3 -m venv env

start-env:
	. env/bin/activate

install:
	pip install -r requirements.txt

run:
	python3 src/main.py

test:
	python3 -m pytest -s