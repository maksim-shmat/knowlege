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

import textwrap
import unittest

'''
class ContainerEqualityTest(unittest.TestCase):

    def testCount(self):
        self.assertCountEqual(
            [1, 2, 3, 2],
            [1, 3, 2, 3],
        )

    def testDict(self):
        self.assertDictEqual(
            {'a': 1, 'b': 2},
            {'a': 1, 'b': 3},
        )

    def testList(self):
        self.assertListEqual(
            [1, 2, 3],
            [1, 3, 2],
        )

    def testMultiLineString(self):
        self.assertMultiLineEqual(
            textwrap.dedent("""
            This string
            has more than one
            line.
            """),
            textwrap.dedent("""
            This string has
            more than two
            lines.
            """),
        )

    def testSequence(self):
        self.assertSequenceEqual(
            [1, 2, 3],
            [1, 3, 2],
        )

    def testSet(self):
        self.assertSetEqual(
            set([1, 2, 3]),
            set([1, 3, 2, 4]),
        )

    def testTuple(self):
        self.assertTupleEqual(
            (1, 'a'),
            (1, 'b'),
        )

RESULTS:

======================================================================
FAIL: testSet (unittest_ex.ContainerEqualityTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/jack/django2/knowlege/python/unittest_ex.py", line 153, in testSet
    self.assertSetEqual(
AssertionError: Items in the second set but not the first:
4

======================================================================
FAIL: testTuple (unittest_ex.ContainerEqualityTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/jack/django2/knowlege/python/unittest_ex.py", line 159, in testTuple
    self.assertTupleEqual(
AssertionError: Tuples differ: (1, 'a') != (1, 'b')

First differing element 1:
'a'
'b'

- (1, 'a')
?      ^

+ (1, 'b')
?      ^


----------------------------------------------------------------------
Ran 7 tests in 0.002s

FAILED (failures=7)
'''

#9 unittest assertIn()
# python3 -m unittest unittest_ex.py

import unittest

'''
class ContainerMembershipTest(unittest.TestCase):

    def testDict(self):
        self.assertIn(4, {1: 'a', 2: 'b', 3: 'c'})

    def testList(self):
        self.assertIn(4, [1, 2, 3])

    def testSet(self):
        self.assertIn(4, set([1, 2, 3]))
'''

#10 unittest exception

import unittest

'''
def raises_error(*args, **kwds):
    raise ValueError('Invalid value: ' + str(args) + str(kwds))


class ExceptionTest(unittest.TestCase):

    def testTrapLocally(self):
        try:
            raises_error('a', b='c')
        except ValueError:
            pass
        else:
            self.fail('Did not see ValueError')

    def testAssertRaises(self):
        self.assertRaises(
            ValueError,
            raises_error,
            'a',
            b='c',
        )
'''

#11 unittest fixtures

import random
import unittest

'''
def setUpModule():
    print('In setUpModule()')

def tearDownModule():
    print('In tearDownModule()')


class FixturesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('In setUpClass()')
        cls.good_range = range(1, 10)

    @classmethod
    def tearDownClass(cls):
        print('In tearDownClass()')
        del cls.good_range

    def setUp(self):
        super().setUp()
        print('\nIn setUp()')

        self.value = random.randint(
            self.good_range.start,
            self.good_range.stop - 1,
        )

    def tearDown(self):
        print('In tearDown()')
        del self.value
        super().tearDown()

    def test1(self):
        print('In test1()')
        self.assertIn(self.value, self.good_range)

    def test2(self):
        print('In test2()')
        self.assertIn(self.value, self.good_range)

RESULTS:
In setUpModule()
In setUpClass()

In setUp()
In test1()
In tearDown()
.
In setUp()
In test2()
In tearDown()
.In tearDownClass()
In tearDownModule()

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
'''

#12 unittest addcleanup

import random
import shutil
import tempfile
import unittest

'''
def remove_tmpdir(dirname):
    print('In remove_tmpdir()')
    shutil.rmtree(dirname)


class FixturesTest(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.tmpdir = tempfile.mkdtemp()
        self.addCleanup(remove_tmpdir, self.tmpdir)

    def test1(self):
        print('\nIn test1()')

    def test2(self):
        print('\nIn test2()')

RESULTS:
In test1()
In remove_tmpdir()
.
In test2()
In remove_tmpdir()
.
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
'''

#13 unittest subtest

import unittest

'''
class SubTest(unittest.TestCase):

    def test_combined(self):
        self.assertRegex('abc', 'a')
        self.assertRegex('abc', 'B')
        # Next not checked
        self.assertRegex('abc', 'c')
        self.assertRegex('abc', 'd')

    def test_with_subtest(self):
        for pat in ['a', 'B', 'c', 'd']:
            with self.subTest(pattern=pat):
                self.assertRegex('abc', pat)

RESULTS:
F
======================================================================
FAIL: test_combined (unittest_ex.SubTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/jack/django2/knowlege/python/unittest_ex.py", line 361, in test_combined
    self.assertRegex('abc', 'B')
AssertionError: Regex didn't match: 'B' not found in 'abc'

======================================================================
FAIL: test_with_subtest (unittest_ex.SubTest) (pattern='B')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/jack/django2/knowlege/python/unittest_ex.py", line 369, in test_with_subtest
    self.assertRegex('abc', pat)
AssertionError: Regex didn't match: 'B' not found in 'abc'

======================================================================
FAIL: test_with_subtest (unittest_ex.SubTest) (pattern='d')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/jack/django2/knowlege/python/unittest_ex.py", line 369, in test_with_subtest
    self.assertRegex('abc', pat)
AssertionError: Regex didn't match: 'd' not found in 'abc'

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=3)
'''

#14 unittest skip

import sys
import unittest

'''
class SkippingTest(unittest.TestCase):

    @unittest.skip('always skipped')
    def test(self):
        self.assertTrue(False)

    @unittest.skipIf(sys.version_info[0] > 2,
                     'only runs on python 2')

    def test_python2_only(self):
        self.assertTrue(False)

    @unittest.skipUnless(sys.platform == 'Darwin',
                         'only runs on macOS')
    def test_macos_only(self):
        self.assertTrue(True)

    def test_raise_skiptest(self):
        raise unittest.SkipTest('skipping via exception')

RESULTS:
ssss
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK (skipped=4)
'''

#15 unittest expectedfailure
