.PHONY: qa quality pylint pyroma

quality:
	isort -c sopel_iplookup
	flake8 sopel_iplookup
	mypy sopel_iplookup

pylint:
	pylint sopel_iplookup

pyroma:
	pyroma .

qa: quality pylint pyroma

.PHONY: develop build

develop:
	python -m pip install -U pip
	python -m pip install -U requirements.txt
	python -m pip install -e .

build:
	rm -rf build/ dist/
	python -m build --sdist --wheel --outdir dist/ .
