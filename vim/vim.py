"""All about vim."""

# first $ touch ~/.vimrc
# an then $ touch ~/.exrc
# .exrc for /home/ is global
# .exrc local for special dir (special for prog, or special for writing, with special options how change global .exrc options)
:version  # how function is available in your version
:help  # read documentation

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

#5 If ''' is trubles roll page from up to down

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

44G  # go to 44 string
10ENTER  # go to 10 string down

``  # go to previous place
''  # go to previous place on the start string

#9 Bookmarks

:mark  # Show me all of my bookmarks
:delmarks 2 zoru n-mark  # delete bookmarks
m bookmark_name  # set a bookmark

# temporary marks (for current seance)
mx  # mark [x], or eny leter
'x  # 'go to start string with mark
`x  # go to mark where is it
``  # go to previous temp mark
''  # go to start string on the previous temp mark


#10 Abbreviation

:ab inc Illigitimi Non Carborundum  # set an abbreviation
and then just write inc for print full name
:una inc  # unset the abbreviation

#11 Autocomplete

- write word multiple times, e.g. Antarctica
- type Ant and then use Ctrl+N (or Ctrl+P)

#12 work with numbers of lines

:2, 10d  # delete lines 2 through 10

:25, $d  # delete every line from line 25 to the end of the file

:%d  # delete every line

:5, 10t 15  # copy lines from 5 through 10 and insert it after line 15

:5, 10m 15  # move lines from t threugh 10 and insert it atrer line 15

#13 Wrapmargin - how many characters into string

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

#14 Moving on the text

w or W(without punctuation)  # (word) move by one word to the right
b or B(without punctuation)  # (word) move to backward
2w and 2b
e or E(without punctuation)  # go to end word

(  # go to start this sentence.
)  # go to start next sentence.

{  # go to start current block
}  # go to start next block

[[  # go to start current paragraph
]]  # go to start next paragraph

3)  # got to through 3 sentences
d)  # del from cursor to end sentence
2y}  # yanked two next block

Ctrl + o  # takes your back to older position
Ctrl + i  # to newer position

%  # on the braket go to another one braket, from ( --> )

#15 Moving with G

1G  # Start page
42G  # string n.42
G  # Go to the bottom
gg  # Go to the top
+  # Go to first new line
-  # Go to first backward line

#16 Redaction

a  # append, with num
c  # change, with num
d  # delete, with num
p  # put, with num
y  # yank
s  # substitute, add simbol (or both with 2s) 
S  # substitute whole string
R  # replace
I  # insert
O  # open

~ or 22~  # change register

cw  # change word
c2b  # change word to backward on the two words
c0  # change words to the start of string from cursor  (but cc ?)
c$ (equal C)  # change words to the end of sting from the cursor (but cc ?)
cc  # change string
C  # change from cursor to the end string

#17 Delete

dw  # delete word from cursor, with whitespace
de  # delete word from cursor, without space
2dd  # delete two strings
D == d$  # delete string from cursor to end string

x  # delete char to rite from cursor
X  # delete char to left from cursor
2x and 3X  # etc.

:%d  # del all into file

#18 P - put

first d or vd  # deleted text save to 'put' buffer
p  # and then p to put text from buffer in a new place
   # or paste after string where is cursor

P  # big P - put text befrore cursor
   # or paste before string where is cursor

#19 replace two char

in the word mvoe place cursor to v
and xp  -> move

#20 Yanked - copy to buffer

y  # copy after cursor
3yk  # copy 3 string to up
3y  # copy 3 string to beneath
y$  # copy string from cursor
yw  # yank word
yy or Y  # copy string

#21 Amalgamate strings

With a
screen editor

J  # amalgamate both string
or 2J
With a screen editor

#22 Screenscrolling

^F  # down screen
^B  # up screen
^D  # down halfscreen
^U  # up halfscreen
zENTER  # down one screen
200zENTER  # go to 200 line
z.  # this line to center of screen
z-  # this line to bottom of screen

#23 Reload screen for remove sys message

^L  # reload page

#24 Steps into one screen

H  # go to up
M  # go to center
L  # go to bottom
3H  # go to 3 lines to up
4L  # go to 4 lines to down

^  # go to first not empty char in string
3|  # go to 3 |1|2|3<-

#25 Search
	?ENTER  # repeat last search
	/ENTER
	or n, N  # after exit insert mode

	d?spam  # del text from cursor to the word spam

	fx  # find and move on new [x] simpol in the string

	;  # repeat fx
	,  # repeat fx to backward

	dfx  # del all before [x] from cursor, del with [x]

	tx  # find [x] but cursor before [x]
	dtx  # del [x] but not include [x]
        
        :set ic  # set ignore case
        :set noic  # unset ignore case
        :set hls  # highlite search results
        :set is  # incsearch, show partial matches for a search phrases

#26 Open file with pattern
$ vi +/pattern file
or POSIX(Linux) style -> $ vi -c/pattern file
for pattern with spaces use -> $ vi +/'pat tern' file
                               $ vim -c/pat\ tern file
For ease use your own pattern e.g MARK, and then find your pattern.

#27 List all swap files

$ vi -r

#28 Save file to buffer

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
"Zy)  # "add new sentence to 'z' buffer

# work with @-functions of buffer

just write in a text field:
cwbubsyexample^[  # that means cw bubsyexample CTRL-V ESC
then del and move it to the buffer:
"gdd    #"
and then go to start a word, and replace it with buffer
@g
result: word -> bubsy^[
emmm...

# past from named buffer

"dP  # "put buffer 'd' before cursor
"ap  # "put buffer 'a' after cursor

#32 Workd with ex

:6  # got to sixths string

:3, 18d  # del strings in diapazone from 3 to 18

:160, 224m23  # move strings from 160 to 224 -> 24str

:23, 29co100  # copy from 23 to 29 and insert afer 100str

;  # mean current, with number of str, else (if ,)cursor place current
:100; +5 p  # from 100 +5 str print

#33 global find

:g/pattern  # find and go to words with pattern
:g!/pattern  # find and go to words without pattern
:60, 123g/pattern/p  # into diapazon

#34 Combined commands with pipe

:1,3d | s/thier/their/  # del and then rewrite

:1,5 m 10 | g/pattern/nu  # move and then view str with pattern and num str

#34 Save as new file with new name

:w newfile.py

:230,$w newfile.py  # save from 230 string into newfile

:.,600w newfile  # save from current to 600 into newfile

:1, 10w newfile  # thats both commands make two insertions into file
:340, $w >> newfile

#35 Read another file from opened file with vim

:read filename  # inserted core file into current place of cursor
:r filename
:r /home/time/data
:$r /home/tim/data

:185r /home/tim/data  # insert after 185 str

:/pattern/r  /home/tim/data  # insert after pattern str

#36 Open both or more files.

$ vi file1 file2
:args(or :ar)  # how many files was open
:rewind(or :rew)  # change to first file in a list
:last  # change to last file in a list of files
change file1
:w  # save file1
change file2
:x  # save and quit
:e!  # or remove all changes

#37 Open more files from one's opened

open file1 and then
:e file2
CTRL+^  # go to previous file

#38 Global substitutes

:s/old/new/
:s/old/nen/g  # g is global
:50, 100s/old/new/g  # substitute from 50str to 100

:1, $s/old/new/g  # substitute in all file
:%s/old/new/g  # substitute ina all file
:%s/old/nes/gc  # g - global and c - confirm all changes
:e!  # remove old version from buffer i.e remove changes

:g/pattern/s/old/new/g
:g/<body>/s/of/on/g  # target substitute of pattern

:g/editer/s//editor/g  # both equivalent
:%s/editor/editor/g

#39 Regular expression for vim

  - any symbol (p.p = pip, pep etc)
*  - bugs* = bugss, bug, bugs, bugsss etc
^  - ^Part = Part at the begining a string, else ^ is carret
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
\I - any symbol from isindent, but without numbers

\k - any keyword from iskeyword
\K - any keyword but witout numbers

\f - any filename from isfname
\F - any filename from isfname, but without numbers

\p - any printable symbol
\P - but without numbers

\s - spaces with taps
\S - All that not spaces and tabs

\b - backspace

\e - escape

\r - carret

\t - tab

\n - ???

~ - last changeble string



[ ] - [AB] = A or B, p[aeiou]t = pat, pet, pit, pot, put

/[Tt]he = The or the

[^0-9] = that carret means - NOT, anybody but not number
[[:alpha:]!] = a, l, p, h, or !
[[.ch.]] = ch only, but not c and h
[[=e=]] = e, franch e with`, and other e deviation

