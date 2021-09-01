"""Search about."""

import difflib

m_list = ['ape', 'apple', 'peach', 'puppy']
m_diff = difflib.get_close_matches('appel', m_list, n=2)
print(m_diff)

###### snowballstemmer lib, better than pymorph2, because search root in word
# first import module: EnglishStemmer, RussianStemmer for example

import snowballstemmer
# with Russian
rus = snowballstemmer.RussianStemmer()
rus.stemWord('Морские')
#'Морск'
## with English
en = snowballstemmer.EnglishStemmer()
en.stemWord('buautyfull')
# 'beauty'

######

import fnmatch, os

def find(pattern, startdir=os.curdir):
    for (thisDir, subsHer, filesHere) in os.walk(startdir):
        for name in subsHere + filesHere:
            if fnmatch.fnmatch(name, pattern):
                fullpath = os.path.join(thisDir, name)
                yield fullpath

def findlist(pattern, startdir=os.curdir, dosort=False):
    matches = list(find(pattern, startdir))
    if dosort: matches.sort()
    return matches

if __name__ == '__main__':
    import sys
    namepattern, startdir = sys.argv[1], sys.argv[2]
    for name in find(namepattern, startdir): print(name)

######

import os, sys
listonly = False
textexts = ['.py', '.pyw', '.txt', '.c', '.h']  # ignoring bytes-files

def searcher(startdir, searchkey):
    global fcount, vcount
    fcount = vcount = 0
    for (thisDir, dirsHere, filesHere) in os.walk(startdir):
        for fname in filesHere:
            fpath = os.path.join(thisDir, fname)
            visitfile(fpath, searchkey)

def visitfile(fpath, searchkey):
    global fcount, vcount
    print(vcount+1, '=>', fpath)
    try:
        if not listonly:
            if os.path.splitext(fpath)[1] not in textexts:
                print('Skipping', fpath)

            elif searchkey in open(fpath).read():
                input('%s has %s' % (fpath, searchkey))
                fcount += 1
                
    except:
        print('Failed:', fpath, sys.exc_info()[0])
        vcount += 1

if __name__ == '__main__':
    searcher(sys.argv[1], sys.argv[2])
    print('Found in %d files, visited %d' % (fcount, vcount))

###### findall()

import re

s = "Tim's phone number are 12345-41621 and 87963-85214"
match = re.findall(r'\d{5}', s)
if match:
    print(match)

######
