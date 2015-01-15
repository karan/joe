#!/bin/bash


function usage {
  local tool=$(basename $0)
  cat <<EOF

  USAGE:
    $ $tool [-h|--help] COMMAND

  EXAMPLES:
    $ $tool readme
    $ $tool pypitest
    $ $tool pypiprod
EOF
  exit 1;
}


# convert README.md to README.rst
function readme {
  pandoc --from=markdown --to=rst --output=README.rst README.md
  printf 'README.rst generated';
}


# total arguments should be 1
if [ $# -ne 1 ]; then
   usage;
fi

if { [ -z "$1" ] && [ -t 0 ] ; } || [ "$1" == '-h' ] || [ "$1" == '--help' ]
then
  usage;
fi


# show help for no arguments if stdin is a terminal
if [ "$1" == "readme" ]; then
  readme
elif [ "$1" == "test" ]; then
  readme
  # build and upload package to test pypi
  python setup.py sdist upload -r pypitest
elif [ "$1" == "prod" ]; then
  readme
  # build and upload package to prod pypi
  python setup.py sdist upload -r pypi
else
  usage;
fi
