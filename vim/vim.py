"""All about vim."""

# first $ touch ~/.vimrc
# an then $ touch ~/.exrc
# .exrc for /home/ is global
# .exrc local for special dir (special for prog, or special for writing, with special options how change global .exrc options)
:version  # how function is available in your version
:help  # read documentation
:h operator  # documentation is awesome

:h $MYVIMRC
/usr/share/vim/vim81/defaults.vim  # file with defaults settings or .vimrc

# Sands of Time

:erlier 4m - in 4 min back

:later 45s - little-bit forvard

:undo 5 - 5 changes back

:undolist - a tree of changes

Ctrl + r - redo

# Move all text from cursor to end
    > G

# Find (+)
    f+
#3 Freeze keyboard

Ctrl + S

#4 Unfreeze keyboard

Ctrl + Q

#5 If ''' is l=trubles roll page from up to down

gg, down-down to bottom of page

#6 change word

cw

#7 Read only

vi -R jill.py
# or vim -Z jill.py
# or rview jill.py
view jill.py

#8 Moving
0 - to start a string
$ - to end a string
b - up
2w - 2 right
hjkl, 2h, 2j, 2k, 2l

44g  # go to 44 string
10enter  # go to 10 string down

``  # go to previous place
''  # go to previous place on the start string

#9 marks

:mark  # show me all of my bookmarks
:delmarks 2 zoru n-mark  # delete bookmarks
m bookmark_name  # set a bookmark

# temporary marks (for current seance)
m{a-xa-z} # mark
a-x - local 26 marks
a-z - global 26 marks

'x  # 'go to start string with local mark x
`x  # go to local mark x where is it

mx  # insert global mark x
`x  # go to global mark x 

``  # go to previous temp mark
''  # go to start string on the previous temp mark

`^  # go to place last insert mode
`.  # go to place last change


#10 abbreviation

:ab inc illigitimi non carborundum  # set an abbreviation
and then just write inc for print full name
:una inc  # unset the abbreviation

#11 autocomplete

- write word multiple times, e.g. antarctica
- type ant and then use ctrl+n (or ctrl+p)

#12 work with numbers of lines

:2, 10d  # delete lines 2 through 10

:25, $d  # delete every line from line 25 to the end of the file

:%d  # delete every line

:5, 10t 15  # copy lines from 5 through 10 and insert it after line 15

:5, 10m 15  # move lines from t threugh 10 and insert it atrer line 15

#13 wrapmargin - how many characters into string

:set wm=79
:set wm=0  # remove wrapmargin

# set numbers of strings

:set nu  # show
:set nonu  # hide

# temporary show numbers

:1, 10#  # show numbers of strings from 1-10
:.,+20#  # show numbers of strings from cursor to +20 strings down
:.=  # number of strings where cursor
:/pattern/=  # number of string where pattern

#14 moving on the text

w or w(without punctuation)  # (word) move by one word to the right
b or b(without punctuation)  # (word) move to backward
2w and 2b
e or e(without punctuation)  # go to end word

(  # go to start this sentence.
)  # go to start next sentence.

{  # go to start current block
}  # go to start next block

[[  # go to start current paragraph
]]  # go to start next paragraph

3)  # got to through 3 sentences
d)  # del from cursor to end sentence
2y}  # yanked two next block

ctrl + o  # takes your back to older position
ctrl + i  # to newer position

%  # cursor on the braket % go to another one braket, from ( -->)

#15 moving with g

1g  # start page
42g  # string n.42
g  # go to the bottom
gg  # go to the top
+  # go to first new line
-  # go to first backward line

#16 redaction

a  # append, with num
c  # change, with num
d  # delete, with num
e  # edit
p  # put, with num
y  # yank
s  # substitute, add simbol (or both with 2s) 
s  # substitute whole string
r  # replace
i  # insert
o  # open

~ or 22~  # change register

cw  # change word
c2b  # change word to backward on the two words
c0  # change words to the start of string from cursor  (but cc ?)
c$ (equal c)  # change words to the end of sting from the cursor (but cc ?)
cc  # change string
C  # change from cursor to the end string

#17 delete

dw  # delete word from cursor, with whitespace
de  # delete word from cursor, without space
2dd  # delete two strings
d == d$  # delete string from cursor to end string

x  # delete char to rite from cursor
x  # delete char to left from cursor
2x and 3x  # etc.

:%d  # del all into file

#18 p - put

first d or vd  # deleted text save to 'put' buffer
p  # and then p to put text from buffer in a new place
   # or paste after string where is cursor

p  # big p - put text befrore cursor
   # or paste before string where is cursor

#19 replace two char

in the word mvoe place cursor to v
and xp  -> move

# replace one char
gr

#20 yanked - copy to buffer

y  # copy after cursor
3yk  # copy 3 string to up
3y  # copy 3 string to beneath
y$  # copy string from cursor
yw  # yank word
yy or y  # copy string

#21 amalgamate strings

with a
screen editor

j  # amalgamate both string
or 2j
with a screen editor

#22 screenscrolling

