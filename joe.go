package main

import (
	"fmt"
	"github.com/codegangsta/cli"
	"io/ioutil"
	"log"
	"os"
	"path"
	"strings"
)

const joe string = `
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀█░█▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
      ▐░▌    ▐░▌       ▐░▌▐░▌          
      ▐░▌    ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
      ▐░▌    ▐░▌       ▐░▌▐░░░░░░░░░░░▌
      ▐░▌    ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ 
      ▐░▌    ▐░▌       ▐░▌▐░▌          
 ▄▄▄▄▄█░▌    ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀      ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
`
const version string = "1.0.0"
const gitignoreUrl = "https://github.com/github/gitignore/archive/master.zip"
const dataDir string = ".joe-data"

var dataPath = path.Join(os.Getenv("HOME"), dataDir)

func availableFiles() (a []string, err error) {
	files, err := ioutil.ReadDir(dataPath)
	if err != nil {
		return nil, err
	}

	availableGitignores := []string{}
	for _, f := range files {
		if strings.HasSuffix(f.Name(), ".gitignore") {
			availableGitignores = append(availableGitignores, strings.Replace(f.Name(), ".gitignore", "", 1))
		}
	}
	return availableGitignores, nil
}

func generate(args string) {
	names := strings.Split(args, ",")

	availableGitignores, err := availableFiles()
	if err != nil {
		log.Fatal(err)
	}

	notFound := []string{}
	output := "#### joe made this: http://goel.io/joe\n"
	for _, name := range names {
		if stringInSlice(name, availableGitignores) {
			bytes, err2 := ioutil.ReadFile(path.Join(dataPath, name+".gitignore"))
			if err != nil {
				log.Fatal(err2)
			}
			output += string(bytes)
		} else {
			notFound = append(notFound, name)
		}
	}
	if len(notFound) > 0 {
		fmt.Printf("Unsupported files: %s\n", strings.Join(notFound, ", "))
		fmt.Println("Run `joe ls` to see list of available gitignores.")
		output = ""
	}
	fmt.Println(output)
}

func main() {
	app := cli.NewApp()
	app.Name = joe
	app.Usage = "generate .gitignore files from the command line"
	app.UsageText = "joe command [arguments...]"
	app.Version = version
	app.Commands = []cli.Command{
		{
			Name:    "ls",
			Aliases: []string{"list"},
			Usage:   "list all available files",
			Action: func(c *cli.Context) {
				availableGitignores, err := availableFiles()
				if err != nil {
					log.Fatal(err)
				}
				fmt.Printf("%d supported .gitignore files:\n", len(availableGitignores))
				fmt.Printf("%s", strings.Join(availableGitignores, ", "))
			},
		},
		{
			Name:    "u",
			Aliases: []string{"update"},
			Usage:   "update all available gitignore files",
			Action: func(c *cli.Context) {
				fmt.Println("Updating gitignore files..")
				err := RemoveContents(dataPath)
				if err != nil {
					log.Fatal(err)
				}
				err = DownloadFiles(gitignoreUrl, dataPath)
				if err != nil {
					log.Fatal(err)
				}
			},
		},
		{
			Name:    "g",
			Aliases: []string{"generate"},
			Usage:   "generate gitignore files",
			Action: func(c *cli.Context) {
				if c.NArg() != 1 {
					cli.ShowAppHelp(c)
				} else {
					generate(c.Args()[0])
				}
			},
		},
	}
	app.Run(os.Args)
}
