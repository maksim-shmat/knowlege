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
