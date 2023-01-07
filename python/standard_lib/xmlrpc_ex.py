"""xmlrpc about.

XML-RPC (Extensible Markup Language Remote Procedure Call"""

#1 xmlrpc server

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import Binary
import datetime

'''
class EcampleService:

    def ping(self):
        """Simple function for check connection."""
        return True

    def now(self):
        """Return currently data and time of server."""
        return datetime.datetime.now()

    def show_type(self, arg):
        """Get arg and return tuple."""
        return (str(arg), str(type(arg)), arg)

    def raises_exception(self, msg):
        raise RuntimeError(msg)

    def send_back_binary(self, bin):
        """Get one binary arg."""
        data = bin.dat
        print('send_back_binary({!r})'.format(data))
        response = Binary(data)
        return response
'''

#2 xmlrpc ServerProxy encoding

import xmlrpc.client

'''
server = xmlrpc.client.ServerProxy('http://localhost:9000',
                                   encoding='ISO-8859-1')
print('Ping:', server.ping())
'''

#3 xmlrpc ServerProxy allow none

import xmlrpc.client

'''
server = xmlrpc.client.ServerProxy('http://localhost:9000',
                                   allow_none=False)
try:
    server.show_type(None)
except TypeError as err:
    print('ERROR:', err)

server = xmlrpc.client.ServerProxy('http://localhost:9000',
                                   allow_none=True)
print('Allowed:', server.show_type(None))
'''

#4 xmlrpc type nested

import xmlrpc.client
import datetime
import pprint

'''
server = xmlrpc.client.ServerProxy('http://localhost:9000')

data = {
        'boolean': True,
        'integer': 1,
        'floating-point number': 2.5,
        'string': 'some text',
        'datetime': datetime.datetime.now(),
        'array1': ['a', 'list'],
        'array2': ('a', 'tuple'),
        'structure': {'a': 'dictionary'},
}
arg = []
for i in range(3):
    d = {}
    d.update(data)
    d['integer'] = i
    arg.append(d)

print('Before:')
pprint.pprint(arg, width=40)

print('\nAfter:')
pprint.pprint(server.show_type(arg)[-1], width=40)
'''

#5 xmlrpc ServerProxy use datetime

import xmlrpc.client

'''
server = xmlrpc.client.ServerProxy('http://localhost:9000',
                                   use_datetime=True)
now = server.now()
print('With:', now type(now), now.__class__.__name__)

server = xmlrpc.client.ServerProxy('http://localhost:9000',
                                   use_datetime=False)
now = server.now()
print('Without:', now, type(now), now.__class__.__name__)
'''

#6 xmlrpc types object

import xmlrpc.client
import pprint

'''
class MyObj:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return 'MyObj({!r}, {!r})'.format(self.a, self.b)

server = xmlrpc.client.ServerProxy('http://localhost:9000')

o = MyObj(1, 'b goes here')
print('o:', o)
pprint.pprint(server.show_type(o))

o2 = MyObj(2, o)
print('\no2:', o2)
pprint.pprint(server.show_type(o2))
'''

#7 Send data with pickle, but it NOT SAFE in net

import xmlrpc.client
import pickle
import pprint

'''
class MyObj:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return 'MyObj({!r}, {!r})'.format(self.a, self.b)

server = xmlrpc.client.ServerProxy('http://localhost:9000')

o = MyObj(1, 'b goes here')
print('Local:', id(o))
print(o)

print('\nAs object:')
pprint.pprint(server.show_type(o))

p = pickle.dumps(o)
b = xmlrpc.client.Binary(p)
r = server.send_back_binary(b)

o2 = pickle.dumps(o)
b = xmlrpc.client.Binary(p)
r = server.send_back_binary(b)

o2 = pickle.loads(r.data)
print('\nFrom pickle:', id(o2))
pprint.pprint(o2)
'''

#8 xmlrpc MultiCall exception

import xmlrpc.client

'''
server = xmlrpc.client.ServerProxy('http://localhost:9000')

multicall = xmlrpc.client.MultiCall(server)
multicall.ping()
multicall.show_type(1)
multicall.raises_exception('Next-to_last call stops execution')
multicall.show_type('string')

try:
    for i, r in enumerate(multicall()):
        print(i, r)
except xmlrpc.client.Fault as err:
    print('ERROR:', err)
'''

#9 xmlrpc function client
#1window $ python3 xmlrpc_function.py  # start server from first code above
#2window $ python3 xmlrpc_function_client.py

import xmlrpc.client

'''
proxy = xmlrpc.client.ServerProxy('http://localhost:9000')
print(proxy.list_contents('/tmp'))
'''

#10 xmlrpc dotted name

from xmlrpc.server import SimpleXMLRPCServer
import os

'''
server = SimpleXMLRPCServer(('localhost', 9000), allow_none=True)

server.register_function(os.listdir, 'dir.list')
server.register_function(os.mkdir, 'dir.create')
server.register_function(os.rmdir, 'dir.remove')

try:
    print('Use CTRL-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
'''

#11 xmlrpc dotted name client.  for #10

import xmlrpc.client

