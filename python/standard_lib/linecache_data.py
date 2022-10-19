"""For linecache_ex.py."""

import os
import tempfile

lorem = '''Lorem ipsum dolor sit amet, consectetuer
adipiscing elit. Vivamus eget elit. In posuere mi non
risus. Mauris id quam posuere ledtus soliciudin
varius. Praesent at mi. Nunc eu velit. Sec augue massa,
fermentum id, nonummy a, nonummy sit amet, ligula. Curabitur
eros pede, egestas at, ultricies ac, apellentsque eu,
tellus.

Sed sed odio sed mi luctus mollis. Integer et nulla ac augue
convallis accumsan. Ut felis. Donec lectus sapien, elementum
nec, condimentum ac, interdum non, tellus. Aenean viverra,
mauris vehicula semper porttitor, ipsum odio consectetuer
lorem, ac imperdiet eros odio a sepien. Nulla mauris tellus,
aliquam non, egestas a, nonummy et, erat. Vivamus saqittis
porttitor eros.'''

def make_tempfile():
    fd, temp_file_name = tempfile.mkstemp()
    os.close(fd)
    with open(temp_file_name, 'wt') as f:
        f.write(lorem)
    return temp_file_name

def cleanup(filename):
    os.unlink(filename)