[:alnum:] - char and num
[:alpha:] - Alphabetical symb
[:blank:] - space and tab
[:cntrl:] - Control symb
[:digit:] - num only
[:graph:] - all visual symb, without spaces or tabs
[:lower:] - lowercase
[:print:] - printable symb, with spaces etc
[:punct:] - punctuation symb
[:space:] - space symb
[:upper:] - upercase
[:xdigit:] - sixteenth num

\( \) - save to the buffer, \(That\) or \(this\) = That to buffer1, this to b2
:s/\(That\) or \(this\)/\2 or \1/  # changing to this or That (result: this or That)
:s/\(That\) or \(this\)/\u\2 or \l\1/  # changing places and change low/up cases (result: This or that)

:s/\(abcd/)\1/alphabet-soup  # changeing abcd to alphabet-soup

\< - start of word, \<ac = action
\> - end of word, ac\> = maninac

& - same name, :%s/Cuchinski/&, Zax/ = :%s/Cuchinski/Cuchinski;, Zax/
:1, 10s/.*/(&)/  - make ->(every str into brakets)<- from 1-10 str

\u - Upercase, :%s/yes, doctor/\uyes, \udoctor (result: Yes, Doctor)
\l - Lower Case 

\U, \L - UPPER/LOWER CASES 
:%s/Fortran/\UFortran/  (result: FORTRAN)
:%S/Fotran/\U&/  (same)