'''
proxy = xmlrpc.client.ServerProxy('http://localhost:9000')
print('BEFORE        :', 'EXAMPLE' in proxy.dir.list('/tmp'))
print('CREATE        :', proxy.dir.create('/tmp/EXAMPLE'))
print('SHOULD EXIST  :', 'EXAMPLE' in proxy.dir.list('/tmp'))
print('REMOVE        :', proxy.dir.remove('/tmp/EXAMPLE'))
print('AFTER         :', 'EXAMPLE' in proxy.dir.list('/tmp'))
'''

#12 xmlrpc instance

from xmlrpc.server import SimpleXMLRPCServer  # that's simple server from above
import os
import inspect

'''
server = SimpleXMLRPCServer(
        ('localhost', 9000),
        logRequests=True,
)


class DirectoryService:
    def list(self, dir_name):
        return os.listdir(dir_name)

server.register_instance(DirectoryService())

try:
    print('Use CTRL-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
'''

#13 xmlrpc instance client

import xmlrpc.client

'''
proxy = xmlrpc.client.ServerProxy('http://localhost:9000')
print(proxy.list('/tmp'))
'''

#14 xmlrpc instance dotted names

from xmlrpc.server import SimpleXMLRPCServer
import os
import inspect

'''
server = SimpleXMLRPCServer(
        ('localhost', 9000),
        logRequests=True,
)

def expose(f):
    """Decorator for set flag of function."""
    f.exposed = True
    return f

def is_exposed(f):
    """Check function."""
    return getattr(f, 'exposed', False)


class MyService:
    PREFIX = 'prefix'

    def _dispatch(self, method, params):
        # Remove prefix from method name
        if not method.startswith(self.PREFIX + '.'):
            raise Exception(
                    'method "{}" is not supported'.format(method)
            )
        method_name = method.partition('.')[2]
        func = getattr(self, method_name)
        if not is_exposed(func):
            raise Exception(
                    'method "{}" is not supported'.format(method)
            )
        method_name = method.partition('.')[2]
        func = getattr(self, method_name)
        if not is_exposed(func):
            raise Exception(
                    'method "{}" is not supported'.format(method)
            )
        return func(*params)

    @expose
    def public(self):
        return 'This is public'

    def private(self):
        return 'This is private'

server.register_instance(MyService())

try:
    print('Use CTRL-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
'''

#add xmlrpc instance dotted names client

import  xmlrpc.client

'''
proxy = xmlrpc.client.ServerProxy('http://localhost:9000')
print(proxy.dir.list('/tmp'))
'''

#15 xmlrpc introspection

from xmlrpc.server import (SimpleXMLRPCServer,
                           list_public_methods)
import os
import inspect

'''
server = SimpleXMLRPCServer(
        ('localhost', 9000),
        logRequests=True,
)
server.register_introspection_functions()


class DirectoryService:

    def _listMethods(self):
        return list_public_methods(self)

    def _methodHelp(self, method):
        f = getattr(self, method)
        return inspect.getdoc(f)

    def list(self, dir_name):
        """list(dir_name) => [<filenames>]
        Returns a list containing the contents of
        the named directory.
        """
        return os.listdir(dir_name)

server.register_instance(DirectoryService())

try:
    print('Use CTRL-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
'''

#add xmlrpc instance with prefix

from xmlrpc.server import SimpleXMLRPCServer
import os
import inspect

'''
server = SimpleXMLRPCServer(
    ('localhost', 9000),
    logRequest=True,
)

def expose(f):
    f.exposed = True
    return f

def is_exposed(f):
    return getattr(f, 'exposed', False)


class MyService:
    PREFIX = 'prefix'

    def _dispatch(self, method, params):
        if not method.startswith(self.PREFIX + '.'):
            raise Exception(
                'method "{}" is not supported'.format(method)
            )
        method_name = method.partition('.')[2]
        func = getattr(self, method_name)
        if not is_exposed(func):
            raise Exception(
                'method "{}" is not supported'.format(method)
            )
        return func(*params)

    @expose
    def public(self):
        return 'This is public'

    def private(self):
        return 'This is private'

server.register_instance(MyService())

try:
    print('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
'''

#add xmlrpc instance with prefix client

import xmlrpc.client
'''
proxy = xmlrpc.client.ServerProxy('http://localhost:9000')
print('public():', proxy.prefix.public())
try:
    print('private():', proxy.prefix.public())
except Exception as err:
    print('\nERROR:', err)
try:
    print('public() without prefix:', proxy.public())
except Exception as err:
    print('\nERROR:', err)
'''

#16 xmlrpc introspectiono

from xmlrpc.server import (SimpleXMLRPCServer,
                           list_public_methods)
import os
import inspect

'''
server = SimpleXMLRPCServer(
        ('localhost', 9000),
        logRequests=True,
)
server.register_introspection_functions()


class DirectoryService:

    def _listMethods(self):
        return list_public_methods(self)

    def _methodHelp(self, method):
        f = getattr(self, method)
        return inspect.getdoc(f)

    def list(self, dir_name):
        """list(dir_name) => [<filenames>]
        Returns a list containing the contents of
        the named directory.
        """
        return os.listdir(dir_name)

server.register_instance(DirectoryService())

try:
    print('Use CTRL-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
'''

#17 xmlrpc introspection client

import xmlrpc.client

'''
proxy = xmlrpc.client.ServerProxy('http://localhost:9000')
for method_name in proxy.system.listMethods():
    print('=' * 60)
    print(method_name)
    print('-' * 60)
    print(proxy.system.methodHelp(method_name))
    print()
'''