^f  # down screen
^b  # up screen
^d  # down halfscreen
^u  # up halfscreen
zenter  # down one screen
200zenter  # go to 200 line
z.  # this line to center of screen
z-  # this line to bottom of screen

#23 reload screen for remove sys message

^l  # reload page

#24 steps into one screen

h  # go to up
m  # go to center
l  # go to bottom
3h  # go to 3 lines to up
4l  # go to 4 lines to down

^  # go to first not empty char in string
3|  # go to 3 |1|2|3<-

#25 search
        
        q/  # search from history
        
        :/d?spam  # search d?spam

	d?spam  # del text from cursor to the word spam

	fx  # find and move on new [x] simpol in the string

	;  # repeat fx
	,  # repeat fx to backward

	dfx  # del all before [x] from cursor, del with [x]

	tx  # find [x] but cursor before [x]
	dtx  # del [x] but not include [x]
        
        :set ic  # set ignore case
        :set noic  # unset ignore case
        :set ic?  # check

        :set hls  # highlight search results
        :set is  # incsearch, show partial matches for a search phrases

        :set path+=path/**  # add path for :find, ** - mean recursively

#26 open file with pattern
$ vi +/pattern file
or posix(linux) style -> $ vi -c/pattern file
for pattern with spaces use -> $ vi +/'pat tern' file
                               $ vim -c/pat\ tern file
for ease use your own pattern e.g mark, and then find your pattern.

#27 list all swap files

$ vi -r

#28 save file to buffer

:pre  or :preserve

#29 paste from one of 1-9 buffers

"2p or "26p

# step by step down for buffers

"1pu.u.u...          #"

#30 copy to named buffer a-z

"dyy  # "copy to 'd' buffer
"a7yy  # "copy 7 strings to 'a' buffer
"a5dd  # "del 5 str to 'a' buffer

# add more to buffer

"zd)  # "del from cursor to end sentence and add to 'z' buffer
2)  go to two sentence down and
"zy)  # "add new sentence to 'z' buffer

# work with @-functions of buffer

just write in a text field:
cwbubsyexample^[  # that means cw bubsyexample ctrl-v esc
then del and move it to the buffer:
"gdd    #"
and then go to start a word, and replace it with buffer
@g
result: word -> bubsy^[
emmm...

# past from named buffer

"dp  # "put buffer 'd' before cursor
"ap  # "put buffer 'a' after cursor

#32 work with ex, ex-mode

:6  # got to sixths string

:3, 18d  # del strings in diapazone from 3 to 18

:160, 224m23  # move strings from 160 to 224 -> 24str
:[range]move{address}
:'<,'>m$  # visual block move to the end of file

;  # mean current, with number of str, else (if ,)cursor place current
:100; +5 p  # from 100 +5 str print

:[6, 12]delete[x]  # del to buffer x
:[6, 12]yank[x]  # copy
:[18]put[x]  # put after 18 line

========================
:[range]copy{address}  # copy, 82copy95 - add copy string from 82 to 95 str
# or :6copy. - copy to next string from the cursor
# or :6co.
# or :6t.
# :t.  # copy current string and past to the next string(yyp analog)
# :t$  # copy currnet string to the end of file
# :'<,'>t0  # '<,'> == visual mode block, and copy it to the start file
# :'<,'>t$  # visual block copy to the end of file
:23, 29co100  # copy from 23 to 29 and insert afer 100str
========================

:[range]join  # join strings
:[range]normal{command}  # fulfil command from normal mode for diapazon strings
:[range]substitute/{pattern}/{string}/[flags]  # change pattern to the string
:[range]global/{pattern}/[cmd]  # fulfil command[cmd] for pattern globally

:h ex-cmd-index  # all ex-commands

@:  # repeat last ex-cmd
@@  # repeat-repeat last ex-cmd
@:  # after @@ backward one step, or use ctrl-o

#33 global find

:g/pattern  # find and go to words with pattern
:g!/pattern  # find and go to words without pattern
:60, 123g/pattern/p  # into diapazon

#34 combined commands with pipe

:1,3d | s/thier/their/  # del and then rewrite

:1,5 m 10 | g/pattern/nu  # move and then view str with pattern and num str

#34 save as new file with new name

:w newfile.py

:230,$w newfile.py  # save from 230 string into newfile

:.,600w newfile  # save from current to 600 into newfile

:1, 10w newfile  # thats both commands make two insertions into file
:340, $w >> newfile

#35 read another file from opened file with vim

:read filename  # inserted core file into current place of cursor
:r filename
:r /home/time/data
:$r /home/tim/data

:185r /home/tim/data  # insert after 185 str

:/pattern/r  /home/tim/data  # insert after pattern str

#36 open both or more files.

$ vi file1 file2
:args(or :ar)  # how many files was open
:rewind(or :rew)  # change to first file in a list
:last  # change to last file in a list of files
change file1
:w  # save file1
change file2
:x  # save and quit
:e!  # or remove all changes

#37 open more files from one's opened

open file1 and then
:e file2
ctrl+^(carret)  # go to previous file

#38 global substitutes

:s/old/new/
:s/old/nen/g  # g is global
:50, 100s/old/new/g  # substitute from 50str to 100

:1, $s/old/new/g  # substitute in all file
:%s/old/new/g  # substitute ina all file
:%s/old/new/gc  # g - global and c - confirm all changes

:e!  # remove old version from buffer i.e remove changes

:g/pattern/s/old/new/g
:g/<body>/s/of/on/g  # target substitute of pattern

:g/editer/s//editor/g  # both equivalent
:%s/editor/editor/g
or
g&  # after cmd g.e. 1) :s/target/replacement/g 2) g& (same :%s//~&)
or
:&&

#39 regular expression for vim

  - any symbol (p.p = pip, pep etc)
*  - bugs* = bugss, bug, bugs, bugsss etc
^  - ^part = part at the begining a string, else ^ is carret
$  - here:$ = here: at the end of string, else $ is dollar
\  - next simbol is casual, \. - merely dot, \\ - is backslash
\| - set variants (house\|home)
\+ - one or more from previous regular expression
\= - one or none from previous regular expression
\{n,m} - diapazon from previous regular expression {0,32000}
\{n} - n prev re
\{n,} - how many more prev re, but not less n
\{,m} - how many more prev re, from 0 to m
\{} - how many more prev re, from 0
\{-n,m} - how many min prev re, in diapazon from -n to m
\{-n}
\{-n,}
\{-,m}

\i - any symbol from isindent
\i - any symbol from isindent, but without numbers

\k - any keyword from iskeyword
\k - any keyword but witout numbers

\f - any filename from isfname
\f - any filename from isfname, but without numbers

\p - any printable symbol
\p - but without numbers

\s - spaces with taps
\s - all that not spaces and tabs

\b - backspace

\e - escape

\r - carret

\t - tab

\n - ???

~ - last changeble string



[ ] - [ab] = a or b, p[aeiou]t = pat, pet, pit, pot, put

/[tt]he = the or the

[^0-9] = that carret means - not, anybody but not number
[[:alpha:]!] = a, l, p, h, or !
[[.ch.]] = ch only, but not c and h
[[=e=]] = e, franch e with`, and other e deviation

[:alnum:] - char and num
[:alpha:] - alphabetical symb
[:blank:] - space and tab
[:cntrl:] - control symb
[:digit:] - num only
[:graph:] - all visual symb, without spaces or tabs
[:lower:] - lowercase
[:print:] - printable symb, with spaces etc
[:punct:] - punctuation symb
[:space:] - space symb
[:upper:] - upercase
[:xdigit:] - sixteenth num

\( \) - save to the buffer, \(that\) or \(this\) = that to buffer1, this to b2
:s/\(that\) or \(this\)/\2 or \1/  # changing to this or that (result: this or that)
:s/\(that\) or \(this\)/\u\2 or \l\1/  # changing places and change low/up cases (result: this or that)

:s/\(abcd/)\1/alphabet-soup  # changeing abcd to alphabet-soup

\< - start of word, \<ac = action
\> - end of word, ac\> = maninac

& - same name, :%s/cuchinski/&, zax/ = :%s/cuchinski/cuchinski;, zax/
:1, 10s/.*/(&)/  - make ->(every str into brakets)<- from 1-10 str

