"""A simple screen-scrapping program."""

from urllib.requests umport urlopen
import re

p = re.compile('<a href="(/job/\\d+)/">(.*?)</a>')
text = urlopen('http://python.org/jobs').read().decode()
for url, name in p.findall(text):
    print('{}({})'.format(name, url))
