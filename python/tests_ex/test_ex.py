"""Tests about."""

##1 Test before coding

from area import rect_area

height = 3
width = 4
correct_answer = 12

answer = rect_area(heigh, width)
if answer == correct_answer:
    print("Test passed")
else:
    print("Test failed")

##2 How is testing?

1. Figure out the new fearure you want. Possibly document it and then write
a test for it.

2. Write some skeleton code for the feature so that your program runs without
any syntax errors or the like, but so your test still fails. It is important
to see you test fail, so you are sure that it actually can fail. It there is
somtething wrong with the test and it always succeeds no matter what (this
has happened to me many times), you aren`t really testing anything. This bears
repeating: see your test fail before you try to make it succeed.

3. Write dummy code for your skeleton, just to appease the test. This doesn`t
have to accurately implement the functionality; it just needs to make the test
pass. This way, you can have all your tests pass all the time when developing
(except the first time you run the test, remember?), even while initially
implementing the functionality.

4. Rewrite (or refactor) the code that it actually does what it`s supposed to,
all the while making sure that your test keeps succeeding.

##3 unittest for files name_function_for_names.py and names_for_test_ex.py

import unittest
from name_function_for_names import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function_for_names.py'."""

    def test_first_last_name(self):
        """Names how: 'Janis Joplin' is work right?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Names now: 'Wolfgang Amadeus Mozart' is worked?"""
        formatted_name = get_formatted_name(
                'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()

Results:
    .
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

##4 assert methods from unittest

assertEqual(a, b)  # check that a == b
assertNotEqual(a, b)  # check that a != b
assertTrue(x)  # check that x is true
assetFalse(x)  # check that x is False
assertIn('?', list)  # check that '?' into list
assertNotIn('?', list)  #check that '?' not into list

##5 Test for survey.py

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for class AnonymousSurvey"""

    def setUp(self):
        """Set list of answers for tests."""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Check that one answer is save right."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_stor_three_responses(self):
        """Check that 3 answers will be saved right."""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()

Results:
..  # . is check one test, E = Error, F = Failed
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

##6
