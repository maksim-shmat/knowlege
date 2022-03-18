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

#7 Read Only

vi -R jill.py

#8 Moving
0 - to start a string
$ - to end a string
b - up
2w - 2 right
hjkl, 2h, 2j, 2k, 2l

#9 Bookmarks

:mark  # Show me all of my bookmarks
:delmarks 2 zoru n-mark  # delete bookmarks
m bookmark_name  # set a bookmark

#10 Abbreviation

:ab inc Illigitimi Non Carborundum  # set an abbreviation
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
y  # yank, and with num some
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

# Search
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
