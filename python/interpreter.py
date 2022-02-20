"""Work into Python interpreter."""

#1 Read doc string
>>> import jill  # equally jill.py
>>> print(jill.__doc__)
Hello I`m Jill, nice to meet you!

#2 Where is file

>>> import jill
>>> print(jill.__file__)
/home/basecamp/durango/pluto/jill.py

#3 Open web page from Python interpreter
#import os # ???
>>> import webbrowser
>>> webbrowser.open('http://www.python.org')
True

#4 How many times?

>>> import time
>>> time.asctime()
'Sat Feb 19 16:54:56 2022'

#5
