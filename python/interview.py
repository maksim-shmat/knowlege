"""Potensially may be questions."""

#1 Objects.

An object consists of attributes and methods. An attibute is merely a variable
that is part of an object, and a method is more or less a function that is
stored in a an attribute. One difference between (bound) methods and other
functions is that methods always receive the object they are part of as theif
first argument, usually called self.

#2 Classes

A class represents a set (or kind) of objects, and every object (instance)
has a class. The class`s main task is to define the methods its instances
will have.

#3 Polymorphism

Polymorphism is the characteristic of being able to treat objects of different
types an classes alike - you don`t need to know which class an object belongs
to in order to call one of its methods.

#4 Encapsulation

Objects may hide (or encapsulate) their internal state. In some languages,
this means that their state (their attributes) is available only through their
methods. In Python, all attributes are publicly available, but programmers
should still be careful about accessing an object`s state directly, since they
might unwittingly make the state inconsistent in some way.

#5 Inheritance

One class may be the subclass of one or more other classes.
The subclass then inherits all the methods of the superclasses. You can use
more than one superclass, and this feature can be used to compose orthogonal
(independent and unrealated) pieces of functionality. A common way of 
inplementing this is using a core superclass along with one or more mix-in
superclasses.

#6 Interface and introspection

In general, you don`t want prod an object too deeply. You rely on plymorphism
an call the methods you need. However, if you want to find out what methods or
attibutes an object has, there are functions that will do the job for you.

#7 Abstract base classes

Using the abc module, you can create so-called abstract base classes, which
serve to identify the kind of functionality a class should provide, without
actually implementing it.

#8 Object-oriented disign

There are many opinions about how (or whether!) to do object-oriented design.
No matter where you stand on the issue, it`s understand your problem
thoroughly and to create a design that is easy to understand.

#9 Exception objects

Exceptional situations (such as when an error has occurred) are represented by
exception objects. These can be manipulated in several ways, but if ignored,
they terninate your program.

#10 Raising exceptions

You can raise exceptions with the raise statement. It accepts either an 
exception class or an exception instance as its arguments. You can also supply
two arguments (an exception and an error message). If you call raise with no
arguments in an except clause, it "reraises" the exception caught by that
clause.

#11 Custom exception clausses

You can create your own kinds of exceptions by subclassing Exception.

#12 Catching exceptions

You catch exceptions with the except clause of a try statement. If you don`t
specify a class in the except clause, all exceptions are caught. You can
specify more than one class by putting them in a tupple. If you give two arguments to except, the second is bound to the exception object. You can have
several except clauses in the same try/except statement, to react differently 
to different exception.

#13 else clauses

You can use an else clause in addition to except. The else clause is executed
if no exceptions are raised in the main try block.

#14 finally

You can use try/finally if you need to make sure that some code (for example,
cleanup code) is executed, regardless of whether or not an exception is
raised. This code is then put in the finally clause.

#15 Exception and functions

When you raise an exception inside a function, it propagates to the place
where the function was called. (The same goes for methods.)

#16 Warnings

Warnings are similar to exceptions but will (in generall) just print out an
error message. You can specify a warning catergory, which is a subclass of
Warning.

#17 Magic methods

Several special methods (with names beginning and ending with double
underscores) exist in Python. These methods diffeer quite a bit in function,
but most of them are called automatically by Python under certain
circumstances. (For example, __init__ is called after object cration.)

#18 Constructors

These are common to many objects-oriented languages, and you`ll probably
implement one for almost every class you write. Constructors are named init
and are automatically called immediately after an object is created.

#19 Overriding

A class can override methods (or any other attributes) defined in it`s
superclasses simply by implementing the methods. If the new method needs to
call the overridden version, it can either call the unbound version from the
superclass directly (old-style classes) or use the super function (new-style
classes).

#20 Sequences and mappings

