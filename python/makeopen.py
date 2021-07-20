import builtins

class makeopen:
    def __init__(self, id):
        self.id = id
        self.original = builtins.open
        builtins.open = self
    def __call__(self, *pargs, **kargs):
        print('Custom open call %r:' % self.id, pargs, kargs)
        return self.original(*pargs, **kargs)
