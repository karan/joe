package main

import (
  "fmt"
  "github.com/codegangsta/cli"
  "os"
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
        fmt.Println("listing shit")
      },
    },
    {
      Name:    "u",
      Aliases: []string{"update"},
      Usage:   "update all available gitignore files",
      Action: func(c *cli.Context) {
        fmt.Println("updating shit")
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
          fmt.Println("generating shit")
          fmt.Println(c.Args()[0])
        }
      },
    },
  }
  app.Run(os.Args)
}
