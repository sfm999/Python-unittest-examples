""" tests/test_str.py
Super simple TestCase class. No dependencies on other files.
"""

import unittest

def setUpModule():
    print(f'Running setUpModule from {__name__}')

def tearDownModule():
    print(f'Running tearDownModule from {__name__}')

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()