-----------------------
# Case1: change child to children, with the same punctuation
# In the text is: child , child, child,, child., etc
# And we need is: childred , children, children,, children., etc
:%s/child\([ ,.;:!?]\)/children\1/g  # \( \)-save to buffer1 punctuation
:%s/\<child\>/children/g  # That is for not change words as Fairchild
-----------------------

# Case2: change half word
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

#Case3: move paragraphs
.Rh "SYNTAX"  # name of paragraphs
blahblah.
.Rh "DESCRIPTION"
blah
blah.
.Rh "PARAMETERS"
blah
    blah.

:g /SYNATX/.,/DESCRIPTION/-1 move /PARAMETERS/-1  # -1 for print 1str down
result:
DESCRIPTION go up above SYNTAX

# ir need del paragraph\

:g/DESCRIPTION/.PARAMETERS/-1d

#Case4: change double spaces to one space
:%s/  */ /g

#Case5: change one or more spaces after . or : to two spaces
:%s/\([:.]\)  */\1  /g

#Case6: del all empty strings
:g/^$/d

#Case7: del all empty and tab-tab or space-space strings
:g/^[ tab]*$/d
:g/^[ tab][ tab]*$/d

#Case8: del all spaces on the start string
:%s/^  *\(.*\)/\1/

#Case9: del all spaces on the end string
:%s/\(.*\)  *$/\1/

#Case10: Insert [  >] into start all strings
:%s/^/>  /

#Case11: Add . to end next six strings

:.,+5s/$/./

#Case12: change parts of sentens between defice ->[-]<-

:%s/\(.*\) - \(.*\)/\2 - \1/

#Case13: change all leters on the UPERCASE

:%s/.*/\U&/  # faster
:%s/./\U&/g  # little bit slower

#Case14: Reverse positions of strings
:g/.*/mo0
:g/^/mo0

#Case15: Where is not typing "Paid in full" print "Overdue"
:g!/Paid in full/s/$/ Overdue/
:v/Paid in full/s/$/ Overdue/

#Case16: Every string not start with number move to end of text

:g!/^[[:digit:]]/m$
:g/^[^[:digit:]]/m$

#Case17: Remove numbers into head of paragraphs, from start of strings

:%s/^[1-9][0-9]*\.[1-9][0-9.]* //

#Case18: Change word Fortran to FORTRAN (acronym FORmula TRANslation)

:%s/\(For\)\(tran\)/\U\1\2\E (acronym of \U\1\Emula \U\2\Eslation)/g

#Case19 Make 10 copies 12-17 str to end file
:1,10g/^/ 12, 17t$

#40 :set

:set all  # list all settings

:set laststatus=2  # show status: filename [+], strings amount, percentage.
:set laststatus=1  # off show status

#41 vim and UNIX

:!date  go to bash, see date, press Enter, and go back to vim

:sh  # go to bash, Enter, back vim

:r !sort jill.csv  # open file, sort and write info from jill.csv

:!ls  # go see how named files in current dir
:r filename

:16,19!sort  # sort strings from 16-19

cursor to 16 string and 5!!sort  # sort from cursor 16str-19
or !5!sort

go cursor to the string for change cases
!)  # then write for change lower to upper cases
tr '[:lower:]' '[:upper:]' ENTER

#42 map

e.g. change places two word 'the' and 'scroll', in the sentence 'you can the scroll page'
cursor on to 'the'
dwelp  # dw - del word, e - go to end next word, l - move to one space to right, p - put del word
then map it command
:map v dwelp  # v is used in vim, use another button!
touch v for change plces any two words

#43 Prefixes

vim -o file1 file2 - open all files into same windows, or open empty window if files less than
or vim -o5 file1 file2 - two windows is visual and three is hiden

vim -O file1 file2 - open all into vertical windows

-z - closed mode, without bash support or other helps
# and [rvim] same, with stop seans since ^Z

#44 Remote server commands vith vim...

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

#45 Where am I?
Ctrl + G  # number of current string and path to file

#46 Completition text or command
first type e.g. :e
then tap Ctrl + D

#47 Through the windows

Ctrl + w + w
Ctrl + w + j (down)
Ctrl + w + b (bottom)
Ctrl + w + t (top)

#48 Jump to a subject

Position the cursor on a tag (e.g. |bars|) and hit CTRL-].
Jump back:  Type CTRL-O.  Repeat to go further back.

