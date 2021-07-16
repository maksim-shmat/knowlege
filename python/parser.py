""" Synchronously download a list of webpages and time it. """

from urllib.request import Request, urlopen
from time import time

sites = [
        "http://news.ycombinator.com/",
        "https://www.yahoo.com/",
        "https://www.aliexpress.com/",
        "http://deelay.me/5000/http://deelay.me/",
]

def find_size(url):
    req = Request(url)
    with urlopen(req) as response:
        page = response.read()
        return len(page)

def main():
    for site in sites:
        size = find_size(site)
        print("Read {:8d} chars from {}".format(size, site))

if __name__ == '__main__':
    start_time = time()
    main()
    print("Ran in {:6.3f} secs".format(time() - start_time))

######

class UndefinedError(Exception): pass
from scanner import Scanner, LexicalError, SyntaxError

class Parser:
    def __init__(self, text=''):
        self.lex = Scanner(text)
        self.vars = {'pi': 3.14159}

    def parse(self, *text):
        if text:
            self.lex.newtext(text[0])
        try:
            self.lex.scan()
            self.Goal()
        except SyntaxError:
            print('Syntax Error at column:', self.lex.start)
            self.lex.showerror()
        except LexicalError:
            print('Lexical Error at column:', self.lex.start)
            self.lex.showerror()
        except UndefinedError as E:
            name = E.args[0]
            print("'%s' is undefined at column:" % name, self.lex.start)
            self.lex.showerror()

    def Goal(self):
        if self.lex.token in ['num', 'var', '(']:
            val = self.Expr()
            self.lex.match('\0')
            print(val)
        elif self.lex.token == 'set':
            self.Assign()
            self.lex.match('\0')
        else:
            raise SyntaxError()

    def Assign(self):
        self.lex.match('set')
        var = self.lex.match('var')
        val = self.Expr()
        self.vars[var] = val

    def Expr(self):
        left = self.Factor()
        while True:
            if self.lex.token in ['\0', ')']:
                return left
            elif self.lex.token == '+':
                self.lex.scan()
                left = left + self.Factor()
            elif self.lex.token == '-':
                self.lex.scan()
                left = left - self.Factor()
            else:
                raise SyntaxError()

    def Factor(self):
        left = self.Term()
        while True:
            if self.lex.token in ['+', '-', '\0', ')']:
                return left
            elif self.lex.token == '*':
                self.lex.scan()
                left = left * self.Term()
            elif self.lex.token == '/':
                self.lex.scan()
                left = left / self.Term()
            else:
                raise SyntaxError()

    def Term(self):
        if self.lex.token == 'num':
            val = self.lex.match('num')
            return val
        elif self.lex.token == 'var':
            if self.lex.value in self.vars.keys():
                val = self.vars[self.lex.value]
                self.lex.scan()
                return val
            else:
                raise UndefinedError(self.lex.value)
        elif self.lex.token == '(':
            self.lex.scan()
            val = self.Expr()
            self.lex.match(')')
            return val
        else:
            raise SyntaxError()
if __name__ == '__main__':
    import testparser
    testparser.test(Parser, 'parser1')
    
######

TraceDefault = False
class UndefinedError(Exception): pass

if __name__ == '__main__':
    from scanner import Scanner, SyntaxError, LexicalError
else:
    from .scanner import Scanner, SyntaxError, LexicalError

class TreeNode:
    def validate(self, dict):
        pass

    def apply(self, dict):
        pass

    def trace(self, level):
        print('.' * level + '<empty>')

class BinaryNode(TreeNode):
    def __init__(self, left, right):
        self.left, self.right = left, right

    def validate(self, dict):
        self.left.validate(dict)
        self.right.validate(dict)

    def trace(self, level):
        print('.' * level + '[' + self.label + ']')
        self.left.trace(level+3)
        self.right.trace(level+3)

class TimesNode(BinaryNode):
    label = '*'
    def apply(self, dict):
        return self.left.apply(dict) * self.right.apply(dict)

class DivideNode(BinaryNode):
    label = '/'
    def apply(self, dict):
        return self.left.apply(dict) / self.right.apply(dict)

class PlusNode(BinaryNode):
    label = '+'
    def apply(self, dict):
        return self.left.apply(dict) / self.right.apply(dict)

class MinusNode(BinaryNode):
    label = '-'
    def apply(self, dict):
        return self.left.apply(dict) - self.right.apply(dict)

class NumNode(TreeNode):
    def __init__(self, num):
        self.num = num

    def apply(self, dict):
        return self.num

    def trace(self, level):
        print('.' * level + repr(self.num))

class VarNode(TreeNode):
    def __init__(self, text, start):
        self.name = text
        self.column = start

    def validate(self, dict):
        if not self.name in dict.keys():
            raise UndefinedError(self.name, self.column)

    def apply(self, dict):
        return dict[self.name]

    def assign(self, value, dict):
        dict[self.name] = value

    def trace(self, level):
        print('.' * level + self.name)

class AssignNode(TreeNode):
    def __init__(self, var, val):
        self.var, self.val = var, val

    def validate(self, dict):
        self.val.validate(dict)

    def apply(self, dict):
        self.var.assign(self.val.apply(dict), dict)

    def trace(self, level):
        print('.' * level + 'set')
        self.var.trace(level + 3)
        self.val.trace(level + 3)

class Parser:
    def __init__(self, text=''):
        self.lex = Scanner(text)
        self.vars = {'pi':3.14159}
        self.traceme = TraceDefault

    def parse(self, *text):
        if text:
            self.lex.newtext(text[0])
        tree = self.analyse()
        if tree:
            if self.traceme:
                print(); tree.trace(0)
            if self.errorCheck(tree):
                self.interpret(tree)

    def analyse(self):
        try:
            self.lex.scan()
            return self.Goal()
        except SyntaxError:
            print('Syntax Error at column:', self.lex.start)
            self.lex.showerror()
        except LexicalError:
            print('Lexical Error at column:', self.lex.start)
            self.lex.showerror()

    def errorCheck(self, tree):
        try:
            tree.validate(self.vars)
            return 'ok'
        except UndefinedError as instance:
            varinfo = instance.args
            print("'%s' is undefined at column: %d" % varinfo)
            self.lex.start = varinfo[1]
            self.lex.showerror()

    def interpret(self, tree):
        result = tree.apply(self.vars)
        if result != None:
            print(result)

    def Goal(self):
        if self.lex.token in ['num', 'var', '(']:
            tree = self.Expr()
            self.lex.match('\0')
            return tree
        elif self.lex.token == 'set':
            tree = self.Assign()
            self.lex.match('\0')
            return tree
        else:
            raise SyntaxError()

    def Assign(self):
        self.lex.match('set')
        vartree = VarNode(self.lex.value, self.lex.start)
        self.lex.match('var')
        valtree = self.Expr()
        return AssignNode(vartree, valtree)
    
    def Expr(self):
        left = self.Factor()
        while True:
            if self.lex.token in [ '\0', ')']:
                return left
            elif self.lex.token ==  '+':
                self.lex.scan()
                left = PlusNode(left, self.Factor())
            elif self.lex.token == '-':
                self.lex.scan()
                left = MinusNode(left, self.Factor())
            else:
                raise SyntaxError()

    def Factor(self):
        left = self.Term()
        while True:
            if self.lex.token in ['+', '-', '\0', ')']:
                return left
            elif self.lex.token == '*':
                self.lex.scan()
                left = TimesNode(left, self.Term())
            elif self.lex.token == '/':
                self.lex.scan()
                left = DivideNode(left, self.Term())
            else:
                raise SyntaxError()

    def Term(self):
        if self.lex.token == 'num':
            leaf = NumNode(self.lex.match('num'))
            return leaf
        elif self.lex.token == 'var':
            leaf = VarNode(self.lex.value, self.lex.start)
            self.lex.scan()
            return leaf
        elif self.lex.token == '(':
            self.lex.scan()
            tree = self.Expr()
            self.lex.match(')')
            return tree
        else:
            raise SyntaxError()

if __name__ == '__main__':
    import testparser
    testparser.test(Parser, 'parser2')
