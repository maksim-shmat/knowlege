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

dir(obj)  # Retrurns an alphabeized list of attribute names.

help(obj)  # Provides interacitve help or help about a specific object.

imp.reload(module)  # Returns a reloaded version of a module that has already been imported.

===================

open(name, ...)  # Opens a file and returns a file object

===================

# urllib about

asynchat  # Additional functionality for asyncore

asyncore  # Asynchronous socket handler

cgi  # Basic CGI support

Cookie  # Cookie object manipulation, mainly for servers

cookielib  # Client-side cookie support

email  # Support for e-mail messages(including MIME)

ftplib  # FTP client module

gopherlib  # Gopher client module

httplib  # HTTP client module

imaplib  # IMAP4 cient module

mailbox  # Reads several mailbox formats

mailcap  # Access to MIME configuration through mailcap files

mhlib  # Access to MH mailboxes

nntplib  # NNTP client module

poplib  # POP client module

robotparser  # Support for parsing web server robot files

Simple XMLRPCServer  # A simple XML-RPC server

smtpd  # SMTP server module

smtplib  # SMTP client module

telnetlib  # Telnet client module

urlparse  # Support for interpreting URLs

xmlrpclib  # Client support for XML-RPC

==================
# urllib and Twisted

urllib.urlopen(url[, data[, proxies]])  # Opens a file-like object from a URL

urllib.urlretrieve(url[, fname[, hook[, data]]])  # Downloads a file from a URL
urllib.quote(string[, save])  # Quotes special URL characters

urllib.quote_plus(string[, safe])  # The same as quote, but quotes spaces as +

urllib.unquote(string)  # The reverse of quote

urllib.urlencode(query[, doseq])  # Encodes mapping for use in CGI queries

select.select(iseq, oseq, eseq[, timeout])  # Finds sockets ready for reading/writing
select.poll()  # Creates a poll object, for polling sockets

reactor.listenTCP(port, factory)  # Twisted function; listen for connections

reactr.run()  # Twisted function; main server loop

===================
# Scrapping with Tidy

handle_starttag(tag, attrs)  # When a start tag is fount, attrs is a sequence
# of (name, value) pairs
handle_startendtag(tag, attrs)  # For empt tags; default handles start and
# end separately.
handle_endtag(tag)   # When and end tag is found

handle_data(data)  # For textual data.

handle_charref(ref)  # For character references of the form &#ref;.

handle_entityref(name)  # For comments; called with only th comment contents.

handle_comment(data)  # For comments; called with only the comment contents.

handle_decl(decl)  # For declarations of the form <!...>.

handle_pi(data)  # For processing instructions.

unknown_decl(data)  # Called when an unknown declaration is read.

====================
#