#49 Split windows

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


# change places of windows

Ctrl-w r  # to -->
Ctrl-w R  # from there <--
Ctrl-w x

# change size of windows

Ctrl-w =  # coequal

:resize -4  # decrease window onto four lines
:cmdheight  # for resize bottom ex-window
:verticalresize n

Ctrl-w >,<  # change width
Ctrl-w |  # default width

z22  3 set window 22 lines

#50 Tags open tag into new window

open :help
write any tag e.g "bars"
type:
:stag! bars  # article "bars" will be opened in a new window

#51 Open file under the cursor(link?) into new tab
^Wgf
^WgF  # and cursor after filename

#52 Open file in a new tab

:tabnew jill.py
or :tabnew  # empty file

:tabclose  # close current tab
:tabonly  # close all another without this tab

Ctrl + PgUp, PgDn  # change tab in terminal

#53 [+] Convolution

zA, za - change all, one
Zc, zc - close all, one
zD, zd - del all, one
zE - del all
zf - make convolution from cursor line to move cmd
countzF - make conv from curlor line to count lines
zM - foldlevel opetion == 0
zN, zn, zi - foldenable option on/off
zO, zo - open conv all(enclose), one
zj, zk - move cursor to next conv
zm, zr - -1 or +1 foldlevel option

3zF - convolution three lines
or 2zfj - conv two lines down
zfgg - conv whole file if cursor is bottom

:set foldcolumn=n  # set suggestions enclose convolution about

:set foldmethod=indent  # convolution with parameters of strings
:set shiftwidth=4  # check tabulation for indent
:set foldlevel=2  # deep view in convolution
:set foldlevel=0  # only headers

then (zr) (zm) - open/closed

#54 Autofoldering prog.lang.

set foldcolumn=3
zE - remove all previous folders

:set foldenable
:set foldmethod=syntax

#55 Autocomplete

:imap Tab <C-P> - autocomplete to Tab e.g.

Ctrl-x Ctrl-l - autocomplete whole string
Ctrl-n, Ctrl-p - up/down in list of variants
and Ctrl-e - esc

Ctrl-x Ctrl-n - autocomplete with keyword

Ctrl-x Ctrl-k - autocomplete with dictionary

Ctrl-x Ctrl-t - autocomplete with tesaurus

Ctrl-x Ctrl-i - autocomplete with include files

Ctrl-x Ctrl-] - autocomplete with tags

Ctrl-x Ctrl-f - autocomplete with filename

Ctrl-x Ctrl-d - autocomplete with macros name

Ctrl-x Ctrl-v - comand line completition

#56 Digraphs for diacritics marks

Ctrl-k c , = ç
Ctrl-k c . = ċ
Ctrl-k a ! = à

# Greec

Ctrl-k p * = π

# ?

Ctrl-k ?I = ¿

Ctrl-k ss = ß

# digraphs with set digraph

:set digraph

c Backspace , = Ç
A BS ! = à
- BS = == ¯ UPPER SCORE, or UPPER DASH

' Bs ' = ´
( Bs a = ă
< Bs a = ǎ
, Bs c = ç
> Bs o = ô
! Bs a = à
- Bs o = º
a Bs - = ā
o Bs / = ø
? Bs n = ñ
: Bs e = ë

:digraph  - list of digraphs

#57 Show dir/files and edit files in another window

o - open file

#58 Make .html from .txt

go to jill.txt
write:
:runtime!syntax/2html.vim  # make entire file

:25, 44TOhtml  # make chank file

#59 Difference

$ vimdiff old_file new_file
or
$ vim -d old_file new_file

#60 Undo/redo

:2undo or 2u

:3redo or 2Ctrl-R

#61 fast change two symbols
xp - erdo --> redo

#62 Fast change two sentence

ddp - up sentence to down

#63

#62 Fast change two sentence

ddp - up sentence to down

#63

#62 Fast change two sentence

ddp - up sentence to down

#63

#62 Fast change two sentence

ddp - up sentence to down

#63

#62 Fast change two sentence

ddp - up sentence to down

#63

#62 Fast change two sentence

ddp - up sentence to down

#63

#62 Fast change two sentence

ddp - up sentence to down

#63

#62 Fast change two sentence

ddp - up sentence to down

#63

#62 Fast change two sentence

ddp - up sentence to down

#63 window last commands
:Ctrl-F
exit from window:
Ctrl-C

#64 If you traped in :ex mode

Q - move you to :ex mode
write:
:vi  # go out from :ex mode

#65 Join short sentence

J or 3J

#66 Add spaces around plus

f+  # find + in sentence, if need find to backward press - ,
s + <Esc>  # rm + and add space, plus, space, esc
;  # find next plus
. repeat

#67 Fast find

cursor on the word
*
n,n

#68
