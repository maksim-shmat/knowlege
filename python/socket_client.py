"""Socket client for socket server."""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 9999))
message = s.recv(1024)
s.close()
print(message.decode('ascii'))

#1 A minimal client

import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
s.connect((host, port))
print(s.recv(1024))  # recv == receive