""" Asynchronously download a list of webpages and time it

Dependencies: Make sure you instanll aiohttp

pip install aiohttp aiodns

"""
import asyncio
import aiohttp
from time import time

sites = [
        "http://news.ycombinator.com/",
        "https://www.yahoo.com/",
        "http://www.aliexpress.com/",
        "http://deelay.me/5000/http://deelay.me/",
]

async def find_size(session, url):
    async with session.get(url) as response:
        page = await response.read()
        return len(page)

async def show_size(session, url):
    size = await find_size(session, url)
    print("Read {:8d} chars from {}".format(size, url))

async def main(loop):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for site in sites:
            tasks.append(loop.create_task(show_size(session, site)))
        await asincio.wait(tasks)

if __name__ == '__main__':
    start_time = time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    print("Ran in {:6.3f} secs".format(time() - start_time))
"""Parser something."""

import re

matchobj = re.match('Hello(.*)World', text2)
print(matchobj)

pattobj = re.compile('Hello(.*)World')
matchobj = pattobj.match(text1)
matchobj.group(1)

patt = '[ \t]*Hello[\t]+(.*)[Ww]orld'
line = ' Hello spamworld'
mobj = re.match(patt, line)
mobj.group(1)

patt = b'[ \t]*Hello[ \t]+(.*)[Ww]orld'
line = b' Hello spawnworld'
re.match(patt, line).group(1)

re.match(patt, ' Hello spawnworld')

re.match('[ \t]*Hello[ \t]+ (.*)[Ww]orld', line)

#--------
re.split('--', 'aaa--bbb--ccc')
re.sub('--', '...', 'aaa--bbb--ccc')

re.split('--|==', 'aaa--bbb==ccc')

re.split('[-=]', 'aaa-bbb=ccc')

re.split('(--)|(==)', 'aaa--bbb==ccc')

re.split('(?:--)|(?:==)', 'aaa--bbb==ccc')

#-------
re.match('(.*)/(.*)/(.*)', 'spam/ham/eggs').groups()

re.match('<(.*)>/<(.*)>/(.*)>', '<spam>/<ham>/<eggs>').groups()

re.match('/s*<(.*)>/?<(.*)>/?<(.*)>', ' <spam>/<ham><eggs>').groups()

re.match('Hello\s*([a-z]*)\s+(.*?)\s*!', 'Hellopattern world !').groups()

re.findall('<(.*?)>', '<spam>/<ham>/<eggs>')

re.findall('<(.*?)>', '<spam> / <ham><eggs>')

re.findall('<(.*?)>/?<(.*?)>',
        'todays menu: <spam>/<ham>...<eggs><s>').groups()

re.findall('<(.*?)>.*<(.*?)>', '<spam> \n <ham>\n<eggs>')

re.findall('(?s)<(.*?)>.*<(.*?)>', '<spam> \n <ham>\n<eggs>')

re.findall('(?s)<(.*?)>.*?<(.*?)>', '<spam> \n <ham>\n<eggs>')

re.search('(?P<part1>\w*)/(?P<part2>\w*)', '...aaa/bbb/ccc]').groups()

re.search('(?P<part1>\w*)/(?P<part2>\w*)', '...aaa/bbb/ccc]').groupdict()

re.search('(?P<part1>\w*)/(?P<part2>\w*)', '...aaa/bbb/ccc]').groups(2)

re.search('(?P<part1>\w*)/(?P<part2>\w*)',
        '...aaa/bbb/ccc]').group('part2')

re.findall('(?P<part1>\w*)/(?P<part2>\w*)', '...aaa/bbb/ccc/ddd]')

###### write your own generator

import request
import re

def get_pages(link):
    pages_to_visit = []
    pages_to_visit.append(link)
    pattern = re.compile('https?')
    while pages_to_visit:
        current_page = pages_to_visit.pop(0)
        page = requests.get(current_page)
        for url in re.findall('<a href="([^"]+)">', str(page.content)):
            if url[0] == '/':
                url = current_page + url[1:]
            if pattern.match(url):
                pages_to_visit.append(url)
        yield current_page
webpage = get_pages('http://www.example.com')
for result in webpage:
    print(result)

######
