"""Unittest about."""

### Basic example

import unittest

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

######
import unittest

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50, 50))

###
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50, 50),
               'incorrect default size')

        def test_widget_resize(self):
            self.widget.resize(100, 150)
            self.assertEqual(self.widget.size(), (100, 150),
                    'wrong size after resize')

######
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()

######
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

#1 unittest for doctest_ex.py file

import unittest, doctest_ex

class ProductTextCase(unittest.TestCase):
    def test_integers(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                p = doctest_ex.product(x, y)
                self.assertEqual(p, x * y, 'Float multiplication failed')

    def test_floats(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                x = x / 10
                y = y / 10
                p = doctest_ex.product(x, y)
                self.assertEqual(p, x * y, 'Float multiplication failed')

if __name__ == '__main__': unittest.main()

#2 Calling external checkers using the subprocess module
# pychecker???
# Other way call PyChecker??? and PyLint from CLI ($ pychecker, $ pylint)

import unittest, doctest_ex
from subprocess import Popen, PIPE

class ProductTestCase(unittest.TestCase):
    # Insert previous tests here, from #1
    def test_with_PyChecker(self):
        cmd = 'pychecker', '-Q', doctest_ex.__file__.rstrip('c')
        pychecker = Popen(cmd, stdout=PIPE, stderr=PIPE)
        self.assertEqual(pychecker.stdout.read(),'')

    def test_with_PyLint(self):
        cmd = 'pylint', '-rn', 'doctest_ex'
        pylint = Popen(cmd, stdout=PIPE, stderr=PIPE)
        self.assertEqual(pylint.stdout.read(),'')

if __name__ == '__main__': unittest.main()

#3
