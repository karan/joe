#!/bin/bash


function usage {
  local tool=$(basename $0)
  cat <<EOF

  USAGE:
    $ $tool [-h|--help] COMMAND

  EXAMPLES:
    $ $tool deps      Install dependencies for joe
    $ $tool build     Build a binary
    $ $tool run       Build and run the binary
EOF
  exit 1;
}


function build {
  go build -o build/joe joe.go utils.go
  printf 'joe built\n';
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
if [ "$1" == "deps" ]; then
  go get github.com/codegangsta/cli
elif [ "$1" == "build" ]; then
  build
elif [ "$1" == "run" ]; then
  build && ./joe
else
  usage;
fi