Creating a sequence or mapping of your own requires implementing all the
methods of the sequence and mapping protocols, including such magic methods
as getitem and __setitem__. By subclassing list (or UserList) and dict (or
UserDict), you can save a lot of work.

#21 Iterators

An iterator is simply an object that has a __next__ method. Iterators can be
used to iterate over a set of values. When there are no more values, the next
method should raise a StopIteration exception. Iterable objects have an
__iter__ method, which returns an iterator, and can be used in for loops,
just like sequences. Often, and iterator is also iterable; that is, it has
an __iter__ method that returns the iterator itself.

#22 Generators

A generator-function (or method) is a function (or method) that contains the
keyword yield. When called, the generator-function returns a generator, which
is a special type of iterator. You can interact with an active generator from
the outside be using the methods send, throw, and close.

#23 Eight Queens

The Eight Queens problem is well known is computer science and lends itself
easily to implementation with generators. The goal is to position eight
queens on a chessboard so that none of the queens is in a position from which
she can attack any of the others.

#24 Read/write

File-like objects: A file-like object is (informally) an object that
supports a set of methods such as read and readline (and possibly write and
writelines).

Opening and closing files: You open a file with the open function, by
supplying a file name. If you want to make sure your file is closed, even if
something goes wrong, you can use the with statement.

Modes and file types: When opening a file, you can also supply a mode, such
as 'r' for read mode or 'w' for write mode. By appending 'b' to your mode,
you can open files as binary files and turn off Unicode ecnoding and newline
substitution.

Standard streams: The three standard files (stdin, stduot, and stderr, found
in the sys module) are file-like objects that implement the UNIX standard I/O
mecanism (also available in Windows).

Reading and writing: You read from a file of file-like object using the
method read. You write with the method write.

Reading and writing lines: Your can read lines from a file using readine and
readlines. You can write files with writelines.

Iterating over file contents: There are many ways of iterating over file
contents. It is most common to iterate over the lines of a text file, and
you can do this by simply iterating over the file itself. There are other
methods too, such as using readlines, that are compatible with older versions
of Python.

#25 Modules

Modules: A module is basically a subprogram whose main function is to define
things, such as function, classes, and variables. If a module contains any
test code, it should be placed in an if statement that checks whether
name == '__main__'. Modules can be imported if they are in the PYTHONPATH.
You import a module stored in the file foo.py with the statement import foo.

Packages: A package is just a module that contains other modules. Packages are
implemented as directories that contain a file named __init__.py.

Exploring modules: After you have imported a module into interactive
interpreter, you can explore it in many ways. Among them are using dir,
examining th __all__ variable, and using the help function. The documentation
and the source code can also be excellent sources of information and insight.

The standard library: Python comes with several modules included, collectively
called the standard library:
    sys: A module that gives you access to several variables and functions
    that are tightly linked with the Python interpreter.

    os: A module that gives you access to several variables and functions
    that are tightly linked with the operating system.

    fileinput: A module that makes it easy to iterate over the lines of
    several files of streams.

    sets, heapq, and deque: Three modules that provide three useful data
    structures. Sets are alse available in the form of the built-in type set.

    time: A module for getting the current time and for manipulating and
    formating times and dates.

    random: A module with functions for generating random numbers, choosing
    random elements from a sequence, and shuffling the elements of a list.

    shelve: A module for creating a persistent mapping, which stores it`s
    contents in a database with a given file name.

    re: A module with support for regular expressions.

#26 GUI

Graphical user interfaces(GUI`s): GUI`s are useful in making your programs
more user friendly. Not all programs need them, but whenever your program
interacts with a user, a GUI is probably helpful.

Tkiner: Tkinter is a mature and widely available cross-platform GUI toolkit
for Python.

Layout: You can position components quite simply by specifying their geometry
directly. However, to make them behave properly when their containing window
is resized, you will need to use some sort of layout manager.

Event handling: Actions performed by the user trigger events in the GUI
toolkit. To be of any use, your program will probably be set up to react to
some of these events; otherwise, the user won`t be able to interact to some
of these events; otherwise, the user won`t be able to interact with it. In
Tkinter, event handlers are added to components with the bind method.

#27 SQL

The Python DB API: This API provides a simple, standardized interface to
which database wrapper modules should confirm, to make it  easier to write programs that will work with several different databases.

Connections: A connection object represents the communication link with the
SQL database. From it, you can get individual cursors, using the cursor method. You also use the connection object to commit or roll back transactions.
After you`re finished with the database, the connection can be closed.

