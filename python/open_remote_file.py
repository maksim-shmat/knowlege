"""If you online, with urllib, open remote file."""

from urllib.request import urlopen

webpage = urlopen('http://www.python.org')

#1 Extract the relateve URL of th 'About'link

import re

text = webpage.read()
m = re.search(b'<a href="([^"]+)".*?>about</a>', text, re.IGNORECASE)
print(m.group(1))

# urlretrieve('http://www.python.org', '~/django2/knowlege/python/jill.html')
