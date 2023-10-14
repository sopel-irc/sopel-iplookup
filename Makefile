.PHONY: qa quality pylint pyroma

quality:
	isort sopel_iplookup
	flake8 sopel_iplookup
	mypy sopel_iplookup

pylint:
	pylint sopel_iplookup

pyroma:
	pyroma .

qa: quality pylint pyroma

.PHONY: develop build

develop:
	pip install -r requirements.txt
	python setup.py develop

build:
	rm -rf build/ dist/
	python -m build --sdist --wheel --outdir dist/ .
