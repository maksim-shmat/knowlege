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
