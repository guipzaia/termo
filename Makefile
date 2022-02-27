clean:
	rm -R -f *.pyc .coverage .pytest_cache htmlcov __pycache__

install:
	pip3 install -r requirements.txt

test:
	python3 -m pytest test_app.py

coverage: clean
	python3 -m pytest --cov=.

lint:
	python3 -m pylint app.py test_app.py constants.py

cov-report: clean
	python3 -m pytest --cov=. --cov-report=html && google-chrome htmlcov/index.html

all: clean install lint test coverage

run:
	python3 app.py