\u - upercase, :%s/yes, doctor/\uyes, \udoctor (result: yes, doctor)
\l - lower case 

\u, \l - upper/lower cases 
:%s/fortran/\ufortran/  (result: fortran)
:%s/fotran/\u&/  (same)

-----------------------
# case1: change child to children, with the same punctuation
# in the text is: child , child, child,, child., etc
# and we need is: childred , children, children,, children., etc
:%s/child\([ ,.;:!?]\)/children\1/g  # \( \)-save to buffer1 punctuation
:%s/\<child\>/children/g  # that is for not change words as fairchild
-----------------------

# case2: change half word
mgibox routine.
mgrbox routine.
mgabox routine.

:g/mg\([ira]\)box/s//mg\1square/g

result:
mgisquare routine.
mgrsquare routine.
mgasquare routine.

:g/mg[ira]box/s/box/square/g  # but it may change another *box words to *square

result:
mgisquare routine.
mgrsquare routine.
mgasquare routine.

#case3: move paragraphs
.rh "syntax"  # name of paragraphs
blahblah.
.rh "description"
blah
blah.
.rh "parameters"
blah
    blah.

:g /synatx/.,/description/-1 move /parameters/-1  # -1 for print 1str less
result:
description go up above syntax

# ir need del paragraph\

:g/description/.parameters/-1d

#case4: change double spaces to one space
:%s/  */ /g

#case5: change one or more spaces after . or : to two spaces
:%s/\([:.]\)  */\1  /g

#case6: del all empty strings
:g/^$/d

#case7: del all empty and tab-tab or space-space strings
:g/^[ tab]*$/d
:g/^[ tab][ tab]*$/d

#case8: del all spaces on the start string
:%s/^  *\(.*\)/\1/

#case9: del all spaces on the end string
:%s/\(.*\)  *$/\1/

#case10: insert [  >] into start all strings
:%s/^/>  /

