"""Make port scanner."""

'''
import socket

target = "10.0.0.5"

def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = s.connect((target, port))
        return True
    except:
        return False
    for x in range(1, 501):
        if (portscan(x)):
            print("Port {} is open!".format(x))
        else:
            print("Port {} is closed!".format(x))
'''

#2 Threaded port scanner

import socket
from queue import Queue
import threading

target = "10.0.0.5"

q = Queue()
for x in range(1, 501):
    q.put(x)

def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = s.connect((target, port))
        return True
    except:
        return False

def worker():
    while True:
        port = q.get()
        if portscan(port):
            print("Port {}is open!".format(port))
for x in range(30):
t = threading.Thread(target=worker)
t.start()
