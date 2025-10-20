
.PHONY: clean sdist test docs


sdist:
	python3 ./setup.py sdist


test:
	@python3 -m unittest discover tests


docs:
	cd ./docs && python -m nbconvert --to html *.ipynb
	cd ./docs && python -m nbconvert --to markdown *.ipynb

clean:
	@find . -type d -name __pycache__ -exec rm -r {} +
