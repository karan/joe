#!/usr/bin/env python

from setuptools import setup, find_packages


version = '0.0.5'

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
    download_url=('https://github.com/karan/joe/archive/%s.tar.gz' % version),
    packages=find_packages(),
    package_data={
        'joe': ['data/*.gitignore', 'data/Global/*.gitignore']
    },
    install_requires=[
        'docopt>=0.6.1',
    ],
    entry_points={
        'console_scripts': [
            'joe=joe.joe:main'
        ],
    }
)
