VENV = .venv/bin/activate

$(VENV):
	python3 -m venv .venv
	. $(VENV) && pip install -r requirements.txt

.PHONY: clean
clean:
	rm -rf $(VENV)
	rm -rf site

serve: $(VENV)
	. $(VENV) && python3 -m mkdocs serve

deploy: $(VENV)
	. $(VENV) && python3 -m mkdocs gh-deploy --force

