PYTHON_VENV = .venv

PIP_PATH = $(PYTHON_VENV)/bin/pip3
PYTHON_PATH = $(PYTHON_VENV)/bin/python3


venv:
	python3 -m venv $(PYTHON_VENV)
	$(PIP_PATH) install -r .requirements


run:
	$(PYTHON_PATH) main.py


debug:
	$(PYTHON_PATH) -m debugpy --listen localhost:8888 --wait-for-client main.py


clean:
	rm -rf $(PYTHON_VENV)
	rm -rf __pycache__
