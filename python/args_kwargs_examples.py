""" Methods Arguments: Default, optional, *args, **kwargs."""

###### Python method definition and call syntax with * and **

def address(city,state,country):
    print(city)
    print(state)
    print(country)

address('San Diego','CA','US')
address('Vancouver','BC','US')

us_address = ('San Diego','CA','US')
address(*us_address)

canada_address = {'country':'US','city':'San Diego','state':'CA'}
address(**canada_address)

###### Python method optional arguments

def address_with_default(city,state,country='US'):
    print(city)
    print(state)
    print(country)

address_with_default('San Diego','CA')
address_with_default('Vancouver','BC','CA')
address_with_default(**{'state':'CA','city':'San Diego'})

##### Python method positional argument

def vowels(*args):
    print("*args is %s" % type(args))
    print("Arguments %s " % ', '.join(args))

vowels('a')
vowels('a','e')
vowels('a','e','i')
vowels('a','e','i','o')
vowels('a','e','i','o','u')

###### Python method with standard and positional argument

def address_with_zipcode(zipcode, *args):
    print(zipcode)
    print("*args is %s" % type(args))
    print("Arguments %s " % ', '.join(args))

address_with_zipcode(92101,'100 Park Boulevard','San Diego','CA','US')
address_with_zipcode('V6B 4Y8','777 Pacific Boulevard','Vancouver','BC','CA')

###### Python method with keyword argument

def address_catcher(**kwargs):
    print("**kwargs is %s" % type(kwargs))
    print("Keyword arguments %s " % ', '.join(['%s = %s' % (k,v) for k,v in kwargs.items()]))

address_catcher(zipcode=92101,street='100 Park Boulevard',city='San Diego',state='CA',country='US')
address_catcher(postalcode='V6b 4Y8',street='777 Pacific Boulevard',city='Vancouver',province='BC',country='CA')

######
