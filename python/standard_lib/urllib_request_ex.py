"""urllib.request about."""

# need http server

#1 urllib request urlopen

from urllib import request

'''
response = request.urlopen('http://localhost:8080/')
print('RESPONSE:', response)
print('URL     :', response.geturl())


headers = response.info()
print('DATE    :', headers['date'])
print('HEADERS :')
print('---------')
print(headers)

data = response.read().decode('utf-8')
print('LENGTH  :', len(data))
print('DATA    :')
print('---------')
print(data)
'''

#2 urllib request urlopen iterator

from urllib import request

'''
response = request.urlopen('http://localhost:8080/')
for line in response:
    print(line.decode('utf-8').rstrip())
'''

#3 urllib request http get args

from urllib import parse
from urllib import request

'''
query_args = {'q': 'query string', 'foo': 'bar'}
encoded_args = parse.urlencode(query_args)
print('Encoded:', encoded_args)

url = 'http://localhost:8080/?' + encoded_args
print(request.urlopen(url).read().decode('utf-8'))
'''

#4 urllib request urlopen post

from urllib import parse
from urllib import request

'''
query_args = {'q': 'query string', 'foo': 'bar'}
encoded_args = parse.urlencode(query_args).encode('utf-8')
url = 'http://localhost:8080/'
print(request.urlopen(url, encoded_args).read().decode('utf-8'))
'''

#5 urllib request request header

from urllib import request

'''
r = request.Request('http://localhost:8080/')
r.add_header(
        'User-agent',
        'PyMOTW (https://pymotw.com/)',
)

response = request.urlopen(r)
data = response.read().decode('utf-8')
print(data)
'''

#6 urllib request request post

from urllib import parse
from urllib import request

'''
query_args = {'q': 'query string', 'foo': 'bar'}

r = request.Request(
        url='http://localhost:8080/',
        data=parse.urlencode(query_args).encode('utf-8'),
)
print('Request method :', r.get_method())
r.add_header(
        'User-agent',
        'PyMOTW (https://pymotw.com/)',
)

print()
print('OUTGOING DATA:')
print(r.data)

print()
print('SERVER RESPONSE:')
print(request.urlopen(r).read().decode('utf-8'))
'''

#7 urllib request upload files

import io
import mimetypes
from urllib import request
import uuid

'''
class MultiPartForm:
    """Amass data."""

    def __init__(self):
        self.form_fields = []
        self.files = []
        # Use random bytes string with high length for different chunks of MIME-data
        self.boundary = uuid.uuid4().hex.encode('utf-8')
        return

    def get_content_type(self):
        return 'multipart/form-data; boundary={}'.format(
                self.boundary.decode('utf-8'))

    def add_field(self, name, value):
        """Add simple field in form of data."""
        self.form_fields.append((name, value))

    def add_file(self, fieldname, filename, fileHandle,
                 mimetype=None):
        """Add loading file."""
        body = fileHandle.read()
        if mimetype is None:
            mimetype = (
                    mimetypes.guess_type(filename)[0] or
                    'application/octet-stream'
            )
        self.files.append((fieldname, filename, mimetype, body))
        return

    @staticmethod
    def _form_data(name):
        return ('Content-Disposition: form-data; '
                'name="{}"\r\n').format(name).encode('utf-8')

    @staticmethod
    def _attached_file(name, filename):
        return ('Content-Disposition: file; '
                'name="{}"; filename="{}"\r\n').format(
                        name, filename).encode('utf-8')

    @staticmethod
    def _content_type(ct):
        return 'Content-Type: {}\r\n'.format(ct).encode('utf-8')

    def __bytes__(self):
        """Return bytes string, how is form-data with added files."""
        buffer = io.BytesIO()
        boundary = b'--' + self.boundary + b'\r\n'

        # Add form fileds
        for name, value in self.form_fields:
            buffer.write(boundary)
            buffer.write(self._form_data(name))
            buffer.write(b'\r\n')
            buffer.write(value.encode('utf-8'))
            buffer.write(b'\r\n')

        # Add loading files
        for f_name, filename, f_content_type, body in self.files:
            buffer.write(boundary)
            buffer.write(self._attached_file(f_name, filename))
            buffer.write(self._content_type(f_content_type))
            buffer.write(b'\r\n')
            buffer.write(body)
            buffer.write(b'\r\n')

        buffer.write(b'--' + self.boundary +b'--\r\n')
        return buffer.getvalue()

if __name__ == "__main__":
    # Create a form with simple fields
    form = MultiPartForm()
    form.add_field('firstname', 'Doug')
    form.add_field('lastname', 'Hellmann')

    # Add fake file
    form.add_file(
            'biography', 'bio.txt',
            fileHandle=io.BytesIO(b'Python developer and blogger.'))

    # Create request with bytestring for loading data
    data = bytes(form)
    r = request.Request('http://localhost:8080/', data=data)
    r.add_header(
            'User-agen',
            'PyMOTW (https://pymotw.com/)',
    )
    r.add_header('Content-type', form.get_content_type())
    r.add_header('Content-length', len(data))

    print()
    print('OUTGOING DATA:')
    for name, value in r.header_items():
        print('{}: {}'.format(name, value))
    print()
    print(r.data.decode('utf-8'))
    print()
    print('SERVER RESPONSE:')
    print(request.urlopen(r).read().decode('utf-8'))
'''

