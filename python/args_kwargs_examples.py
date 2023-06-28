""" Methods Arguments: Default, optional, *args, **kwargs."""

# * - is a tuple
# ** - is a dict

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

###### Python method with standard, positional and keyword argument

def address_full(country,*args,**kwargs):
    print(country)
    print("*args is %s" % type(args))
    print("Arguments %s " % ', '.join(args))
    print("**kwargs is %s" % type(kwargs))
    print("Keyword arguments %s " % ', '.join(['%s = %s' % (k,v) for k,v in kwargs.items()]))

address_full('US','100 Park Boulevard', 'San Diego', state='CA',zipcode=92101)
address_full('CA','777 Pacific Boulevard','Vancouver',province='BC',postalcode='V6B 4Y8')

#1 Just simple example

def print_params(x, y, z=3, *pospar, **keypar):
    print(x, y, z)
    print(pospar)
    print(keypar)

print_params(1, 2, 3, 5, 6, 7, foo=1, bar=2)
# 1 2 3
# (5, 6, 7)
# {'foo':1,'bar':2}

print_params(1, 2)
# 1 2 3
()
{}

#2 powersum

def powersum(power, *args):
    '''Return sum args, in power.'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total

>>> powersum(2, 3, 4)  # 3*3=9, 4*4=16; 9+16=25
25
>>> powersum(2, 10)
100

#3 Args convenient

host_info = ('www.python.org', 80, '/')  # tuple

def check_web_server(host, port, path):
    pass

# call function
check_web_server(host_info[0], host_info[1], host_info[2])  # Not good

# use args
check_web_server(*host_info)  # That's my girl!

#4 Kwargs convenient

host_info = {'host': 'www.python.org', 'port': 80, 'path': '/'}  # dict

def check_web_server(host, port, path):
    pass

# call function
check_web_server(**host_info)  # indentical check_web_server(host='www.python.org, port=80, path='/')

#5 Count daily sales

def daily_sales_total(*all_sales):  # * - it is for all calls
    total = 0.0
    for each_sale in all_sales:
        total += float(each_sale)
    return total

# call function, all calls access

daily_sales_total()
daily_sales_total(10.00)
daily_sales_total(5.00, 1.50, '123.79')

#6 connect to a db

def connect(**options):
    conn_params = {
            'host': options.get('host', '127.0.0.1'),
            'port': options.get('port', 5432),
            'user': options.get('user', ''),
            'pwd': options.get('pwd', ''),
    }
    print(conn_params)
    # we then connect to the db (connected out)
    # db.connect(**conn_params)

connect()
connect(host='127.0.0.1', port=5433)
connect(port=5431, user='herus', pwd='generallissimus')

# RESULTS:
# {'host': 127.0.0.1', 'port': 5432, 'user': '', 'pwd': ''}
# {'host': 127.0.0.1', 'port': 5433, 'user': '', 'pwd': ''}
# {'host': 127.0.0.1', 'port': 5431, 'user': 'herus', 'pwd': 'generallissimus'}

#7
