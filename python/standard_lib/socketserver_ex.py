"""socketserver about."""

#1 socketserver echo

'''
import logging
import sys
import socketserver


logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    )

class EchoRequestHandler(socketserver.BaseRequestHandler):
    
    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger('EchoRequestHandler')
        self.logger.debug('__init__')
        socketserver.BaseRequestHandler.__init__(self, request,
                                                 client_address,
                                                 server)
        return

    def setup(self):
        self.logger.debug('setup')
        return socketserver.BaseRequestHandler.setup(self)

    def handle(self):
        self.logger.debug('handle')

        # echo message for client
        data = self.request.recv(1024)
        self.logger.debug('recv()->"%s"', data)
        self.request.send(data)
        return

    def finish(self):
        self.logger.debug('finish')
        return socketserver.BaseRequestHandler.finish(self)


class EchoServer(socketserver.TCPServer):

    def __init__(self, server_address,
                 handler_class=EchoRequestHandler,
                 ):
        self.logger = logging.getLogger('EchoServer')
        self.logger.debug('__init__')
        socketserver.TCPServer.__init__(self, server_address,
                                        handler_class)
        return

    def server_activate(self):
        self.logger.debug('server_activate')
        socketserver.TCPServer.server_activate(self)
        return

    def serve_forever(self, poll_interval=0.5):
        self.logger.debug('waiting for request')
        self.logger.info(
                'Handling requests, press <Ctr-C> to quit'
        )
        socketserver.TCPServer.serve_forever(self, poll_interval)
        return

    def handle_request(self):
        self.logger.debug('handle_request')
        return socketserver.TCPServer.handle_request(self)

    def verify_request(self, request, client_address):
        self.logger.debug('verify_request(%s, %s)',
                          request, client_address)
        return socketserver.TCPServer.verify_request(
                self, request, client_address,
        )

    def process_request(self, request, clent_address):
        self.logger.debug('process_request(%s, %s)',
                          request, client_address)
        return socketserver.TCPServer.process_request(
                self, request, client_address,
        )

    def server_close(self):
        self.logger.debug('server_close')
        return socketserver.TCPServer.server_close(self)

    def finish_request(self, request, client_address):
        self.logger.debug('finish_request(%s, %s)',
                          request, client_address)
        return socketserver.TCPServer.finish_request(
                self, request, client_address,
        )

    def close_request(self, request_address):
        self.logger.debug('close_request(%s)', request_address)
        return socketserver.TCPServer.close_request(
                self, request_address,
        )

    def shutdown(self):
        self.logger.debug('shutdown()')
        return socketserver.TCPServer.shutdown(self)

if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost', 0)  # the core and port, or against 0 port-number
    server = EchoServer(address, EchoRequestHandler)
    ip, port = server.server_address  # check port

    # Start server in a thread
    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)  # work in background
    t.start()

    logger = logging.getLogger('client')
    logger.info('Server on %s:%s', ip, port)

    # Connect to the server
    logger.debug('creating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.debug('connecting to server')
    s.connect((ip, port))

    # Send data
    message = 'Hello, world'.encode()

    logger.debug('sending data: %r', message)
    len_sent = s.send(message)

    # Get answer
    logger.debug('waiting for response')
    response = s.recv(len_sent)
    logger.debug('response from server: %r', response)

    # Clear resources
    server.shutdown()
    logger.debug('closing socket')
    s.close()
    logger.debug('done')
    server.socket.close()
'''

#2 socketserver echo simple

import socketserver

'''
class EchoRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # Echo message for client
        data = self.request.recv(1024)
        self.request.send(data)
        return


if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost', 0)
    server = socketserver.TCPServer(address, EchoRequestHandler)
    ip, port = server.server_address

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    message = 'Hello, world'.encode()
    print('Sending : {!r}'.format(message))
    len_sent = s.send(message)

    response = s.recv(len_sent)
    print('Received: {!r}'.format(response))

    server.shutdown()
    s.close()
    server.socket.close()
'''
#3 socketserver threaded

import threading
import socketserver

'''
class ThreadedEchoRequestHandler(
        socketserver.BaseRequestHandler,
):

    def handle(self):
        # Echo message for client
        data = self.request.recv(1024)
        cur_thread = threading.currentThread()
        response = b'%s: %s' % (cur_thread.getName().encode(),
                                data)
        self.request.send(response)
        return


class ThreadedEchoServer(socketserver.ThreadingMixIn,
                         socketserver.TCPServer,
                         ):
    pass


if __name__ == '__main__':
    import socket

    address = ('localhost', 0)  # 0 is random port, or write oneself
    server = ThreadedEchoServer(address,
                                ThreadedEchoRequestHandler)
    ip, port = server.server_address

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()
    print('Server loop running in thread:', t.getName())

    # connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Send data
    message = b'Hello, world'
    print('Sending : {!r}'.format(message))
    len_sent = s.send(message)

    # Get answer
    response = s.recv(1024)
    print('Received: {!r}'.format(response))

    # Clear resources
    server.shutdown()
    s.close()
    server.socket.close()

RESULTS:
<stdin>:222: DeprecationWarning: setDaemon() is deprecated, set the daemon attribute instead
<stdin>:224: DeprecationWarning: getName() is deprecated, get the name attribute instead
Server loop running in thread: Thread-1 (serve_forever)
Sending : b'Hello, world'
<stdin>:200: DeprecationWarning: currentThread() is deprecated, use current_thread() instead
<stdin>:201: DeprecationWarning: getName() is deprecated, get the name attribute instead
Received: b'Thread-2 (process_request_thread): Hello, world'
'''

#4 socketserver forking

import os
import socketserver

'''
class ForkingEchoRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # Echo message for client
        data = self.request.recv(1024)
        cur_pid = os.getpid()
        response = b'%d: %s' % (cur_pid, data)
        self.request.send(response)
        return


class ForkingEchoServer(socketserver.ForkingMixIn,
                        socketserver.TCPServer,
                        ):
    pass


if __name__ == '__main__':
    import socket
    import threading


    address = ('localhost', 0)
    server = ForkingEchoServer(address,
                               ForkingEchoRequestHandler)
    ip, port = server.server_address

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()
    print('Server loop running in process:', os.getpid())

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    message = 'Hello, world'.encode()
    print('Sending : {!r}'.format(message))
    len_sent = s.send(message)

    response = s.recv(1024)
    print('Received: {!r}'.format(response))

    server.shutdown()
    s.close()
    server.socket.close()

RESULTS:
<stdin>:288: DeprecationWarning: setDaemon() is deprecated, set the daemon attribute instead
Server loop running in process: 628423
Sending : b'Hello, world'
Received: b'628425: Hello, world'
'''
