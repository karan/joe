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
  joe (add | a) <gitignore>
  joe (remove | rm) <gitignore>
  joe [NAME...]
  joe (-h | --help)
  joe --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""


import os
import sys
import platform
import operator

from docopt import docopt
from shutil import copyfile
from os.path import expanduser
from termcolor import colored


__version__ = '0.0.6'


_ROOT = os.path.abspath(os.path.dirname(__file__))
PLATFORM = platform.system()
_HOME = expanduser('~')


def get_share_folder():
    paths = {
        'Darwin' : os.path.join(_HOME, '.joe'),
        'Linux' : os.path.join(_HOME, '.joe'),
        'Windows' : os.path.join(_HOME, '.joe')
    }
    path = paths[PLATFORM] or None
    if path:
        if not os.path.isdir(path):
            os.mkdir(path)
        return path
    else:
        print 'This is not a supported OS.'

def _get_data_dir(path):
    '''Returns the path to the directory matching the passed `path`.'''
    return os.path.dirname(os.path.join(_ROOT, 'data', path))


def _walk_gitignores():
    '''Recurse over the data directory and return all .gitignore file names'''
    _gitignores = {}
    for root, subFolders, files in os.walk(DATA_DIR):
        for f in files:
            if f.endswith('.gitignore'):
                raw_name = f.replace('.gitignore', '')
                _gitignores[raw_name.lower()] = colored(raw_name, 'blue')
    for root, subFolder, files in os.walk(get_share_folder()):
        for f in files:
            if f.endswith('.gitignore'):
                raw_name = f.replace('.gitignore', '')
                _gitignores[raw_name.lower()] = colored(raw_name + '*', 'green')

    return sorted(_gitignores.items(), key=operator.itemgetter(0))


# Where all gitignore files are
DATA_DIR = _get_data_dir('*.gitignore')
SHARED_DATA_DIR = get_share_folder()
# Load up names for all gitignore files
GITIGNORE_RAW = _walk_gitignores()
GITIGNORE = [filename for filename,displayname in GITIGNORE_RAW]
GITIGNORE_DISPLAY = [displayname.lower() for filename,displayname in GITIGNORE_RAW]


def _print_filenames():
    '''List all available .gitignore files.'''
    print ', '.join(GITIGNORE_DISPLAY)


def _handle_gitignores(names):
    '''Generates and sends the gitignore contents to stdout.'''
    output = '#### joe made this: https://goel.io/joe\n'
    for name in names:
        try:
            (raw_name, display_name) = GITIGNORE_RAW[GITIGNORE.index(name.lower())]
        except ValueError:
            print ('Uh oh! Seems like joe doesn\'t know what %s is.\n'
                   'Try running `joe ls` to see list of available gitignore '
                   'files.') % name
            break
        output += _fetch_gitignore(raw_name)
    print output


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
    custom_filepath = os.path.join(SHARED_DATA_DIR, raw_name + '.gitignore')
    if directory:
        filepath = os.path.join(DATA_DIR, '%s/%s.gitignore' %
                                (directory, raw_name))
    else:
        filepath = os.path.join(DATA_DIR, raw_name + '.gitignore')
        output += '\n'
    try:
        with open(custom_filepath) as gitignore:
            output += gitignore.read()
        return output
    except IOError:
        try:
            with open(filepath) as gitignore:
                output += gitignore.read()
            return output
        except IOError:
            return _fetch_gitignore(raw_name, 'Global')

def _add_custom_gitignore(new_gitignore):
    '''Add a custom gitignore to the joe folder in the shared data folder.'''
    share_folder = get_share_folder()
    gitignore_file = new_gitignore if new_gitignore.endswith('.gitignore') else new_gitignore + '.gitignore'
    if os.path.isfile(new_gitignore):
        can_copy_file = True
        if (os.path.isfile(os.path.join(share_folder, gitignore_file))):
            can_copy_file = _confirm_selection('The file ' + colored(new_gitignore, 'green') + colored(' already exists.', 'red') + ' Do you wish to '+ colored('overwrite it', 'red') + '?', "no")
        if can_copy_file:
            try:
                copyfile(new_gitignore, os.path.join(share_folder, gitignore_file))
                print colored(new_gitignore, 'green') + ' was successfully added to joe.'
            except OSError:
                print 'Could not copy ' + colored(new_gitignore, 'red') + ' to ' + share_folder + '.\nCheck your permissions for both'
        else:
            print 'Ignoring ' + colored(new_gitignore, 'blue')
    else:
        print 'Could not copy ' + colored(new_gitignore, 'red') + ' to ' + colored(share_folder, 'red') + '.\nCheck your permissions for both'

def _remove_custom_gitignore(gitignore_to_remove):
    '''Remove a custom gitignore from the joe folder in the shared data folder.'''
    share_folder = get_share_folder()
    gitignore_file = gitignore_to_remove if gitignore_to_remove.endswith('.gitignore') else gitignore_to_remove +  '.gitignore'
    if os.path.isfile(os.path.join(share_folder, gitignore_file)):
        can_remove_file = _confirm_selection('This will remove ' + colored(gitignore_to_remove, 'red') + ' from your custom gitignores. Do you wish to continue?', "yes")
        if can_remove_file:
            try:
                os.remove(os.path.join(share_folder, gitignore_file))
                print 'The file ' + colored(gitignore_to_remove, 'red') + ' was successfully removed.'
            except OSError:
                print 'Could not remove ' + colored(gitignore_to_remove, 'red') + ' from ' + colored(share_folder, 'red') + '.\nCheck your permissions.'
        else:
            print 'Ok, ignoring ' + colored(gitignore_to_remove, 'green')
    else:
        print 'The file ' + colored(os.path.join(share_folder, gitignore_file), 'red') + ' was not found'

def _confirm_selection(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " ["+colored('Y', 'green')+"/n] "
    elif default == "no":
        prompt = " [y/"+colored('N', 'red')+"] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

def main():
    '''joe generates .gitignore files from the command line for you'''
    arguments = docopt(__doc__, version=__version__)

    if arguments['ls'] or arguments['list']:
        _print_filenames()
    elif (arguments['add'] or arguments['a']):
        _add_custom_gitignore(arguments['<gitignore>'])
    elif (arguments['remove'] or arguments['rm']):
        _remove_custom_gitignore(arguments['<gitignore>'])
    elif (arguments['NAME']):
        _handle_gitignores(arguments['NAME'])
    else:
        print __doc__


if __name__ == '__main__':
    main()
