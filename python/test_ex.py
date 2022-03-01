"""Tests about."""

#1 Test before coding

from area import rect_area

height = 3
width = 4
correct_answer = 12

answer = rect_area(heigh, width)
if answer == correct_answer:
    print("Test passed")
else:
    print("Test failed")

#2 How is testing?

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

#3
