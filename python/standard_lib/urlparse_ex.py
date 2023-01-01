"""urlparse about."""

#1 urllib parse urlparse

from urllib.parse import urlparse

'''
url = 'http://netloc/path;param?query=arg#frag'
parsed = urlparse(url)
print(parsed)

RESULTS:
ParseResult(scheme='http', netloc='netloc', path='/path', params='param', query='query=arg', fragment='frag')
'''

#2 urllib parse urlparseattrs

from urllib.parse import urlparse

'''
url = 'http://user:pwd@NetLoc:80/path;param?query=arg#frag'
parsed = urlparse(url)
print('scheme   :', parsed.scheme)
print('netloc   :', parsed.netloc)
print('path     :', parsed.path)
print('params   :', parsed.params)
print('query    :', parsed.query)
print('fragment :', parsed.fragment)
print('username :', parsed.username)
print('password :', parsed.password)
print('hostname :', parsed.hostname)
print('port     :', parsed.port)

RESULTS:
scheme   : http
netloc   : user:pwd@NetLoc:80
path     : /path
params   : param
query    : query=arg
fragment : frag
username : user
password : pwd
hostname : netloc
port     : 80
'''

#3 urllib parse urlsplit

from urllib.parse import urlsplit

'''
url = 'http://user:pwd@NetLoc:80/p1;para/p2;para?query=arg#frag'
parsed = urlsplit(url)
print(parsed)
print('scheme  :', parsed.scheme)
print('netloc  :', parsed.netloc)
print('path    :', parsed.path)
print('query   :', parsed.query)
print('fragment:', parsed.fragment)
print('username:', parsed.username)
print('password:', parsed.password)
print('hostname:', parsed.hostname)
print('port    :', parsed.port)

RESULTS:
SplitResult(scheme='http', netloc='user:pwd@NetLoc:80', path='/p1;para/p2;para', query='query=arg', fragment='frag')
scheme  : http
netloc  : user:pwd@NetLoc:80
path    : /p1;para/p2;para
query   : query=arg
fragment: frag
username: user
password: pwd
hostname: netloc
port    : 80
'''

#4 urllib parse urldefrag

from urllib.parse import urldefrag

'''
original = 'http://netloc/path;param?query=arg#frag'
print('original:', original)
d = urldefrag(original)
print('url    :', d.url)
print('fragment:', d.fragment)

RESULTS:
original: http://netloc/path;param?query=arg#frag
url    : http://netloc/path;param?query=arg
fragment: frag
'''

#5 urllib parse geturl

from urllib.parse import urlparse

'''
original = 'http://netloc/path;param?query=arg#frag'
print('ORIG  :', original)
parsed = urlparse(original)
print('PARSED:', parsed.geturl())

RESULTS:
ORIG  : http://netloc/path;param?query=arg#frag
PARSED: http://netloc/path;param?query=arg#frag
'''

#6 urllib parse urlunparse

'''
from urllib.parse import urlparse, urlunparse

original = 'http://netloc/path;param?query=arg#frag'
print('ORIG  :', original)
parsed = urlparse(original)
print('PARSED:', type(parsed), parsed)
t = parsed[:]
print('TUPLE :', type(t), t)
print('NEW   :', urlunparse(t))

RESULTS:
ORIG  : http://netloc/path;param?query=arg#frag
PARSED: <class 'urllib.parse.ParseResult'> ParseResult(scheme='http', netloc='netloc', path='/path', params='param', query='query=arg', fragment='frag')
TUPLE : <class 'tuple'> ('http', 'netloc', '/path', 'param', 'query=arg', 'frag')
NEW   : http://netloc/path;param?query=arg#frag
'''

#7 urllib parse urlunparseextra

'''
from urllib.parse import urlparse, urlunparse

original = 'http://netloc/path;?#'
print('ORIG  :', original)
parsed = urlparse(original)
print('PARSED:', type(parsed), parsed)
t = parsed[:]
print('TUPLE :', type(t), t)
print('NEW   :', urlunparse(t))

RESULTS:
    ORIG  : http://netloc/path;?#
PARSED: <class 'urllib.parse.ParseResult'> ParseResult(scheme='http', netloc='netloc', path='/path', params='', query='', fragment='')
TUPLE : <class 'tuple'> ('http', 'netloc', '/path', '', '', '')
NEW   : http://netloc/path
'''

#8 urllib parse urljoin

from urllib.parse import urljoin

'''
print(urljoin('http://www.example.com/path/file.html',
              'anotherfile.html'))
print(urljoin('http://www.example.com/path/file.html',
              '../anotherfile.html'))
RESULTS:
    http://www.example.com/path/anotherfile.html
http://www.example.com/anotherfile.html
'''

#9 urllib parse urljoin with path

from urllib.parse import urljoin

'''
print(urljoin('http://www.example.com/path/',
              '/subpath/file.html'))
print(urljoin('http://www.example.com/path/',
              'subpath/file.html'))

RESULTS:
http://www.example.com/subpath/file.html
http://www.example.com/path/subpath/file.html
'''

#10 urllib parse urlencode

from urllib.parse import urlencode

'''
query_args = {
        'q': 'query string',
        'foo': 'bar',
}

encoded_args = urlencode(query_args)
print('Encoded:', encoded_args)

RESULTS:
Encoded: q=query+string&foo=bar
'''

#11 urllib parse urlencode doseq

from urllib.parse import urlencode

'''
query_args = {
        'foo': ['foo1', 'foo2'],
}
print('Single  :', urlencode(query_args))
print('Sequence:', urlencode(query_args, doseq=True))

RESULTS:
Single  : foo=%5B%27foo1%27%2C+%27foo2%27%5D
Sequence: foo=foo1&foo=foo2
'''

#12 urllib parse parse qs

from urllib.parse import parse_qs, parse_qsl

'''
encoded = 'foo=foo1&foo=foo2'

print('parse_qs :', parse_qs(encoded))
print('parse_qsl:', parse_qsl(encoded))

RESULTS:
parse_qs : {'foo': ['foo1', 'foo2']}
parse_qsl: [('foo', 'foo1'), ('foo', 'foo2')]
'''

#13 urllib parse quote

from urllib.parse import quote, quote_plus, urlencode

'''
url = 'http://localhost:8000/~hellhound/'
print('urlencode() :', urlencode({'url': url}))
print('quote()     :', quote(url))
print('quote_plus():', quote_plus(url))

RESULTS:
urlencode() : url=http%3A%2F%2Flocalhost%3A8000%2F~hellhound%2F
quote()     : http%3A//localhost%3A8000/~hellhound/
quote_plus(): http%3A%2F%2Flocalhost%3A8000%2F~hellhound%2F
'''

#14 urllib parse unquote

from urllib.parse import unquote, unquote_plus

'''
print(unquote('http%3A//localhost%3A8080/%7Ehelhound/'))
print(unquote_plus(
    'http%3A%2F%2Flocalhost%3A8080%2F%7Ehellhound%2F'
))

RESULTS:
http://localhost:8080/~helhound/
http://localhost:8080/~hellhound/
'''
