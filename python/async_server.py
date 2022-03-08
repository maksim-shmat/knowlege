"""async about."""

#A minimal server pogram.

from asyncore import dispatcher
import asyncore

class ChatServer(dispatcher): pass
s = ChatServer()
asyncore.loop()

#2 A server that accepts connections

from asyncore import dispatcher
import socket, asyncore

class ChatServer(dispatcher):
    def handle_accept(self):
        conn, addr = self.accept()
        print('Connection attempt from ', addr[0])

s = ChatServer()
s.create_socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 5005))
s.listen(5)
asyncore.loop()

#3 The basic server with some cleanups

from asyncore import dispatcher
import socket, asyncore
PORT = 5005

class ChatServer(dispatcher):
    def __init__(self, port):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INIT, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)

    def handle_accept(self):
        conn, addr = self.accept()
        print('Connection attempt from', addr[0])

if __name__ == '__main__':
    try: asyncore.loop()
    except KeyboardInterrupt: pass

#4 Server Program with ChatSession Class

from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore

PORT = 5005

class ChatSession(async_chat):
    def __init__(self, sock):
        async_chat.init(self, sock)
        self.set_terminator(''\r\n'')  # or ('\r\n') ?
        self.data = []

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        line = ''.join(self.data)
        self.data = []
        # Do something with the line...
        print(line)


class ChatServer(dispatcher):
    def __init__(self, port): dispatcher.init(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.sessions = []

    def handle_accept(self):
        conn, addr = self.accept()
        self.sessions.append(CharSession(conn))

if __name__ == '__main__':
    s = ChatServer(PORT)
    try: asyncore.loop()
    except KeyboardInterrupt: print()

#5
