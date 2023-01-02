"""http.server about."""

#1 http server GET
# for check server:
# In another window: $ curl -v -i http://127.0.0.1:8080/?foo=bar

from http.server import BaseHTTPRequestHandler
from urllib import parse

'''
class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = parse.urlparse(self.path)
        message_parts = [
                'CLIENT VALUES:',
                'client_address={} ({})'.format(
                    self.client_address,
                    self.address_string()),
                'command={}'.format(self.command),
                'path={}'.format(self.path),
                'real path={}'.format(parsed_path.path),
                'query={}'.format(parsed_path.query),
                'request_version={}'.format(self.request_version),
                '',
                'SERVER VALUES:',
                'server_version={}'.format(self.server_version),
                'sys_version={}'.format(self.sys_version),
                'protocol_version={}'.format(self.protocol_version),
                '',
                'HEADERS RECEIVED:',
        ]
        for name, value in sorted(self.headers.items()):
            message_parts.append(
                    '{}={}'.format(name, value.rstrip())
            )
        message_parts.append('')
        message = '\r\n'.join(message_parts)
        self.send_response(200)
        self.send_header('Content_Type',
                         'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), GetHandler)
    print('Starting server, use <CTRL-C> to stop')
    server.serve_forever()
'''

#2  http server POST
# type in another window: $ curl -v http://127.0.0.1:8080/ -F name-dhellhound -F foo=bar -F datafile=@http_server_GET.py

import cgi
from http.server import BaseHTTPRequestHandler
import io

'''
class PostHandler(BaseHTTPRequestHandler):

    def do_POST(serlf):
        # Analise downloaded data
        form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={
                    'REQUEST_METHOD': 'POST',
                    'CONTENT_TYPE': self.headers['Content-Type'],
                }
        )

        # Start answering
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()

        out = io.TextIOWrapper(
                self.wfile,
                encoding='utf-8',
                line_fuffering=False,
                write_through=True,
        )

        out.write('Client: {}\n'.format(self.client_address))
        out.write('User-agent: {}\n'.format(
            self.headers['user-agent']))
        out.write('Path: {}\n'.format(self.path))
        out.write('Form data:\n')

        # Sending backward data with form
        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                # It field contain downloaded file
                file_data = field_item.file.read()
                file_len = len(file_data)
                del file_data
                out.write(
                        '\tUpload {} as {!r} ({} bytes)\n'.format(
                            field, field_item.filename, file_len)
                )
            else:
                # Common form value
                out.write('\t{}={}\n'.format(
                    field, form[field].value))

        # Off TextIOWrapper out of base buffer, for safe socket connection
        out.detach()

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), PostHandler)
    print('Starting server, use <CTRL-C> to stop')
    server.serve_forever()
'''

#3 http server threads

from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading

'''
class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()
        message = threading.currentThread().getName()
        self.wfile.write(message.encode('utf-8'))
        self.wfile.write(b'\n')


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in different thread."""


if __name__ == '__main__':
    server = ThreadedHTTPServer(('localhost', 8080), Handler)
    print('Starting server, use <CTRL-C> to stop')
    server.serve_forever()

RESULTS:
Starting server, use <CTRL-C> to stop
^[[O127.0.0.1 - - [02/Jan/2023 23:36:20] "GET / HTTP/1.1" 200 -
<stdin>:133: DeprecationWarning: currentThread() is deprecated, use current_thread() instead
<stdin>:133: DeprecationWarning: getName() is deprecated, get the name attribute instead
127.0.0.1 - - [02/Jan/2023 23:36:23] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [02/Jan/2023 23:36:28] "GET / HTTP/1.1" 200 -

IN ANOTHER WINDOW:
jack@Cesar:~/django2/knowlege/unix$ curl http://127.0.0.1:8080/
Thread-1 (process_request_thread)
jack@Cesar:~/django2/knowlege/unix$ curl http://127.0.0.1:8080/
Thread-2 (process_request_thread)
jack@Cesar:~/django2/knowlege/unix$ curl http://127.0.0.1:8080/
Thread-3 (process_request_thread)
'''

#4 http server errors

from http.server import BaseHTTPRequestHandler

'''
class ErrorHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_error(404)

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), ErrorHandler)
    print('Starting server, use <CTRL-C> to stop')
    server.serve_forever()

RESULTS:
# in another window:
jack@Cesar:~/django2/knowlege/unix$ curl http://127.0.0.1:8080/
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
        "http://www.w3.org/TR/html4/strict.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        <title>Error response</title>
    </head>
    <body>
        <h1>Error response</h1>
        <p>Error code: 404</p>
        <p>Message: Not Found.</p>
        <p>Error code explanation: 404 - Nothing matches the given URI.</p>
    </body>
</html>
'''

#5 http server send header

from http.server import BaseHTTPRequestHandler
import time

'''
class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header(
                'Content-Type',
                'text/plain; charset=utf-8',
        )
        self.send_header(
                'Last-Modified',
                self.date_time_string(time.time())
        )
        self.end_headers()
        self.wfile.write('Response body\n'.encode('utf-8'))

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), GetHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()

RESULTS:
# jack@Cesar:~/django2/knowlege/unix$ curl -i http://127.0.0.1:8080/
HTTP/1.0 200 OK
Server: BaseHTTP/0.6 Python/3.10.6
Date: Mon, 02 Jan 2023 20:57:16 GMT
Content-Type: text/plain; charset=utf-8
Last-Modified: Mon, 02 Jan 2023 20:57:16 GMT

Response body
'''

#6 start http.server built-in server for local filesystem
'''
# for vim ->             :!python3 -m http.serve 8080  # start server
# in another window ->   $ curl -I http://127.0.0.1:8080/index.rst
RESULTS:
jack@Cesar:~/django2/knowlege/unix$ curl -I http://127.0.0.1/index.rst
HTTP/1.1 404 Not Found
Server: nginx/1.18.0 (Ubuntu)
Date: Mon, 02 Jan 2023 21:04:18 GMT
Content-Type: text/html
Content-Length: 162
Connection: keep-alive
'''
