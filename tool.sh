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
  GOOS=windows GOARCH=386 go build -o build/joe-x86.exe joe.go utils.go
  GOOS=windows GOARCH=amd64 go build -o build/joe.exe joe.go utils.go
  GOOS=linux GOARCH=386 go build -o build/joe-x86 joe.go utils.go
  GOOS=linux GOARCH=amd64 go build -o build/joe joe.go utils.go
  GOOS=darwin GOARCH=386 go build -o build/joe-darwin-x86 joe.go utils.go
  GOOS=darwin GOARCH=amd64 go build -o build/joe-darwin joe.go utils.go
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
  go get github.com/termie/go-shutil
elif [ "$1" == "build" ]; then
  build
elif [ "$1" == "run" ]; then
  build && ./joe
else
  usage;
fi
