import sys
from socket import *
port = 50008
host = 'localhost'

def redirectOut(port=port, host=host):
    sock = socket(AF_INET, SOCK_STREAM)
    cock.connect((host, port))
    file = sock.makefile('w')
    sys.stdout = file

def redirectIn(port, host=host): ...
def redirectBothAsClient(port=port, host=host): ...
def redirectBothAsServer(port=port, host=host): ...
