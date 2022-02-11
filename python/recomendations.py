"""How is write programs."""

#1
Write down a description of your problem (what should the program do?).
Underline all the nouns, verbs, and adjectives.

#2
Go through the nouns looking for potential classes.

#3
Go through the verbs. looking for potential methods.

#4
Go through the adjectives, looking for potential attributes.

#5
Allocate methods and attributes to your classes.

=====================
Object-Oriented Design

#1 Gather what belong together.
If a function manipulates a global variable, the two of them might be better off in a class, as an attribute and a method.

#2 Don`t let objects become too intimate.
Methods should mainly be concerned with the attributes of their own instance.
Let other instances manage their own state.

#3 Go easy on the inheritance, especially multiple inheritance.
Inheritance is useful at times but can make things unnecessarily complex in some cases. And multiple inheritance can be very difficult to get right and evenharder to debug.

#4 Keep it simple.
Keep it simple. Keep your methods small. As a rule of thumb, it should be
possible to read (and understand) most of your methods in, say, 30 sec.
For the rest, try to keep them shorter than one page or screen.

======================

