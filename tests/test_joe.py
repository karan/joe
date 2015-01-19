import unittest
from joe import joe


class TestJoe(unittest.TestCase):

    def test_fetch_gitignore_find_file(self):
        expected_gitignore = '\n#####=== python ===#####\n\n'
        expected_gitignore += open('./joe/data/Python.gitignore').read()
        self.assertMultiLineEqual(joe._fetch_gitignore('python'), expected_gitignore)
