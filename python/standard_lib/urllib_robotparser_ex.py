"""urllib.ropotparser about."""

#1 robots.txt
'''
Sitemap: http://pymotw.com/sitemap.xml
User-agent: *
Disallow: /admin/
Disallow: /downloads/
Disallow: /media/
Disallow: /static/
Disallow: /codehosting/
'''

#2 urllib robotparser simple

from urllib import parse
from urllib import robotparser

'''
AGENT_NAME = 'PyMOTW'
URL_BASE = 'https://pymotw.com/'
parser = robotparser.RobotFileParser()
parser.set_url(parse.urljoin(URL_BASE, 'robot.txt'))
parser.read()

PATHS = [
        '/',
        '/PyMOTW/',
        '/admin/',
        '/downloads/PyMOTW-1.92.tar.gz',
]

for path in PATHS:
    print('{!r:>6} : {}'.format(
        parser.can_fetch(AGENT_NAME, path), path))
    url = parse.urljoin(URL_BASE, path)
    print('{!r:>6} : {}'.format(
        parser.can_fetch(AGENT_NAME, url), url))
    print()

'''

#3 urllib robotparser longlived

from urllib import robotparser
import time

'''
AGENT_NAME = 'PyMOTW'
parser = robotparser.RobotFileParser()
# User local copy
parser.set_url('file:robots.txt')
parser.read()
parser.modified()

PATHS = [
        '/',
        '/PyMOTW/',
        '/admin/',
        '/downloads/PyMOTW-1.92.tar.gz',
]

for path in PATHS:
    age = int(time.time() - parser.mtime())
    print('age:', age, end=' ')
    if age > 1:
        print('rereading robots.txt')
        parser.read()
        parser.modified()
    else:
        print()
    print('{!r:>6} : {}'.format(
        parser.can_fetch(AGENT_NAME, path), path))
    # Imitation waiting
    time.sleep(1)
    print()
'''
