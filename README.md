![](http://i.imgur.com/y8g506n.png?1)

# joe

A .gitignore magician in your command line. Joe generates `.gitignore` files from the command line for you.

## Features

- Written in uncomplicated Python
- Easy to install
- Stupidly easy to use
- Supports all Github-supported `.gitignore` files
- Warns if target directory isn't a git repo
- Works on Mac, Linux and Windows

## Installation

### Option 1: Homebrew

```bash
$ brew install gitignore
```

### Option 2: Pip

```bash
$ pip install joe
```

### Option 2: From source

```bash
$ git clone git@github.com:karan/joe.git
$ cd joe/
$ python setup.py install
```

## Usage

### Basic usage


```bash
$ joe java    # outputs .gitignore file for java to stdout
```

### Overwrite existing `.gitignore` file

```bash
$ joe java > .gitignore    # saves a new .gitignore file for java
```

### Append to existing `.gitignore` file

```bash
$ joe java >> .gitignore    # appends new .gitignore file for java
```

### Multiple languages

```bash
$ joe java javascript python    # saves a new .gitignore file for multiple languages
```

### List all available files

```bash
$ joe ls

# OR

$ joe list
```

Output:

> actionscript, ada, agda, android, appceleratortitanium, archlinuxpackages, autotools, c++, c, cakephp, cfwheels, chefcookbook, clojure, cmake, codeigniter, commonlisp, composer, concrete5, coq, craftcms, dart, delphi, dm, drupal, eagle, elisp, elixir, episerver, erlang, expressionengine, extjs, fancy, finale, forcedotcom, fortran, fuelphp, gcov, gitbook, go, gradle, grails, gwt, haskell, idris, igorpro, java, jboss, jekyll, joomla, jython, kohana, labview, laravel, leiningen, lemonstand, lilypond, lithium, lua, magento, maven, mercury, metaprogrammingsystem, meteor, nanoc, nim, node, objective-c, ocaml, opa, opencart, oracleforms, packer, perl, phalcon, playframework, plone, prestashop, processing, python, qooxdoo, qt, r, rails, rhodesrhomobile, ros, ruby, rust, sass, scala, scons, scrivener, sdcc, seamgen, sketchup, stella, sugarcrm, swift, symfony, symphonycms, tex, textpattern, turbogears2, typo3, umbraco, unity, visualstudio, vvvv, waf, wordpress, xojo, yeoman, yii, zendframework, zephir
