"""
reloadall3.py: transitonal reload inserted modules(explicit stack)
"""

import types
from imp import reload
from  reloadall import status, tryreload, tester

def transitive_reload(modules, visited):
    while modules:
        next = modules.pop()
        status(next)
        tryreload(next)
        visited.add(next)
        modules.extend(x for x in next.__dict__.values()
                if type(x) == types.ModuleType and x not in visited)

def reload_all(*modules):
    transitive_reload(list(modules), set())

if __name__ == '__main__':
    tester(reload_all, 'reloadall3')