#8 urllib request nfs handler

import io
import mimetypes
import os
import tempfile
from urllib import request
from urllib import response

'''
class NFSFile:

    def __init__(self, tempdir, filename):
        self.tempdir = tempdir
        self.filename = filename
        with open(os.path.join(tempdir, filename), 'rb') as f:
            self.buffer = io.BytesIO(f.read())

    def read(self, *args):
        return self.buffer.read(*args)

    def readline(self, *args):
        return self.buffer.readline(*args)

    def close(self):
        print('\nNFSFile:')
        print('  unmounting {}'.format(
            os.path.basename(self.tempdir)))
        print('  when {} is closed'.format(
            os.path.basename(self.filename)))


class FauxNFSHandler(request.BaseHandler):

    def __init__(self, tempdir):
        self.tempdir = tempdir
        super().__init__()

    def nfs_open(self, req):
        url = req.full_url
        directory_name, file_name = os.path.split(url)
        server_name = req.host
        print('FauxNFSHandler simulating mount:')
        print('  Remote path: {}'.format(directory_name))
        print('  Server     : {}'.format(server_name))
        print('  Local path : {}'.format(
            os.path.basename(tempdir)))
        print('  Filename   : {}'.format(file_name))
        local_file = os.path.join(tempdir, file_name)
        fp = NFSFile(tempdir, file_name)
        content_type = (
                mimetypes.guess_type(file_name)[0] or 
                'application/octet-stream'
        )
        stats = os.stat(local_file)
        size = stats.st_size
        headers = {
                'Content-type': content_type,
                'Content-length': size,
        }
        return response.addinfourl(fp, headers,
                                   req.get_full_url())

if __name__ == '__main__':
    with tempfile.TemporaryDirectory() as tempdir:
        # Create content for temporary file
        filename = os.path.join(tempdir, 'file.txt')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('Contents of file.txt')

        # Create object for access to resources with NFS-handler and register it for default
        opener = request.build_opener(FauxNFSHandler(tempdir))
        request.install_opener(opener)

        # Open file with URL-address
        resp = request.urlopen(
                'nfs://remote_server/path/to/the file.txt'
        )
        print()
        print('READ CONTENTS:', resp.read())
        print('URL          :', resp.geturl())
        print('HEADERS:')
        for name, value in sorted(resp.info().items()):
            print('  {:<15} = {}'.format(name, value))
        resp.close()
'''
