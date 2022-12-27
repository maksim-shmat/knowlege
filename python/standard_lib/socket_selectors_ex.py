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
#2 selectors echo client

import selectors
import socket

'''
mysel = selectors.DefaultSelector()
keep_running = True
outgoing = [
        b'It will be repeated.',
        b'This is the message.',
]
bytes_sent = 0
bytes_received = 0

# connect is operation of blocked, and then need call setblocking()
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)
sock.setblocking(False)

# Set selector for check socket for send and check read data
mysel.register(
        sock,
        selectors.EVENT_READ | selectors.EVENT_WRITE,
)

while keep_running:
    print('waiting for I/O')
    for key, mask in mysel.select(timeout=1):
        connection = key.fileobj
        client_address = connection.getpeername()
        print('client({})'.format(client_address))

        if mask & selectors.EVENT_READ:
            print('ready to read')
            data = connection.recv(1024)
            if data:
                # Client's socet for read get data
                print('received {!r}'.format(data))
                bytes_received += len(data)

            # Stop after empty result or double results
            keep_running = not (
                    data or
                    (bytes_received and
                        (bytes_received == bytes_sent))
            )

        if mask & selectors.EVENT_WRITE:
            print('ready to write')
            if not outgoing:
                # If not messages change registration and set read only
                print('switching to read_only')
                myself.modify(sock, selectors.EVENT_READ)
            else:
                # Send next message
                next_msg = outgoing.pop()
                print('sending {!r}'.format(next_msg))
                sock.sendall(next_msg)
                bytes_sent += len(next_msg)

print('shutting down')
mysel.unregister(connection)
connection.close()
mysel.close()
'''

#3 selectors is high level, and select low level, high level prefer for ease
# select echo server for check both connections

import select
import socket
import sys
import queue


# Create socket TCP/IP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

# Bind socket to port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address),
        file=sys.stderr)
server.bind(server_address)

# Listen connections
server.listen(5)

# Sockets for read data
inputs = [server]

# Sockets for write data
outputs = []

# Queue for messages (socket:Queue)
message_queues = {}

while inputs:
    # wait while socket get ready
    print('waiting for the next event', file=sys.stderr)
    readable, writable, exceptional = select.select(inputs,
                                                    outputs,
                                                    inputs)
    # get data
    for s in readable:

        if s is server:
            # Socket for read ready for connection
            connection, client_address = s.accept()
            print('connection from', client_address,
                    file=sys.stderr)
            connection.setblocking(0)
            inputs.append(connection)

            # Put queue with data for connection
            message_queues[connection] = queue.Queue()

        else:
            data = s.recv(1024)
            if data:
                print('received {!r} from {}'.format(
                    data, s.getpeername()), file=sys.stderr,
                )
                message_queues[s].put(data)
                # add chanel for send answer
                if s not in outputs:
                    outputs.append(s)
                else:
                    print('closing', client_address,
                            file=sys.stderr)
                    # stop listening
                    if s in outputs:
                        outputs.remove(s)
                        inputs.remove(s)
                        s.close()
                        
                        # del queue of messages
                        del message_queue[s]

    for s in writable:
