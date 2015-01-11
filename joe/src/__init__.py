import click

import handlers

@click.group()
def cli():
    '''Joe generates .gitignore files from the command line for you.'''
    pass

cli.add_command(handlers.ls)
cli.add_command(handlers.list)
