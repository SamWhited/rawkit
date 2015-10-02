REBUILD_FLAG =
VENV=env
BIN=$(VENV)/bin
ACTIVATE=source $(BIN)/activate
APIDOCS=docs/source/api
DOCSRC=$(APIDOCS)/modules.rst docs/source/* docs/source/_static/*

.PHONY: all
all: test build pre-commit

.PHONY: pre-commit
pre-commit: .git/hooks/pre-commit
.git/hooks/pre-commit: .pre-commit-config.yaml $(VENV)
	$(BIN)/pre-commit install

.PHONY: $(VENV)
$(VENV): requirements.txt $(BIN)/pip-sync $(VENV)/bin/activate
	$(BIN)/pip-sync

requirements.txt: requirements.in $(BIN)/pip-sync
	$(BIN)/pip-compile $<

$(BIN)/pip-sync: $(BIN)/activate
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install pip-tools

$(BIN)/activate:
	pyvenv $(VENV)
	touch $(BIN)/activate


.PHONY: test
test: $(VENV)
	$(BIN)/tox $(REBUILD_FLAG)

.PHONY: stress-test
stress-test: $(VENV)
	INPUT=$(INPUT) $(BIN)/tox -c tox-stress.ini $(REBUILD_FLAG)

dist/*.whl: setup.py rawkit/*.py
	python setup.py bdist_wheel

dist/*.tar.gz: setup.py rawkit/*.py
	python setup.py sdist bdist

.PHONY: wheel
wheel: dist/*.whl

.PHONY: dist
dist: dist/*.tar.gz

.PHONY: build
build: pre-commit wheel dist

.PHONY: upload
upload: clean
	python setup.py sdist bdist bdist_wheel upload

.PHONY: clean
clean:
	-$(ACTIVATE) 2>/dev/null; $(MAKE) -C docs $@
	find . -iname '*.pyc' | xargs rm -f
	find . -iname '__pycache__' -type d | xargs rm -rf
	rm -rf .tox
	rm -rf build
	rm -rf dist
	rm -rf $(VENV)
	rm -f requirements.txt

.PHONY: docs
docs: epub html $(VENV)

.PHONY: html
html: $(DOCSRC) $(VENV)
	$(ACTIVATE); $(MAKE) -C docs $@

.PHONY: epub
epub: $(DOCSRC) $(VENV)
	$(ACTIVATE); $(MAKE) -C docs $@

$(APIDOCS)/modules.rst: rawkit/*.py libraw/*.py $(VENV)
	$(BIN)/sphinx-apidoc -f -E -M -o $(APIDOCS) -H Contents . docs tests setup.py
