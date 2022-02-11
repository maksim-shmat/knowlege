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
