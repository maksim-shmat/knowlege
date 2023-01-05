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
