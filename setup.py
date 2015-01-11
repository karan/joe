#!/usr/bin/env python

from setuptools import setup

setup(
    name='joe',
    version='0.0.0',
    description='A .gitignore magician in your command line.',
    author='Karan Goel',
    license='MIT',
    keywords = "gitignore command line cli",
    author_email='karan@goel.io',
    url='http://github.com/karan/joe',
    include_package_data=True,
    package_data = {
        'src': ['data/*.gitignore']
    },
    install_requires=[
        "click==3.3",
    ],
    entry_points = {
        'console_scripts': [
            'joe = joe.src:cli'
        ],
    }
)
