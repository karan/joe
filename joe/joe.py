"""Joe.

Joe generates .gitignore files from the command line for you

Usage:
  joe (ls | list)
  joe [NAME...]
  joe (-h | --help)
  joe --version

Options:
  -h --help        Show this screen.
  --version     Show version.

"""

# import argparse
import os
import sys

from docopt import docopt
# import click


_ROOT = os.path.abspath(os.path.dirname(__file__))
def _get_data_dir(path):
    '''Returns the path to the directory matching the passed `path`.'''
    return os.path.dirname(os.path.join(_ROOT, 'data', path))


# Where all gitignore files are
DATA_DIR = _get_data_dir('*.gitignore')
# Load up names for all gitignore files
GITIGNORE_RAW = [f.replace('.gitignore', '') \
                    for f in next(os.walk(DATA_DIR))[2]]
GITIGNORE = [f.lower() for f in GITIGNORE_RAW]


# class PrintFilenamesAction(argparse.Action):
#     '''Prints a comma-separated list of all gitignore files we have.'''

#     def __init__(self, option_strings, dest, nargs=None, **kwargs):
#         if nargs is not None:
#             raise ValueError("nargs not allowed")
#         super(PrintFilenamesAction, self).__init__(option_strings, dest, **kwargs)

    
    
#     def __call__(self, parser, namespace, values, option_string=None):
#         _print_filenames()


# @click.command(name='ls', help='List all available .gitignore files.')
# def ls():
#     _print_filenames()


# @click.command(name='list', help='List all available .gitignore files.')
# def list():
#     _print_filenames()


# # @click.command(help='Output the .gitignore for passed languages.')
# # @click.argument('langs', nargs=-1, type=click.Path())
# # def generate(langs):
# #     '''Generates and sends the gitignore contents to stdout.'''
# #     output = '# Joe made this: https://goel.io/joe\n'
# #     filepath = os.path.join(DATA_DIR, GITIGNORE_RAW[GITIGNORE.index(name)] + '.gitignore')
# #     click.echo(langs)


# @click.group()
# def known_cli():
#     '''Joe generates .gitignore files from the command line for you.'''
#     pass

# known_cli.add_command(ls)
# known_cli.add_command(list)


def _print_filenames():
    '''List all available .gitignore files.'''
    print ', '.join(GITIGNORE)


def _handle_gitignores(names):
    '''Generates and sends the gitignore contents to stdout.'''
    output = '# Joe made this: https://goel.io/joe\n'
    for name in names:
        raw_name = GITIGNORE_RAW[GITIGNORE.index(name)]
        output += '\n#####=== %s ===#####\n' % raw_name
        filepath = os.path.join(DATA_DIR, raw_name + '.gitignore')
        output += '\n'
        with open(filepath) as f:
            output += f.read()
    print output


if __name__ == '__main__':

    arguments = docopt(__doc__, version='Joe 0.0.0')
    # print(arguments)

    if (arguments['ls'] or arguments['list']):
        _print_filenames()
    else:
        _handle_gitignores(arguments['NAME'])
