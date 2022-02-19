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

#24