Cursors: A cursor in used to execute queries and to examine the  results.
Resulting rows can be retrived one by one or many (or all) at once.

Types and special values: The DB API specifies the names of a set of
constructiors and special values. The constructors deal with date and time
objects, as well as binary data objects. The special values represent the
types of the relational database, such as STRING, NUMBER, and DATATIME.

SQLite: This is a small, embedded SQL database, whose Python wrapper is
included in the standard Python distribution under the name sqlite3. It`s
fast and simple to use and does not require a separate server to be set up.

#28 Sockets

Sockets and the socket module: Sockets are information channels that let
programs (processes) communicate, possibly across a network. The socket module
gives you low-level access to both client and server sockets. Server sockets
listen at a given address for client connections, while clients simply connect
directly.

urllib and urllib2: These models let you read and download data from various
servers, given a URl to the data source. The urllib module is a simpler
implemetation, while urllib2 is very extensible and quit powerful. Both work
through strightforward functions such as urlopen.

The SocketServer framework: This is a network of synchronous server base
classes, found in the standard library, which lets you write servers quite
easily. There is even support for simple web (HTTP) servers with CGI. If you
want to handle serveral connections simultaneously, you need to use a
forking or threading mix-in class.

select and poll: These two functions let you consider a set of connections and
find out which ones are ready for reading and writing. This means that you can
serve several connections piecemeal, in a round-robin fashion. This gives the
illusion of handling several connections at the same time and, although
superficially a bit more complicated to code, is a much more scalable and
efficient solution than threading or forking.

Twisted: this framework, from Twisted Matrix Laboratories, is very rich and
complex, with support for most major network protocols. Eve though it is
large and some of the idioms used may seem a bit foreign, basic usage is very
simple and intuitive. The Twisted framework is also asynchronous, so it`s
very efficient and scalable. If you have Twisted available, it may very well
be the best choice for many custom network applications.

#29 Parsing/scraping

Screen scraping: This is the practice or downloading web pages automatically
and extracting information from them. The Tidy program and its library version
are useful tools for fixing ill-formed HTML before using an HTML parser.
Another option is to use Beautiful Soup, which is very forgiving of messy
input.

CGI: The Common Gateway Interface is a way of creating dynamic web pages, by
making a web server run and communicate with your programs and display the
results. The cgi and cgiltb modules are useful for writing CGI scripts. CGI
scripts are usually invoked from HTML forms.

Web services: Web services are to programs with (dynamic) web pages are to
people. You may see them as a way of making it possible to do network
programming at a higher level of abstraction. Common web service standards are
RSS (and its relatives, RDF and Atom), XML-RPC, and SOAP.

#30 Tests

Test-driven programming: Basically, test-driven programming means to test
first, code later. Tests let you rewrite your code with confidence, making
your development and maintenance more flexible.

The doctest and modules: These are indispensible tools if you want to do unit
testing in Python. The doctest module is designed to check examples in
docstrings but can easily be used to design test suites. For more flexibility
and structure in your suites, the unittest framework is very useful.

PyChecker and PyLint: These two tools read source code and point out potential
(and actual) problems, They check everything from short variable names to
unreachable pieces of code. With a little to make sure all of your rewrites
and refactorings conform to your coding standards.

Profiling: If you really care about speed and want to optimize your program
(do this if it`s absolutely necessary), you should profile it first. Use the
profile or cProfile module to find bottlenecks in your code.

#31
