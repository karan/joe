#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='joe',
    version='0.0.0',
    description='A .gitignore magician in your command line.',
    author='Karan Goel',
    license='MIT',
    keywords="gitignore command line cli",
    author_email='karan@goel.io',
    url='http://github.com/karan/joe',
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
