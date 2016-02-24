#!/usr/bin/env python

from setuptools import setup, find_packages


version = '0.0.7'

setup(
    name='joe',
    version=version,
    description='joe generates .gitignore files from the command line for you.',
    long_description=open('README.rst').read(),
    author='Karan Goel',
    author_email='karan@goel.io',
    license='MIT',
    keywords=['gitignore', 'git', 'github', 'command line', 'cli'],
    url='http://github.com/karan/joe',
    packages=find_packages(),
    install_requires=[
        'docopt>=0.6.1',
        'GitPython==1.0.2',
    ],
    entry_points={
        'console_scripts': [
            'joe=joe.joe:main'
        ],
    }
)
