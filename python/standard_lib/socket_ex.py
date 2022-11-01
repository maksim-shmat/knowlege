"""socet about."""

#1 socket file

import sys
import socketserver


class Echo(socketserver.BaseRequestHandler):

    def handle(self):
        """Get bytes and return it to client.
        Decode data not need, then it not use there.
        """
        data = self.request.recv(1024)
        self.request.send(data)


class PassThrough:

    def __init__(self, other):
        self.other = other

    def write(self, data):
        print('Writing:', repr(data))
        return self.other.write(data)

    def read(self, size=-1):
        print('Reading:', end=' ')
        data = self.other.read(size)
        print(repr(data))
        return data

    def flush(self):
        return self.other.flush()

    def close(self):
        return self.other.close()

if __name__ == '__main__':
    import codecs
    import socket
    import threading

    address = ('localhost', 0)  # The core check port
    server = socketserver.TCPServer(address, Echo)
    ip, port = server.server_address  # How port is checked?

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)  # make thread to the daemon thread
    t.start()

    # Connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Wrapping socket from read/write object
    read_file = s.makefile('rb')
    incoming = codecs.getreader('utf-8')(PassThrough(read_file))
    write_file = s.makefile('wb')
    outgoing = codecs.getwriter('utf-8')(PassThrough(write_file))

    # Send data
    # Not encoded first!
    text = 'français'
    print('Sending:', repr(text))
    outgoing.write(text)
    outgoing.flush()

    # get an ansver
    response = incoming.read()
    print('Received:', repr(response))

    # Empty source
    s.close()
    server.socket.close()

'''RESULTS:
<stdin>:50: DeprecationWarning: setDaemon() is deprecated, set the daemon attribute instead
Sending: 'français'
Writing: b'fran\xc3\xa7ais'
Reading: b'fran\xc3\xa7ais'
Reading: b''
Received: 'français'
'''