#case11: add . to end next six strings

:.,+5s/$/./

#case12: change parts of sentens between defice ->[-]<-

:%s/\(.*\) - \(.*\)/\2 - \1/

#case13: change all leters on the upercase

:%s/.*/\u&/  # faster
:%s/./\u&/g  # little bit slower

#case14: reverse positions of strings
:g/.*/mo0
:g/^/mo0

#case15: where is not typing "paid in full" print "overdue"
:g!/paid in full/s/$/ overdue/
:v/paid in full/s/$/ overdue/

#case16: every string not start with number move to end of text

:g!/^[[:digit:]]/m$
:g/^[^[:digit:]]/m$

#case17: remove numbers into head of paragraphs, from start of strings

:%s/^[1-9][0-9]*\.[1-9][0-9.]* //

#case18: change word fortran to fortran (acronym formula translation)

:%s/\(for\)\(tran\)/\u\1\2\e (acronym of \u\1\emula \u\2\eslation)/g

#case19 make 10 copies 12-17 str to end of file
:1,10g/^/ 12, 17t$

#40 :set

:set all  # list all settings

:set laststatus=2  # show status: filename [+], strings amount, percentage.
:set laststatus=1  # off show status

#41 vim and unix

:!date  go to bash, see date, press enter, and go back to vim

:sh  # go to bash, enter, back vim

:r !sort jill.csv  # open file, sort and write info from jill.csv

:!ls  # go see how named files in current dir
:r filename

:16,19!sort  # sort strings from 16-19

cursor to 16 string and 5!!sort  # sort from cursor 16str-19
or !5!sort

go cursor to the string for change cases
!)  # then write for change lower to upper cases
tr '[:lower:]' '[:upper:]' enter

#42 map

e.g. change places two word 'the' and 'scroll', in the sentence 'you can the scroll page'
cursor on to 'the'
dwelp  # dw - del word, e - go to end next word, l - move to one space to right, p - put del word
then map it command
:map v dwelp  # v is used in vim, use another button!
touch v for change plces any two words

#43 prefixes

vim -o file1 file2 - open all files into same windows, or open empty window if files less than
or vim -o5 file1 file2 - two windows is visual and three is hiden

vim -o file1 file2 - open all into vertical windows

-z - closed mode, without bash support or other helps
# and [rvim] same, with stop seans since ^z

#44 remote server commands vith vim...

-remote file
-remote-silent file
-remote-wait file
-remote-send file
-servername name
-remote-expr expr
-remote-wait-silent file
-remote-tab
-remote-send keys
-remote-wait-silent file
-serverlist

#45 where am i?
ctrl + g  # number of current string and path to file

#46 completition text or command
first type e.g. :e
then tap ctrl + d

#47 through the windows

ctrl + w + w
ctrl + w + j (down)
ctrl + w + b (bottom)
ctrl + w + t (top)

#48 jump to a subject

position the cursor on a tag (e.g. |bars|) and hit ctrl-].
jump back:  type ctrl-o.  repeat to go further back.

#49 split windows

:split  # two windows for one file
:vsplit  # vertical two window for one file
or :split jill.py

:[n]split [++opt][+cmd][file]
:15split ++fileformat=unix otherfile

:new jill.py  # open new split window
:vnew jill.py  # open new vertical split window
:[n]new [++opt][+cmd][file]

:sview filename  # open horizontal split window read only
:sfind [++opt] [+cmd] filename  # first find file, if it be than open window

:clo  # close current window
:hid  # hidden current window
:on  # only current window is vision


# windows

ctrl-w v (and :e jill.txt) # open vertical window
or :vsplit jill.txt
   :vsp jill.txt

ctrl-w s (and :e jill.py) # open horizontal window
or :split jill.py
   :sp jill.py

ctrl-w c  # close current window
or :close  # for close current window
   :clo
or :only  # for close other windows
   :on

ctrl-ww  # go to next window
ctrl-w h,j,k,l  # go to the: left, down, up, right

ctrl-w r  # move window to -->
ctrl-w r  # move window from there <--
ctrl-w x

# change size of windows

ctrl-w =  # coequal

ctrl-w _  # max height current window
22ctrl-w _  # increase height to 22 lines

ctrl-w |  # default width
20ctrl-w |  # increase width to 20 lines

ctrl-w >,<  # change width

:resize -4  # decrease window onto four lines
:cmdheight  # for resize bottom ex-window
:verticalresize n

z22  3 set window 22 lines

#50 tags open tag into new window

open :help
write any tag e.g "bars"
type:
:stag! bars  # article "bars" will be opened in a new window

#51 open file under the cursor(link?) into new tab
^wgf
^wgf  # and cursor after filename

#52 open file in a new tab

:tabnew jill.py
or :tabnew  # empty file

:tabclose  # close current tab
:tabonly  # close all another without this tab

ctrl + pgup, pgdn  # change tab in terminal

#53 [+] convolution

