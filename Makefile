usage:
	@echo "USAGE:"
	@echo "\t $ make COMMAND\n"
	@echo "EXAMPLES:"
	@echo "\t$ make readme    Generate README.rst from README.md"
	@echo "\t$ make test      Upload release to testpypi"
	@echo "\t$ make prod      Upload release to prod pypi"
	@echo "\t$ make help      Show this usage"

create-readme:
	$(shell pandoc --from=markdown --to=rst --output=README.rst README.md)
	@echo 'README.rst generated'

test: create-readme
	python setup.py sdist upload -r pypitest

prod: create-readme
	python setup.py sdist upload -r pipy

readme: create-readme

.DEFAULT help: usage
