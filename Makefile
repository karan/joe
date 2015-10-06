.PHONY: usage readme test prod
define USAGE
  USAGE:
    $$ make COMMAND

  EXAMPLES:
    $$ make			  Shows this help text
    $$ make readme    Generate README.rst from README.md
    $$ make test      Upload release to testpypi
    $$ make prod      Upload release to prod pypi
endef

usage:
	$(info $(USAGE))
	@:

readme:
	@rm -f README.rst
	@pandoc --from=markdown --to=rst --output=README.rst README.md
	$(info README created as README.rst)
	@:

test: readme
	@python setup.py sdist upload -r pypitest
	$(info Distribution uploaded to pypitest)
	@:

prod: readme
	python setup.py sdist upload -r pypi
	$(info Distribution uploaded to pypi)
	@:
