" stack module"
stack = []
class error(Exception): pass

def push(obj):
    global stack
    stack = [obj] + stack

def pop():
    global stack
    if not stack:
        raise error('stack underflow')
    return stack[0]

def empty(): return not stack
def membetr(obj): return obj in stack
def item(offset): return stack[offset]
def length(): return len(stack)
def dump(): print('<Stack:%s>' % stack)
