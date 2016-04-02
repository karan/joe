r"""
     _
    (_)   _      __
    | | /'_`\  /'__`\
    | |( (_) )(  ___/
 _  | |`\___/'`\____)
( )_| |
`\___/'


joe generates .gitignore files from the command line for you

Usage:
  joe (ls | list)
  joe update
  joe [NAME...]
  joe (-h | --help)
  joe --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""


import os
import shutil
import sys

from docopt import docopt
import git


__version__ = '0.0.7'


# Where all gitignore files are
_DATA_DIR_NAME = '.joe-data'
_DATA_DIR_PATH = '%s/%s' % (os.path.expanduser('~'), _DATA_DIR_NAME)

REMOTE_URL = "https://github.com/github/gitignore"


def _walk_gitignores():
    '''Recurse over the data directory and return all .gitignore file names'''
    gitignores = []
    for _root, _sub_folders, files in os.walk(_DATA_DIR_PATH):
        gitignores += [f.replace('.gitignore', '')
                       for f in files if f.endswith('.gitignore')]
    return sorted(gitignores)


# Load up names for all gitignore files
GITIGNORE_RAW = _walk_gitignores()
GITIGNORE = [filename.lower() for filename in GITIGNORE_RAW]


def _update_instructions():
    return ('No .gitignore files found. '
            'Retry after running:\n\n    $ joe update')


def _create_again(directory):
    if os.path.isdir(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)
    return directory


def _update():
    '''Update gitignore files.'''
    print('Updating gitignore files.. '),
    _create_again(_DATA_DIR_PATH)
    repo = git.Repo.init(_DATA_DIR_PATH)
    origin = repo.create_remote('origin', REMOTE_URL)
    origin.fetch()
    origin.pull(origin.refs[0].remote_head)
    return 'Done'


def _get_filenames():
    '''List all available .gitignore files.'''
    if not GITIGNORE:
        return _update_instructions()
    return ', '.join(GITIGNORE)


def _handle_gitignores(names):
    '''Generates and returns the gitignore contents.'''
    if not GITIGNORE:
        return _update_instructions()

    output = '#### joe made this: http://goel.io/joe\n'
    failed = []
    for name in names:
        try:
            raw_name = GITIGNORE_RAW[GITIGNORE.index(name.lower())]
            output += _fetch_gitignore(raw_name)
        except ValueError:
            failed.append(name)
    if failed:
        sys.stderr.write((
            'joe doesn\'t know the following gitignores:'
            '\n%s\n'
            'Run `joe ls` to see list of available gitignores.\n'
        ) % "\n".join(failed))
        output = []

    return output


def _fetch_gitignore(raw_name, directory=''):
    '''Returns a the corresponding .gitignore as a string.

    It is assumed that raw_name is a valid .gitignore filename.
    Given a raw_name, it will look in data directory for a
        matching .gitignore.
    An empty string as a default argument evaluates to None.
    directory must then be checked as string operations such as
        string + None return ''
    '''
    output = '\n#####=== %s ===#####\n' % raw_name
    if directory:
        filepath = os.path.join(_DATA_DIR_PATH, '%s/%s.gitignore' %
                                (directory, raw_name))
    else:
        filepath = os.path.join(_DATA_DIR_PATH, raw_name + '.gitignore')
        output += '\n'
    try:
        with open(filepath) as gitignore:
            output += gitignore.read()
        return output
    except IOError:
        return _fetch_gitignore(raw_name, 'Global')


def main():
    '''joe generates .gitignore files from the command line for you'''
    arguments = docopt(__doc__, version=__version__)

    if arguments['ls'] or arguments['list']:
        print(_get_filenames())
    elif arguments['update']:
        print(_update())
    elif arguments['NAME']:
        print(_handle_gitignores(arguments['NAME']))
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
