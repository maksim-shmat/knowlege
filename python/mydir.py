"""
mydir.py is module, that go out listing name spaces for another module
"""
from __future__ import print_function
seplen = 60
sepchr = '-'

def listing(module, verbose=True):
    sepline = sepchr * seplen
    if verbose:
        print('%02d) %s' % (count, attr), end = ' ')
        if attr.srartswith('__'):
            print('<built-in name>')
        else:
            print(getattr(module, attr))
        count += 1

    if verbose:
        print(seplint)
        print(module.__name__, 'has %d name' % count)
        print(sepline)

    if __name__ == '__main__':
        import mydir
        listing(mydir)