za, za - change all, one
zc, zc - close all, one
zd, zd - del all, one
ze - del all
zf - make convolution from cursor line to move cmd
countzf - make conv from curlor line to count lines
zm - foldlevel opetion == 0
zn, zn, zi - foldenable option on/off
zo, zo - open conv all(enclose), one
zj, zk - move cursor to next conv
zm, zr - -1 or +1 foldlevel option

3zf - convolution three lines
or 2zfj - conv two lines down
zfgg - conv whole file if cursor is bottom

:set foldcolumn=n  # set suggestions enclose convolution about

:set foldmethod=indent  # convolution with parameters of strings
:set shiftwidth=4  # check tabulation for indent
:set foldlevel=2  # deep view in convolution
:set foldlevel=0  # only headers

then (zr) (zm) - open/closed

#54 autofoldering prog.lang.

set foldcolumn=3
ze - remove all previous folders

:set foldenable
:set foldmethod=syntax

#55 autocomplete

:imap tab <c-p> - autocomplete to tab e.g.

ctrl-x ctrl-l - autocomplete whole string

ctrl-n, ctrl-p - up/down in list of variants
and ctrl-e - esc

ctrl-x ctrl-n - autocomplete with keyword

ctrl-x ctrl-k - autocomplete with dictionary

ctrl-x ctrl-t - autocomplete with tesaurus

ctrl-x ctrl-i - autocomplete with include files

ctrl-x ctrl-] - autocomplete with tags

ctrl-x ctrl-f - autocomplete with filename

ctrl-x ctrl-d - autocomplete with macros name

ctrl-x ctrl-v - comand line completition

# autocomplete in insert mode
Ctrl-p or Ctrl-n
Ctrl-n  # next
Ctrl-p  # previous
Down/Up
Ctrl-y  # yes
Ctrl-e  # exit
Ctrl-h or BackSpace(<BS>)  # del example
Ctrl-l  # add example

#56 digraphs for diacritics marks

ctrl-k c , = „ß
ctrl-k c . = ‰ã
ctrl-k a ! = „†

# greec

ctrl-k p * = ÔÄ

# ?

ctrl-k ?i = ‚ø

ctrl-k ss = „ü

# digraphs with set digraph

:set digraph

c backspace , = „á
a bs ! = „†
- bs = == ‚Ø upper score, or upper dash

