.PHONY: validate manifest score all

PYTHON ?= python3

validate:
	$(PYTHON) scripts/validate_structure.py

manifest:
	$(PYTHON) scripts/build_manifest.py

score:
	$(PYTHON) scripts/quality_score.py

all: manifest validate score
