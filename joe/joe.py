from os import walk

import click


@click.command(name='ls', help='List all available .gitignore files.')
def ls():
    click.echo('ls called yo')


@click.command(name='list', help='List all available .gitignore files.')
def list():
    click.echo('list called yo')


# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
#               help='The person to greet.')
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo('Hello %s!' % name)


@click.group()
def cli():
    '''Joe generates .gitignore files from the command line for you.'''
    pass


cli.add_command(ls)
cli.add_command(list)


if __name__ == '__main__':
    cli()
