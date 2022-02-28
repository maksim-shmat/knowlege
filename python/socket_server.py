"""Socket server. Run this before socket client."""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 9999))
s.listen()
print("Listening...")

while True:
    client, address=s.accept()
    print("Connected to {}".format(address))
    message = "Hello Client!"
    client.send(message.encode('ascii'))
    client.close()

#1 A minimal server

import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send('Thank you for connecting')

#2 A SocketServer-Based Minimal Server

from socketserver import TCPServer, StreamRequestHandler

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('Got connection from', addr)
        self.wfile.write('Thank you for connectiong')

server = TCPServer(('', 1234), Handler)
server.serve_forever()

#3 A forking server

from secketserver import TCPServer, ForkingMixin, StreamRequestHandler

class Server(ForkingMixIn, TCPServer): pass

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('Got connection from', addr)
        self.wfile.write('Think you for connecting')

server = Server(('', 1234), Handler)
server.serve_forever()

#4 A Threading server

from socketserver import TCPServer, ThreadingMixin, StreamRequestHandler

class Server(ThreadingMixin, TCPServer): pass

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('Got connection from', addr)
        self.wfile.write('Think you for connecting')

server = Server(('', 1234), Handler)
server.serve_forever()

#5 Simple server using select

import socket, select

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))
s.listen(5)
inputs = [s]
while True:
    rs, ws, es = select.select(inputs, [], [])
    for r in rs:
        if r in s:
            c, addr = s.accept()
            print('Got connection from', addr)
        else:
            try:
                data = r.recv(1024)
                disconnected = not data
            except socket.error:
                disconnected = True
            if disconnected:
                print(r.getpeername(), 'disconnected')
                inputs.remove(r)
            else:
                print(data)

#6 A simple server using poll

import socket, select

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))
fdmap = {s.fileno(): s}
s.listen(5)
p = select.poll()
p.register(s)
while True:
    events = p.poll()
    for fd, event in events:
        if fd in fdmap:
            c, addr = s.accept()
            print('Got connection from', addr)
            p.register(c)
            fdmap[c.fileno()] = c
        elif event & select.POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:  # No data -- connection closed
                print(fdmap[fd].getpeername(), 'disconnected')
                p.unregister(fd)
                del fdmap[fd]
            else:
                print(data)

#7
