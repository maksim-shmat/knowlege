"""unittest about."""

#1 run this: $ python3  -m unittest unittest_simple.py
'''
RESULTS:
.  # . - OK
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''

#2 verbose: $ python3 -m unittest -v unittest_simple.py
'''
RESULTS:
test (unittest_simple.SimplisticTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''

#3 unittest outcomes
# run it with: $ python3 -m unittest unittest_outcomes.py
'''
import unittest


class OutcomesTest(unittest.TestCase):

    def testPass(self):
        return

    def testFail(self):
        self.assertFalse(True)

    def testError(self):
        raise RuntimeError('Test error!')
'''

#4 unittest fail with message
# run: $ python3 -m unittest -v unittest_failwithmessage.py

import unittest

'''
class FailureMessageTest(unittest.TestCase):

    def testFail(self):
        self.assertFalse(True, 'failure message goes here')
'''

#5 unittest truth
# run: $ python3 -m unittest -v unittest_truth.py

import unittest
'''

class TruthTest(unittest.TestCase):

    def testAssertTrue(self):
        self.assertTrue(True)

    def testAssertFalse(self):
        self.assertFalse(False)
'''

#6 unittest equality

import unittest

'''
class EqualityTest(unittest.TestCase):

    def testExpectEqual(self):
        self.assertEqual(1, 3 -2)

    def testExpectEqualFails(self):
        self.assertNotEqual(2, 3 - 2)

    def testExpectNotEqual(self):
        self.assertNotEqual(2, 3 - 2)

    def testExpectNotEqualFails(self):
        self.assertNotEqual(1, 3 - 2)
'''

#7 unittest almost equal

import unittest

'''
class AlmostEqualTest(unittest.TestCase):

    def testEqual(self):
        self.assertEqual(1.1, 3.3 - 2.2)

    def testAlmostEqual(self):
        self.assertAlmostEqual(1.1, 3.3 - 2.2, place=1)

    def testNotAlmostEqual(self):
        self.assertNotAlmostEqual(1.1, 3.3 - 2.0, place=1)
'''

#8 unittest equality container

import testwrap
import unittest


class ContainerEqualityTest(unittest.TestCase):

    def testCount
