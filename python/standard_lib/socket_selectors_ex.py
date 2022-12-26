"""selectors about."""

#1 selectors echo server

import selectors
import socket

'''
mysel = selectors.DefaultSelector()
keep_running = True


def read(connection, mask):
    """Callback function for read task."""
    global keep_running
    
    client_address = connection.getpeername()
    print('read({})'.format(client_address))
    data = connection.recv(1024)
    if data:
        # socket of client for read keep data
        print('  received {!r}'.format(data))
        connection.sendall(data)
    else:
        # empty result check how close connection
        print('  closing')
        mysel.unregister(connection)
        connection.close()
        # Main cicle is stoped
        keep_running = False


def accept(sock, musk):
    """Callback function for new connections."""
    new_connection, addr = sock.accept()
    print('accept({})'.format(addr))
    new_connection.setblocking(False)
    mysel.register(new_connection, selectors.EVENT_READ, read)

server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(server_address)
server.listen(5)

mysel.register(server, selectors.EVENT_READ, accept)

while keep_running:
    print('waiting for I/O')
    for key, mask in mysel.select(timeout=1):
        callback = key.data
        callback(key.fileobj, mask)

print('shutting down')
mysel.close()
'''
#2
