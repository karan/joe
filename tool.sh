#!/bin/bash


function usage {
  local tool
  tool=$(basename "$0")

  cat <<EOF >/dev/stderr

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


# allow maximum of 1 argument for all subcommands except run
if [ $# -ne 1 ] && [ "$1" != "run" ]; then
   usage;
fi

if { [ -z "$1" ] && [ -t 0 ] ; } || [ "$1" == '-h' ] || [ "$1" == '--help' ]
then
  usage;
fi


# show help for no arguments if stdin is a terminal
if [ "$1" == "deps" ]; then
  go get github.com/urfave/cli
  go get github.com/termie/go-shutil
elif [ "$1" == "build" ]; then
  build
elif [ "$1" == "run" ]; then
  # default to linux-amd64
  joe_path=joe
  target="$(go env GOOS)-$(go env GOARCH)"

  # select executable targeted for current host environment
  case "${target}" in
    windows-386)
      joe_path=joe-x86.exe
      ;;
    windows-amd64)
      joe_path=joe.exe
      ;;
    linux-386)
      joe_path=joe-x86
      ;;
    linux-amd64)
      joe_path=joe
      ;;
    darwin-386)
      joe_path=joe-darwin-x86
      ;;
    darwin-amd64)
      joe_path=joe-darwin
      ;;
  esac

  build && ./build/${joe_path} "${@:2}"
else
  usage;
fi
