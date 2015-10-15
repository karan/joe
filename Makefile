
# function usage {
#   local tool=$(basename $0)
#   cat <<EOF

#   USAGE:
#     $ $tool [-h|--help] COMMAND

#   EXAMPLES:
#     $ $tool readme    Generate README.rst from README.md
#     $ $tool test      Upload release to testpypi
#     $ $tool prod      Upload release to prod pypi
# EOF
#   exit 1;
# }


# # convert README.md to README.rst
# function readme {
#   pandoc --from=markdown --to=rst --output=README.rst README.md
#   printf 'README.rst generated';
# }


# # total arguments should be 1
# if [ $# -ne 1 ]; then
#    usage;
# fi

# if { [ -z "$1" ] && [ -t 0 ] ; } || [ "$1" == '-h' ] || [ "$1" == '--help' ]
# then
#   usage;
# fi


# # show help for no arguments if stdin is a terminal
# if [ "$1" == "readme" ]; then
#   readme
# elif [ "$1" == "test" ]; then
#   readme
#   # build and upload package to test pypi
#   python setup.py sdist upload -r pypitest
# elif [ "$1" == "prod" ]; then
#   readme
#   # build and upload package to prod pypi
#   python setup.py sdist upload -r pypi
# else
#   usage;
# fi

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
