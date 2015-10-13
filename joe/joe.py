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
  joe [NAME...]
  joe (-h | --help)
  joe --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""


import os
import sys

from docopt import docopt


__version__ = '0.0.6'


_ROOT = os.path.abspath(os.path.dirname(__file__))


def _get_data_dir(path):
    '''Returns the path to the directory matching the passed `path`.'''
    return os.path.dirname(os.path.join(_ROOT, 'data', path))


def _walk_gitignores():
    '''Recurse over the data directory and return all .gitignore file names'''
    gitignores = []
    for _root, _sub_folders, files in os.walk(DATA_DIR):
        gitignores += [f.replace('.gitignore', '')
                       for f in files if f.endswith('.gitignore')]
    return sorted(gitignores)


# Where all gitignore files are
DATA_DIR = _get_data_dir('*.gitignore')
# Load up names for all gitignore files
GITIGNORE_RAW = _walk_gitignores()
GITIGNORE = [filename.lower() for filename in GITIGNORE_RAW]


def _get_filenames():
    '''List all available .gitignore files.'''
    return ', '.join(GITIGNORE)


def _handle_gitignores(names):
    '''Generates and returns the gitignore contents.'''
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
    Given a raw_name, it will look in data/ and then data/Global/ for a
        matching .gitignore.
    An empty string as a default argument evaluates to None.
    directory must then be checked as string operations such as
        string + None return ''
    '''
    output = '\n#####=== %s ===#####\n' % raw_name
    if directory:
        filepath = os.path.join(DATA_DIR, '%s/%s.gitignore' %
                                (directory, raw_name))
    else:
        filepath = os.path.join(DATA_DIR, raw_name + '.gitignore')
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
    elif arguments['NAME']:
        print(_handle_gitignores(arguments['NAME']))
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