' bs ' = ‚¥
( bs a = ‰É
< bs a = Áé
, bs c = „ß
> bs o = „¥
! bs a = „†
- bs o = ‚∫
a bs - = ‰Å
o bs / = „∏
? bs n = „±
: bs e = „´

:digraph  - list of digraphs

#57 show dir/files and edit files in another window

o - open file

#58 make .html from .txt

go to jill.txt
write:
:runtime!syntax/2html.vim  # make entire file

:25, 44tohtml  # make chank file

#59 difference

$ vimdiff old_file new_file
or
$ vim -d old_file new_file

#60 undo/redo

:2undo or 2u

:3redo or 2ctrl-r

#61 fast change two symbols, leter
xp - erdo --> redo

#62 fast change two sentence

ddp - from botom line of sentence to down

#63 window last commands
:ctrl-f
back from window:
ctrl-c

#64 if you traped in :ex mode

q - move you to :ex mode
write:
:vi  # go out from :ex mode

#65 join short sentence

j or 3j

#66 add spaces around plus

f+  # find + in sentence, if need find to backward press - ,
s + <esc>  # rm + and add space, plus, space, esc
;  # find next plus
. repeat

#67 fast find

cursor on the word
*
n,n

# find char
f[char]  # e.g. <fo> for find [o]
;  # next
,  # previous

# find previous char
f[char]

t[char]  # find place before [char]
t[char]  # find backward place after [char]

#68 delete back, or there and back again

db and x

and b  # back
dw

#69 delete a word

if cursor between words you may del next word without moving

daw

#70 addition and subtraction

cursor on the number or will be able next number in left into str
and ctrl-a
40 11ctrl-a --> 51
40 -10ctrl-x --> 30

but! number with 0 e.g 007 it is 8-char(octal numeric system) system, and then
007 + 001 = 010(in 8-char sys) 010 --> means 8

:set nrformats=  # that option interpret all number in 
                 # 10-char(decimal numeric system) system

#71 del into insert mode, and into bash

ctrl-h  # del a char to the left of cursor

ctrl-w  # del a word to the left of cursor

ctrl-u  # del a part of string to the left of cursor

#72 one bullet for command 

insert mode, write text...
ctrl-o (and zz e.g.)  # up screen

#73 insert buffer one time insert mode

insert mode, write text

ctrl-r + buffer(a-z, 1-9)
# and how yanked?

#74 arithmetic calculations

write:
 6 clutches, each costing $12, total $
then:
ctrl-r=  6*12enter
result:
 6 clutches, each costing $12, total $72

#75 insert unicode and ad hoc characters

in insert mode:
ctrl-v + 123  # three characters

ctrl-vu + 1234 or 99bf # unicode „ø È¶ø

# if you need asc what the symbol in this text - put cursor on the ??? 
# and insert <ga>

ctrl-k + 12  == ‚Ω  # for both symbols(digraphs)
ctrl-k + bo  == „Åº
ctrl-l + v%  == é
:digraphs
:h digraph-table  # all digraphs

#76 visual mode

v - one char

v - string

ctrl-v - block

gv - repeat last 

o - go to brink visual block

gn - after search ?something visual it

# receipte how change visual block
start visual
vbb  # go to words back, but start not there where need
o  # leap to another brink
e  # go to better start place

#77 settings for python

:set shiftwidth=4 softtabstop=4 expandtab

#78 how check word inside symbols?

<a href="#">one</a>  # for one

vit  # visually inside the tag
u  # change lowercase to capital 

# and there for non visual analog
guit  # change lowercase to capital
j.
j.

#79 how to make a table with lines
first we have a table without lines g.e:

chapter            page
normal mode         15
insert mode         32
visual mode         88

then:
go cursor to the empty place between colones
ctrl-v3j  # empty vertical block for del empty space
x...  # del empty space
gv  # repeat vertical block
r|  # change empty block to the vertical line
yyp  # copy first string and past it for not empty pattern( make dublicate)
vr-  # change not empty pattern to the horizontal line

result:

chapter    |  page
------------------
normal mode|  15
insert mode|  32
visual mode|  88

#80 change the collone in the table

ctrl-v, move the cursor to visual collone
c  # change
print new words
esc
result:
all words in collone is changed to new words

#81 visual block text with not equal strings
ctr-v jj$  # to the end of strings

# and add ; to the end of string

a;  # go to end of string (or text object) and add semicolon
esc
result:
all strings with ; to the end.

#82 normal cmd

# how to add ; to every string in a visual block
make diapazon in visual mode:
jvg
and then press colon<:>
:'<,'>normal .
result:
<;> semicolon will be end of every string of visual block

#83 how to add ; to every string to whole file
:%normal a;

:%normal i#  # comment every string in file

#84 autocomplete to ex-mode

:col ctrl-d  # autocomplete variants
colder    colorscheme

:colorscheme ctrl-d
blackboard desert morning shine etc.

or <tab>  # for autocomplete variants, step by step

#84 open command line for ex-mode

q:  # open list of last commands
:q  # exit from list command line
ctrl-f  # change list of commands

#85 start bash into vim

:shell  # start
$ exit  # go back to vim

ctrl-z  # vim to sleep and go bash
$fg  # go back to the vim

#86 sort and filtering

firtst name, last name, email
jane,doe,jane@example.com
drew,neil,drew@vimcasts.org
john,smith,john@example.com

:2, $!sort -t',' -k2  # sort from 2 str to end, delimeter is <,>, for 2-d colone

# insert cursor place to ex-mode comand line, if you need from cursor to the end of file
!g  # :.,$!  and then add filter to the exclamation mark, e.g. <sort>

#87 make a vim script file

touch file jill.vim
write strings of commands into file
:source jill.vim

# for many files
:args
vim/file1.html vim/file2.py vim/file3.txt
:first
:source file1.html
:next
:source file2.py
or

:args
vim/file1.html vim/file2.py vim/file3.txt
:argdo source batch.vim  # fulfil for all files targeted in :args

#88 buffers

:ls # how many files in buffers now?

ctrl-^  # go to another file in buffers

:bprev or :bp # go to previous file
:bnext or :bn # go to next file

:bfirst  # go to first in stack
:blast  # go to last in stack

:buffer 2  # go to buffer #2
or
:buffer {bufname} # :buffer ji for jill.vim, or use tab for autocomplete name

:bufdo  # for all files

:bdelete n1 n2 n3  # delete buffers
or
: n, m bdelete
:5,10bd  # del buffers form 5 to 10
:bd 5 6 7 9 10  # del and not touch buffer 8

#89 change working directory into vim-window

:pwd  # print working directory
:lcd  # look current dir
:lcd /one/two/three/  # change working directory for current window
:windo lcd /one/two/three  # define working dir for all windows in this tab

#90 work with vim-tabs(not terminal-tabs)

:tabe[dit] {filename}  # open filename in new tab

ctrl-w t  # move current window to new tab

:tabc[lose]  # close current tab and there all windows

:tabo[nly]  # close other tabs

2gt  ------------# go to second tab
or :tabn[ext] 2  # go to second tab

gt  ---------------# go to backward
or :tabp[revious]  # go o backward

:tabmove 0  # go tab to the top of stack
:tabmove    # go tab to the bottom of stack

#91 open vim file manager netrw

:edit.
:e .  # open file manager for current dir

:explore  # open file manager for current buffer
:e

:sexplore  # new horizontal window
:vexplore  # new vertical window

ctrl-w c  # exit

if you open file manager uppon file 
ctrl-^  # back again to file

#92 move to screen strings
gj  # down
gk  # up
go  # first symbol
g^  # first symbol but not space
g$  # end

#93 move word by word

w, b  # start word
e, ge  # end word

w, b  # for complex word (e.g. we're - one word)
e, ge  # ~

#94 find comma and delete all before dot.

i`ve been expecting you, mister bond.
f,
dt.
i`ve been expecting you.

#95 del chunk of text

v  # go to visual mode
/pattern  # find from cursor to word
hjkl  # little bit correct cursor if you need
d  # delete for example

#96 visual objects

print('hello, world')

va(  # visual with brackets ('hello, world')
vi(  # visual inside brackets 'hello, world'
if need more just add i[ or a' whethever   '

or
ci'  '# change inside quotes

#97 text objects

ciw  # change insice word
daw  # ~ plus one space
ciw  # change inside word object
daw  # ~ plus one space
cis  # change inside string
das  # ~ plus one space
cip  # change inside paragraph
dap  # ~ plus one empty string

#98 change curly brackets to square brakets

cursor on the first braket
dt{  # delete, find {
%  # go to another }
r]  # change } to ]
``  # go back to first {
r[  # change { to [

#99 go to previous place

:jumps  # list of places

ctrl-o  # back
ctrl-i  # forward

e.g.
:e jill.py  # open new file
ctrl-o  # go back to first file
ctrl-i  # go to new file again

:changes  # list of changes

g;  # go to the place of last changes
g,  # go to the place of before changes

`^  # go to place last insert mode
`.  # go to place last change

#100 go to the link of file

~/django2/knowlege/python/jill.py

gf  # go to file in address
ctrl-o  # go back to first file

#101 paths to find

:set path?  # how paths includes?

#102 global find (but you need include all paths for potencial find)

mh  # make global mark in current file

:vimgrep /dispotcher/ **  # find dispatcher in whole file system

`h  # go back to first file with yuor sessioned mark

#101 work with registers(temporary buffers)

"ayiw  "# copy current word into register 'a'
"bdd   "# delete another current string and save it into register 'b'
"ap    "# insert word from 'a' register to new place
"bp    "# inset string from 'b' register to new place

#102 quote0(register) vs nonamed<quote_quote>("")(register), yank vs cut

yiw  # yank word "one" into quote0 register(yank register?)
diw  # del/cut word "two" into nonamed register
p  # put - "two"
"0p  "# put "one"

# quote0 register with a-z registers

"ayiw  "# yank word into a quote0 register
"ap  "# put from 'a' quot0 register
:reg "0  "# show yank register

#103 "_ (black whole) register

yiw  # yank word "one"
"_diw  "# del/cut into black whole and don't touch nonamed("") register
p  # put from no touched register

#104 change places of two word
# how cnange places two parts or sentence?

fc  # find word [c]oax
de  # del/cut to buffer e
mm  # make mark m
ww  # go to two word 
ve  # visual edit and go to end of word
p  # put after cursor
`m  # go back to the mark m
p  # put before cursor

#105 copy one word and replace it another

yiw  # yank word
jww  # go to next word
ciw<ctrl-r>0 esc  # put from quote0 register

#106 copy/paste paragraph and put it after previous, cursor ready to write.

yap  # yank a paragraph
gp  # put paragraph after previous paragraph, and move cursor to position for ready to write.

#107 system cut/paste

ctrl-c  # system cut
ctrl-shift-v  # system paste

#108 macros

qa  # start recording into 'a' register
a;<esc>  # add semicolon
ivar <esc> # add 'var'
q  # stop recording

# check register 'a'
:reg a

# enter macros
@a  # enter marcos 'a' from cusor place
or
@@
or 10@a  # ten ones repeat

# example for add spaces around '+'

x = "("+a+", "+b+", "+c+", "+d+", "+e+")";
f+  # find '+'
s + <esc>  # substitute '+' to space'+'space
qq;.q  # qq - start writing macro into q register,';'- go to next,'.'-  repeat last comand, 'q' - stop write marcro
22@q  # repeat marcor 22 ones, but need 10, in error that marcos stoped
result:
x = "(" + a + ", " + b + ", " + c + ", " + d + ", " + e + ")";

#109 change dots to brackets and make capital leters
1. one
2. two
3. three
4. four

qa  # start write macros to 'a' register
0f.  # go to start string and find '.'
r)  # change '.' to ')'
w~  # chnage word to first capital leter
j  #
q  # stop writing macros
3@a  # third fulfil 'a' macros3@a  # third fulfil 'a' macros3@a  # third fulfil 'a' macros
result:
1) one
2) two
3) three
4) four

