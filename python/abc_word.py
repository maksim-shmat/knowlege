"""Did is it a, b, and c in a word?"""

#1
'''
import sys
for ln in sys.stdin:
    if "a" in ln and ln.find("a") < ln.find("b") < ln.find("c"):
        print(ln.rstrip())
'''

#2
# isABC :: String -> Bool
def isABC(s):
    '''True if s contains 'a', 'b' and 'c', with the
    first occurrences of each in that order.
    '''
    return None != bind(
            bind(
                residue('a')('bc')(s)
            )(
                residue('b')('c')
            )
        )(
                residue('c')('')
        )

# residue Char -> String -> String -> Maybe String
def residue(c):
    '''Any characters remaining in s after c, unless
    c in preceded by excluded characters.
    '''
    def excluding(cs):
        def go(s):
            if s:
                x = s[0]
                return None if x in cs else(
                        s[1:] if c == x else go(s[1:])
                )
            else:
                return None
        return go
    return excluding

# ---------- TEST ----------
# main :: IO ()
def main():
    '''All words matching the isABC predicate
    in a local copy of jill.txt
    '''
    for x in enumerate(
            filter(
                isABC,
                readFile('jill.txt').splitlines()
            ),
            start=1
    ):
        print(x)

# ---------- GENERIC ----------

# bind (>>=) :: Maybe a -> (a -> Maybe b) -> Maybe b
def bind(m):
    '''Composition of a sequence of (a -> None | b) functions.
    If m is None, it is passed straight through.
    If m is x, the result is an application
    of the (a -> None | b) function (mf) to x.
    '''
    
    def go(mf):
        return m if None is m else mf(m)
    return go

# readFile :: FilePath -> IO String
def readFile(fp):
    '''The contents of any file at the path
    derived by expanding any ~ in fp.
    '''
    with open(fp, 'r', encoding='utf-8') as f:
        return f.read()

# MAIN ---
if __name__ == '__main__':
    main()
