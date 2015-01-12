import os
import sys

import click


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


def _print_filenames():
    '''Prints a comma-separated list of all gitignore files we have.'''
    click.echo(GITIGNORE[0], nl=False)
    for f in GITIGNORE[1:]:
        click.echo(', ', nl=False)
        click.echo(f, nl=False)
    click.echo()


@click.command(name='ls', help='List all available .gitignore files.')
def ls():
    _print_filenames()


@click.command(name='list', help='List all available .gitignore files.')
def list():
    _print_filenames()


# @click.command(help='Output the .gitignore for passed languages.')
# @click.argument('langs', nargs=-1, type=click.Path())
# def generate(langs):
#     '''Generates and sends the gitignore contents to stdout.'''
#     output = '# Joe made this: https://goel.io/joe\n'
#     filepath = os.path.join(DATA_DIR, GITIGNORE_RAW[GITIGNORE.index(name)] + '.gitignore')
#     click.echo(langs)


@click.group()
def known_cli():
    '''Joe generates .gitignore files from the command line for you.'''
    pass

known_cli.add_command(ls)
known_cli.add_command(list)


if __name__ == '__main__':
    cli()