#110 parallel work of macros

qa  # start marcos to 'a' register
0f.r)w~  # change dot to bracket and change to capital letter
q  # stop writing macros

#111 change macros aftre writing

:reg a  # for 'a' register
qa  # append to end of macros
j  # add move
q  # stop macros

# 112 macros with iterator

from:
partridge in a pear tree
turtle doves
french hens
calling birds
golden rings

to:
1) partrige in a pear tree
2) turtle doves
3) french hens
4) calling birds
5) golden rings
"""
:let i=0  # def variable 'i'
:echo i  # check value of variable
0

:let i += 1  # increase value
:echo i  # check
1
"""
:let i=1
qa
i<c-r>=i<cr>)
<esc>
:let i += 1
q

go cursor to start position
jvg  # all text
:'<,'>normal @a  # go macros for all text

#113 amend macros

:put a  # change the macros as simple string
change string --> i=irÄ˝aÄ˝aÄ˝a:let i Äkb+= 1
0  # go to start string
"ay$  "# insert macros to register
dd  # del from current text

#114 patterns about

add into pattern:
\c  # for on upper/lower case filling in pattern
\c  # for off u/l case filling

#115 new regular expression

#\([0-9a-fa-f]\{6}\|[0-9a-fa-f]\{3}\)  # old style with shielding

