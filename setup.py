#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='joe',
    version='0.0.3',
    description='joe generates .gitignore files from the command line for you.',
    long_description=open('README.md').read(),
    author='Karan Goel',
    author_email='karan@goel.io',
    license='MIT',
    keywords=['gitignore', 'git', 'github', 'command line', 'cli'],
    url='http://github.com/karan/joe',
    download_url='https://github.com/karan/joe/archive/0.0.2.tar.gz',
    packages=find_packages(),
    package_data={
        'joe': ['data/*.gitignore']
    },
    install_requires=[
        "docopt==0.6.1",
    ],
    entry_points={
        'console_scripts': [
            'joe=joe.joe:main'
        ],
    }
)
