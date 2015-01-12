import os

import click


_ROOT = os.path.abspath(os.path.dirname(__file__))
def _get_data_dir(path):
    '''Returns the path to the directory matching the passed `path`.'''
    return os.path.dirname(os.path.join(_ROOT, 'data', path))


# Where all gitignore files are
DATA_DIR = _get_data_dir('*.gitignore')
# Load up names for all gitignore files
GITIGNORE = [f.replace('.gitignore', '').lower() \
                for f in next(os.walk(DATA_DIR))[2]]


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


@click.group()
def cli():
    '''Joe generates .gitignore files from the command line for you.'''
    pass


cli.add_command(ls)
cli.add_command(list)


if __name__ == '__main__':
    cli()