/\v#([0-9a-fa-f]{6}|[0-9a-fa-f]{3})  # search 16-char codes of color
or
/\v#(\x{6}|\x{3})  # the same

# how to search a.k.a.?

/a.k.a  # nope, backward and a.k.a.

/a\.k\.a\.  # ok, old style

/\va.k.a.  # new style

?\v  # for exactly search
\v  # for regular expression, abbrogate meaning special characters

#116 how to find repeated words e.g i'm the the man

/\v<(\w+)\_s+\1>

()<--\1
()()<--\1\2
()()...<--\1...\9
()()()...<--\0  for all reg ex

< >  # that's a start and end of word, if you need <the> and not they, there
g.e. 
/\v<the>  # search <the>, but not they

\_s  # that's a spaces and new lines

#117 search/find word under cursor

shift-*  # forwarc search word under cursor
shift-#  # backward search word under cursor
or
g*
g#

#118 how not include quotes in search?

?\v"[^"]+"  "# with quotes
?\v"\zx[^"]+\ze"  "# without quotes
or
?\v"@<=[^"]+"@=  "#

#119 how to insert cursor to end of searches result?

/example/e  # search and put cursor to the end of result
if you not know 
/example  # simple search
//e  # and then put cursor to the end of result if you need

#120 how to change Xhtml to XHTML?

/\VX(ht)?ml\C  # find without register fillings
gUgn
n
.
n.
.

#121 how count results
/\example\
:%s///gn  # how much results
or
/\example\
:vimgrep //g %
:cnext
:cprev

#122 Replace fields in .csv file

last name,first name,email
neil,burgh,few@bumbshell.org
dou,hores, johnathan@escrow.com

/\v^([^,]*),([^,]*),([^,]*)$  # for three fields, all symbols without comma

:%s//\3,\2,\1  # replace fields 1,2,3 to 3,2,1

#123 Change html headers: <h2> to <h1>, <h3> to <h2>, arithmetic work

/\v\<\/?h\zs\d  # <?h from start digital

:%s//\=submatch(0)-1/g  # minus 1

#124 Replace both words

The dog bit the man.

:let swapper={"dog":"man","man":"dog"}  # make a dict
:echo swapper["dog"]
man
:echo swapper["man"]
dog

/\v(<man>|<dog>)  # find both words

:%s//\={"dog":"man","man":"dog"}[submatch(1)]/g

#125 Change words into many files of current dir

/work\ze with  # change only work word
:vimgrep // **/*.py  # find in current dir

:vimgrep /about/g jill.py forcword.py clock.py # find 'about' in files for all results
or
:vimgrep /about/g *.py # for .py files
or first make args and then first between them
:args *.py
:vim /about/g ##

# find in file and then find global
/[Dd]on't  '# find in file
:vim //g *.py  # find in dir

:cnext, :cprev, :exit  # show all files how finded
or :5cnext

:cfirst, :slast

:cnfile, :cpfile  # go to first/last to next/prev files

:copen, :cclose or :exit or :q  # quickfix list of files how finded

:cc 11  # go to result 11

:cdo {cmd}  # cmd for all strings of quickfix list
:cfdo {cmd}  # cmd one time for all files in quickfix list

:colder  # undo for quickfix list
:cnewer  # redo for quickfix list

:set hidden  # for exit from changable files without write

:cfdo %s//job/gc  # change work to job with accnowlegments

:cfdo update  # for save changes
or
:cfdo %s//job/g | update

#126 Clarify html from tags

/\v\<\/?\w+>
:g//d

or another way hold tags and del other
:v/href/d  # :v == :vglobal (invert global)

#126 Set all comments

qaq  # clear register 'a'
:reg a

:g/chore/yank A
:reg a

open new window for write new file
"ap  "# insert comments into new file
or
:g/chore/t$  # add all chore comments to the end file

#127 Sort words into block

html{
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  font: inherit;
  vertical-align: baseline;
}

cursor on the {
vi{  # visual into { }
:'<,'>sort

:g/{/ .+1,/}/-1 sort  # sort all blocks into file

# make a spaces from a start strings into { } blocks

:g/{/ .+1,/}/-1 >

#128 spell checking

write, make an error:
Ctrl-x s  # change

:set spell
:set spelllang=en_us  # if you need US English

:set spell
:set spelllang=ru
Ctrl-x Ctrl-k

[s, ]s  # go/back by errors  ??? NOT WORKING
z=  # list of examples for change
zg  # add current word to dict
zw  # delete current word from dict
zug # undo delete or add to dictionary

#129 autocomplete fool line

ba
Ctrl-x Ctrl-l
result:
background-color: #ef66ef; 

