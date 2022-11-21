"""Tips for vim."""

# How write ⅔, ², etc

:set digraph
2 backspace 3  == ⅔

2 backspace 2 == ²

#75 insert unicode and ad hoc characters

in insert mode:
ctrl-v + 123  # three characters

ctrl-vu + 1234 or 99bf # unicode ã¿ é¦¿

# if you need asc what the symbol in this text - put cursor on the ???
# and insert <ga>

ctrl-k + 12  == â½  # for both symbols(digraphs)
ctrl-k + bo  == ã<81>¼
ctrl-l + v%  == ð<8e>
:digraphs
:h digraph-table  # all digraphs

#56 digraphs for diacritics marks

ctrl-k c , = ã§
ctrl-k c . = ä<8b>
ctrl-k a ! = ã 

# greec

ctrl-k p * = ï<80>

# ?

ctrl-k ?i = â¿

ctrl-k ss = ã<9f>

# digraphs with set digraph

:set digraph

c backspace , = ã<87>
a bs ! = ã 
- bs = == â¯ upper score, or upper dash

' bs ' = â´
( bs a = ä<83>
< bs a = ç<8e>
, bs c = ã§
> bs o = ã´
! bs a = ã 
- bs o = âº
a bs - = ä<81>
o bs / = ã¸
? bs n = ã±
: bs e = ã«

:digraph  - list of digraphs

