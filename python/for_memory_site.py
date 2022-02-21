map(func, seq[, seq, ...])  # Applies the function to all the elements in the sequences

filter(func, seq)  # Returns a list of those elements for which the function is true

reduce(func, seq[, initial])  # Equivalent to func(func(func(func(seq[0], seq[1], seq[2]),...)

sum(seq)  # Returns the sum of all the elements of seq

apply(func[,args[,kwargs]])  # Call the function, optionall supplying argument

=================

chr(n)  # Returns a one-character string when passed ordinal n(0 <= n <= 256)

eval(source[,globals[,locals]])  # Evaluates a string as an expression and returns the value

exec(source[,globals[,locals]])  # Evaluates and executes a string as a statement

enumerate(seq)  # Yields (index, value) pairs suitable for iteration

ord(c)  # Returns the integer ordinal value of a one-character string

range([start,]stop[,step])  # Creates a list of integers

sorted(seq[, cmp][,key][,reverse])  # Returns a list with the values of seq in sorted order

zip(seq1, seq2, ...)  # Creates a new sequence suitable for parallel iteration

=================

callable(object)  # Determines if the object is callable (such as a function or a method)

getattr(object, name[,default])  # Gets the value of an attribute, optionally providing a default

hasattr(object, name)  # Determines if the object has the given attribute

isinstance(object, class)  # Determines if the object is an instance of the class

issubclass(A, B)  # Determines if A is a subclass of B

random.choice(sequence)  # Chooses a random element from a nonempty sequence

settattr(object, name, value)  # Sets the given attribute of the object to value

type(object)  # Return the type of the object

===================

warnings.filterwarnings(action, category=Warning, ...)  # Used to filter out warnings
warnings.warn(message, category=None)  # Used to issue warnings

===================

iter(obj)  # Extracts an iterator from an iterable object

next(it)  # Advances an iterator and returns its next element

property(fget, fset, fdel, doc)  # Returns a property; all arguments are optional

super(class, obj)  # Return a bound instance of class's superclass

===================

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

===================

dir(obj)  # Retrurns an alphabeized list of attribute names.

help(obj)  # Provides interacitve help or help about a specific object.

imp.reload(module)  # Returns a reloaded version of a module that has already been imported.

===================

