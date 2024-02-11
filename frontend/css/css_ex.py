"""CSS about."""


#1 Media queries
@media screen and (max-width: 600px) {
	/* Styles for screens with a width of 600 pixels or less */
}

#2 Breakpoints
@media screen and (max-width: 480px) {
	/* Styles for small screens (e.g., mobile phones) */
}

@media screen and (min-width: 481px) and (max-width: 768px) {
	/* Styles for medium screens (e.g., tablets) */
}

@media screen and (min-width: 769px) {
	/* Styles for large screens(e.g., desctops) */
}

#3 Flexbox for menus, form control and layout items
.flex-container {
	display: flex;
	justify-content: space-between;
}

.flex-item {
	flex: 1;
}

#4 Grids
.grid-container {
	display: grid;
	grid-template-columns: repeat(3, 1fr);
	grid-gap: 10px;
}

.grid-item {
	grid-column: span 2;
}

#5 Connect css to Html
#a
<link rel="stylesheet" type="text/css" href="sheet1.css" media="all">  # or other files

#b
<style type="text/css">
@import url(sheet2.css) all and (min-resolution: 96dpi);
@import url(blueworld.css) screen and (color-depth: 8);
@import url(Djanny.css) projection, print and (color) and (orientation: land scape) and(min-device-width: 800px), handheld;
@import url(http://example.org/library/layout.css);
body {color: red;}
h1 {color: gray;}
</style>

#6 link(rel, type, href, media, title)

rel="stylesheet"
type="text/css"
href="http://mysite.com/sheet1.css"
media="screen, projection"
title="Default" or "Big Text", or "more something"  # for different file.css, and for group files.css use one title name
# if title is than it default

#7 style for HTML

<p style="color: maroon;">Бордовый цвет. The most wonderful of all breackfast foods</p>

#4 Comments in CSS, from C/C++

/* Comments
in css */

<style type="text/css"><!--
h1 {color: maroon;}
body {background: yellow;}
--></style>

#5 supports

@supports (color: black) and ((display: flex) or (display: grid)) {
        div#main {display: grid; grid-gap: 1em 0;
        overflow: visible;}
        div#main div.column{margin: 0;}
}

#6 Classes

<p class="warning">...</p>  # Declaration
<p>...<span class="warning">...</span>  # string into paragraph

.warning {font-weight: bold;}  # Short call
p.warning {font-weight: bold;}  # for paragraphs 
span.warning {font-style: italic;}  # for span element

#7 Combine classes

<p class="urgent warning">blah-blah-blah.</p>
<p>blah-blah, <span class="warning">blah-blah</span>.blah-blah.</p>

.warning {font-weight: bold;}  # for one
.urgent {font-style: italic:}  # for other
.warning.urgent {background: silver;}  # for both

#8 # - selector id, * - for all elements

*#first-para {font-weight: bold;}  # bold for all elements with id=first-para
#lead-para {font-weight: bold;}  # without * all the same

#9 selectors with half value

[foo|="bar"]  # start with bar plus [-]
[foo~="bar"]  # bar between spaces
[foo*="bar"]  # bar into
[foo^="bar"]  # start with bar
[foo$="bar"]  # end with bar
------
*[lang|="en"] {color: white;}   # Rule for change color

<h1 lang="en">Hello!</h1>       # Yes change color this
<p lang="en-us">Greetings!</p>  # Yes
<div lang="en-au">G`day!</div>  # Yes
<p lang="fr">Bonjour!</p>       # No
<h4 lang="cy-en">Jrooana!</h4>  # No
------
img[src|="default"] {border: 1px solid gray;}  # rule for format files
default-1.gif  # Yes
default-2.gif  # Yes
default-3.gif  # Yes
------
Against "btn btn-small btn-arrow btn-active"
Use
*[class|="btn"] {border-radius: 5px}
<button class="btn-small-arrow-active">Шёлкни тут!</button>

#10 Formatting with keywords and tilde for all elements

p[class~="warning"] {font-weight: bold;}  # for all with 'warning'
span[class~="barren"] {font-style: italic;}  # for all with 'barren'
img[title~="Figure"] {border: 1px solid gray}

#11 Formatting with keyword and asterisk only for class-keyword

span[class*="cloud"] {font-style: italic;}  # Rule with *

<span class="barren rocky">Mercury</span>  # No
<span class="cloudy barren">Venus</span>   # Yes formatted
<span class="life-bearing cloudy">Earth</span>

# e.g. format all links with juja.com

a[href*="juja.com"] {font-weight: bold;}

# format all img with "space"

img[src*="space"] {border: 5px solid red;}

# format for input

input[title*="format"] {background-color: magenta;}  # Rule for CSS

<input type="tel"
  title="Telephone number should be formatted as XXX-XXX-XXXX"
  pattern="\d{3}\-\d{3}\-\d{4}">

#12 Formatting with keyword and caret for start element

a[href^="https:"] {font-weight: bold;}
a[href^="mailto:"] {font-style: italic;}

#13 Formatting with keyword and dollar sign for end element

a[href$=".pdf"] {font-weight: bold;}

img[src$=".gif"] {...}

#14 for all registers

a[href$=".PDF" i]  # for .pdf, .Pdf, .PDF

planet[type*="rock" i]  # Rule CSS

<planet type="barren rocky">Mercury</planet>     # Yes
<planet type="bloudy ROCKY">Venus</planet>       # Yes
<planet type="life-bearing Rock">Earth</planet>  # Yes

#15 sign <+> for first neighbor, sign <~> for second and more neighbors

h1 + p {margin-top: 0;}  # for next paragraph from h1

li + li {font-wight: bold;}  # for next two lists

html > body table + ul{margin-top: 1.5em;}  # for ul how after table, from body

h2 ~ol {font-style: italic;}  # for all next neighbors

#16 selectors pseudo class read from right to left

a:link:hover:lang(be) {color: gray;}
a:visited:hover:lang(be) {color: silver;}

:root {border: 10px dotted gray;}  # border for all page

p:empty{display: none;}  # hide all empty elements in paragraph

<a [href] img:only-child {border: 1px solid black;}  # add border to img who is only one child and able link

<a [href] img:only-of-type {border: 5px solid black;}  # add border to imb/link who is one child against neighbors

p:first-child {font-weight: bold;}  # for first child,
#read from right to left, first p element as a child in other parent(div e.g)
li:first-child {text-transform: uppercase;}  # for first child as list in other parent

:last-child  # be
 
# Pseudo class not the same as class, :first-child != class="first-child"

table:first-of-type {border-top: 2px solid gray;}  # for first elements in table who(table) included in parent
td: first-of-type {border-left: 1px solid red;}  # for first elements of table

:last-of-type  # be

#17 Selectors for numerical elements

p:nth-child(1) {font-weight: bold;}  # for first paragraph and first element in it.

li:nth-child(1) {text-transform: uppercase;}  # in list

ul > li:nth-child(3n + 1) {text-transform: uppercase;}  # for first(default) and fourth(3n + 1), where n = 0,1,2,3,4, and in total result = 1,4,7,10,13

:nth-child(2n+1) or :nth-child(odd)  # for odd numbers
:nth-child(2n-1) or :nth-child(even)  # for even numbers

tr:nth-child(odd) {background: silver:}  # for all second row in table

tr:nth-last-child(odd) {background: silver}  # for every second row but include last row strictly

#18 selector for numerical elements with one type

p > a:nth-of-type(even) {background: blue; color: white;}  # colored even second link in paragraph

#19 Links

a.external:link, a[href^="http"]:link {color: stateblue;}
a.external:visited, a[href^="http"]:visited {color: maroon;}

a#footer-copyright:link {background: yellow;}
a#footer-copyright:visited {background: gray;}

a:link {color: navy;}  # порядок имеет значение
a:visited {color: gray;}
a:focus {color: orange;}  # for active uses
a:hover {color: red;}  # if tuch it with cursor show something
a:active {color: yellow;}  # user will be this already

Выделение элемента формы в котором установлен курсор
input:focus {background: silver; font-weight: bold;}

#20 Enabled, disabled

:enabled {font-weight: bold;}
:disabled {opacity: 0.5;}

#21 Checked, indeterminate for radio buttons for example

:checked {background: silver;}  # ON
:indeterminate {border: red;}   # Shredinger
input[type="checkbox"]:not(:checked)  # OFF

# For change how look label
input[type="checkbox"]:checked + label {
        color: red;
        font-style: italic;
}
<input id="chbx" type="checkbox"> <label for="chbx">Подпись</label>

#22 Default

[type="checkbox"]:default + label {font-style: italic;}

<input for="chbx">Выставляется при загрузке страницы</label>

#23 Required, optional

input:required {border: 1px solid red;}  # red == #f00
input:optional {border: 1px solid blue;}  # blue==#ccc

<input type="email" placeholder="enter an email address" required>  # required
<input type="email" placeholder="optional email address">  # optional
<input type="email" placeholder="optional email address"   # optional
    required="false">

variant for css
input[required] {border: 1px solid red;}  # red==#f00
input:not([required]) {border: 1px solid blue;}  # blue==#ccc

#24 Valid, Invalid
# for fields input email address

input[type="email"]:focus {
        background-position: 100% 50%;
        background-repeat: no-repeat;
}
input [type="email"]:focus:invalid {
        background-image: url(warning.jpg);
}
input[type="email"]:focus:valid {
        background-image: url(checkmark.jpg);
}
<input type="email">

#25 In-range, out-of-range

input[type="number"]:focus {
        background-position: 100% 50%;
        background-repeat: no-repeat;
}
input[type="number"]:focus:out-of-range {
        background-image: url(warning.jpg);
}
input[type="number"]:focus:in-range {
        background-image: url(checkmark.jpg);
}
<input id="nickels" type="number" min="0" max="1000" />

# with step

input[type="number"]:invalid {color: red;}
input[type="number"]:in-range {font-weight: bold;}

<input id="by-tens" type="number" min="0" max="1000" step="10"
    value="23" />  # not valid by no step 10

#26 :target

*:target {border-left: 5px solid gray; background: yellow
        url (target.png) top right no-repeat;}

#27 :lang

*:lang(fr) {font-style: italic;}
*[lang|="fr"] {font-style: italic;}

#28 :not()

li:not(.moreinfo) {font-style: italic;}

.moreinfo:not(li) {font-style: italic;}

*:not(section) >table

*:not(thead) >tr>th

*.link:not(li):not(p) {font-style: italic;}

#29 !important, add only before semicolon, strictly

p.dark {color: whitesmoke !important; background: white;}

p.light {color: yellowgreen; font: smaller Times, serif !important;}

h1 {font-style: italic; color: gray !important;}
.title {color: black; background: silver;}
*background: black !important;}

<h1 class="title">NightWing</h1>

#30  inherit наследование

#toolbar {color: inherit;}

span {border-color: inherit;}

#31 initial, change for default value

font-weigh: initial
equals:
font-weight: normal  # default

#32 unset, inherit and initial as one key word

section {color: white; background: black; font-weight: bold;}
{all: inherit}  # for inherit all

section {color: white; background: black; font-weight: bold;}
{color: inherit; background: inherit; font-weight: inherit;}  # for not all inherit

#32
1fr fr - дробное значение, часть макета например.
---
10in - inches,

4.561pt - points  # 1in == 72pt, 18pt == 0.25in

4q - quadriple of millimeter  # 4q == 1mm

1.5pc - cicero or pickes  # 1pc == 12pt, 1in == 1pc

100px - pixels  # 100px != 100pc because screen difference

dpi -dots per inch
dpcm - dots per centimeter
dppx - dots per pixel unit  # 1dpx == 96dpi 2017year
@media (min-resolution: 500dpi)  # show if screen => 500dpi

px  pixels        1/96 of an inch
pt  points        1/72 of an inch
cm  centimeters   37.8px or about 0.4in
mm  millimeters   1/10 of a cm; about 3.8px
Q   quarter-mm    1/40 of a cm; about 1px
in  inches        96px; about 2.54cm
pc  picas         1/6 of an inch; 16px

#33 em, rem and ex, ch

em == font-size  # if {font-size: 14px;}, than 1em == 14px  # em is a tipographic width <m> letter

font-size: 1rem == change to default font-size how determine in browser # raw? width of <m> letter
or
font-size: initial

<p>This paragraph inherit font size from root element. What?.</p>
    <div style="font-size: 30px; background: silver;">
            <p style="font-size: 1em;">This paragraph show as parrent font element.</p>

            <p style="font-size: 1rem;">This paragraph inherit font size fron root element. But with parrent background.</p>
    </div>

ex  # is a tipographic height <x> letter

1ch -[0]  # ширина символа с боковыми отступами

# more css units

vm - viewport width unit (if screen width == 937px, then 1vm => 937/100 == 9.37px)

vh - viewport hight unit (if screen width == 650px, then 1vh == 6.5px)

vmin - viewport minimum unit (minimum screen width), if screen 937x650, then 1vmin == 6.5px
vmax - viewport maximum unit (maxinum screen width), if screen 937x650, then 1max == 9.37px

Use it for bind fonts with screen size
h1 {font-size: 10vh;}  # this font == 1/10 of screen size

Or use it for elements
div {width: 50vh; height: 33vw; background: gray;}

#34 Border
value1;  Aplies value1 to all four sides

value1 value2;  Applies value1 to the top and bottom and value2 to the right and left

value1 value2 value3  Applies v1 to the top, v2 to the right and left, v3 to the bottom

value1 value2 value3 value4  v1 - top, v2 - right, v3 - bottom, v4 - left

#Style:
    dotted
    dashed
    solid
    double
    groove
    ridge
    insert
    outset

# Asterisk <*> for everithing on the page
* {
        outline: 1px red dashed;
}

# border radius
aside {
        border: 1px solid black;
        border-radius: 50px 100px 10px;
}
it is equivalent:
aside {
        border: 1px solid black;
        border-top-left-radius: 50px;
        border-top-right-radius: 100px;
        border-bottom-right-radius: 10px
        border-bottom-left-radius: 100px;
}

# horizontal vertical border radius

div {
        border: 3px outset darkgreen;
        border-radius: 10px 20px;  # 10px horizontal, 20px vertical
}

or for details:
aside {
        border: 5px dashed red;
        border-top-left-radius: 50px 75px;
        border-top-right-radius: 100px 50px;
        border-bottom-right-radius: 75px 100px;
        border-bottom-left-radius: 50px 25px;
}

#35 margin  кайма?

aside {
        margin-top: 16px;
        margin-riht: 8px;
        margin-bottom: 32px;
        margin-left: 24px;
}

margin-right: auto;
margin-left: auto;

value1 - for all four sides
value1 value2 - v1 to the top, v2 right/left
value1,2,3 - v1 top, v2 right/left, v3 bottom
value1,2,3,4 - v1 top, v2 righ, v3 bottom, v4 left

aside {
        margin: 16px 8px 32px 24px;
}

#36 Height and width of elements

div {
        border-radius: 50%;
        height: 100px;
        width: 100px;
}

# min max

selector {
        min-heigth: 200px;
        min-width; 200px;
}

footer {
        max-height: 200px;
        max-width: 150px;
}

# box-sizing

* {
        box-sizing: border-box;
}

display: inline-block;

display: block;

#37 # and *

* universal selector

# id selector

<h1 id="page-title">

#page-title {
                color: maroon;
                font-family: "Times New Roman", serif;
                text-transform: uppercase;
}

#38 > ~ +
# > child combinator
parrent > child

aside > h4 {
        color: green;
        border-top: 3px solid black;
        border-bottom: 5px double black;
        padding: 4px 0;
        text-transform: uppercase;
}

# ~ subsequent-sibling combinator
reference ~ target

h2 ~ ul {
        background: lightpink;
        border: 5px outset crimson;
        list-style-type: square;
        padding: 8px 20px;
}

# + next-sibling combinator
reference + target

h2 + p {
        font-style: italic;
}

#39 Selecting elements by attribute

abbr[title] {
        border: 1px dotted gray;  # all abbr elements that have the title attribute
}

a[href="https://www.w3.org/"] {  # all an element that have an href 
        color: green;
}

a[href^="http://"] {  # all an element that have an href that begins with http://
        color: red;
}

div[id*="navbar"] {  # all div elements that have an id that includes the string navbar
        font-size: 14px;
}

a[href$=".org"] {
        color: firebrick;  # all an element that have an href attribute that ends with .org
}

div[lang|="en"] {
        color: blue;  # all div elements that have a lang attribute that equals or starts with en
}

img[alt~="photo"] {
        border: 12px ridge saddlebrown;  # not match alt attributes that include words such as photograph
}                                        # or tlephoto (assuming they don't have the whole word photo)

#40 calc() +, -, *, / and ()

for:
    length
    frequency
    angle
    time  # 2 * 2.5rem(true), but 3.5rem * 2rem(false)
    percentage
    number
    integer  # number + integer == number (5 + 2.7 = 7.7)

for division: 20em/2.75(true), but 20/2.75em(false)
              20em/0(fale)
for math symbolls add whitespace for both sides: 2 + 2, but not 2+2(false), because 2 + -2

p {width: calc(90% - 2em);}  # 90% from parrent element minus 2em

# exmpls
calc(50vw + 10px)
calc(100vh - 5rem)
calc(10% * 3)
calc(100% / 8)
calc(100vw - (5rem + 10px))

article {
        width: calc(100% - 15rem);
}

# min max clamp

article {
        width: max(75vw, 450px);
}

article {
        width: clamp(450px, calc(100% - 15rem), 1200px);  # 450px is lower bound, 1200 upper bound, 100% - 15rem is width
}

#41 attr()

p::before {content: "[" attr(id) "]";}  # add attr before string in every paragraph with [] 

<p id="Start">It is first paragraph.</p>
<p>Then second paragraph.</p>
<p id="Finish">It is third paragraph.</p>
Results:
    [Start]It is first paragraph.
    []Then second paragraph.
    [Finish]It is third paragraph.

# define width field with attr()

input[type="text"] {width: attr(maxlength em);}

<input type="text" maxlength="10">

#42 Colors

rgb(100%,100%,100%)
or
rgb(255,255,255)

rgb(100%,0%,0%)  # red
rgb(50%,0%,0%)  # maroon
rgb(75%,0%,0%)  # between red and maroon

h1 {color: rgb(75%,50%,50%);}  # for pink, need add green and blue
or
h1 {color: rgb(191,127,127);}

# half tones

p.one {color: rgb(0%,0%,0%);}
p.two {color: rgb(20%,20%,20%);}
three 40,40,40
four 60,60,60
five 80,80,80
six 0,0,0
seven 51,51,51
eight 102,102,102
nine 153,153,153
ten 204,204,204

# for "enfante terrible"

P.one {color: rgb(300%,4200%,100%);}  # css comment /* 100%,100%,100% */
P.two {color: rgb(0%,-40%,-5000%);}  # 0%,0%,0%
p.three {color: rgb(42,444,-13);}  # 42,255,0

# convert percentage to rgb numbers

if it 25% red, 35.5% green and 60% blue
multiple it in 255
equals: 63.75, 95.625 and 153
Result: rgb(64,96,153)

# RGBa with alpha chanel (clarity)

rgba(255,255,255,0.5)  # fourth is clarity from 0-1
rgba(100%,100%,100%,0.5)

# HSL - Hue(tone) это цвет, Saturation(consistence) это Насыщенность(т.е. степень чистоты цвета)
# Lightness(brightness) - степень отличия от белого и чёрного (

p.one {color: hsl(0,0%,0%);}  # black and white
p.two {color: hsl(60,0%,25%);}  # hue(tone) >50 is full color
p.three {color: hsl(120,0%,50%);}
p.four {color: hsl(180,0%,75%);}
p.five {color: hsl(240,0%,0%);}
p.six {color: hsl(300,0%,25%);}
p.seven {color: hsl(360,0%,50%);}

# HSLa with alpha chanel (clarity)

p.one {color: hsl(0,0%,0%,1);}
p.two {color: hsl(0,0%,0%,0.8);}

# transparent and currentColor

rgba(0,0,0,0) - transparent(fool clarity) i.e white

main {color: gray; border-color: currentColor;}  # Gray color border

# Angles for HSL color circle

deg - 360 degrees
grad - 400 graduces
rad - 2Пrad(6.2832rad)
turn - around HSL color circle

  0deg    0grad    0rad        0turn
 45deg   50grad    0.785rad    0.125turn
 90deg  100grad    1.571rad     0.25turn
180deg  200grad    3.142rad      0.5turn
270deg  300grad    4.712rad     0.75turn
356deg  400grad    6.283rad        1turn

#43 Time, and frequency(частота) for sound

a[href] {transition-duration: 2.4s;}
or
a[href] {transition-duration: 2400ms;}

h1 {pitch: 128hz;}  # Hz count
or
h1 {pitch: 0.128khz;}  # kHz count or KHZ? Chick it. For what?

#44 positioning

25% 35px  # 25% horizontal, 35px vertical
35px 25%  # 35px horizontal, 25% vertical

25% left  # false
35px right # false
right left  # stupid
top bottom  # child

left 25%  # true
rigth 35px  # true

right10px bottom 30px  # go to the left on 10px from right bring
                       # and go to top on 30px from bottom bring
#45 Users variable

html {
        --base-color: #639;
        --highlight-color: # AEA;
}

h1 {color: var(--base-color);}
h2 {color: var(--highlight-color);}

or

htm {
        --zuza: #639;
        --pipa: #AEA;
}

h1 {color: var(--zuza);}
h1 {color: var(--pipa);}

# how it uses
html {
        --base-color: #639;
}
aside {
        --base-color: #F60;
}
h1 {color: var(--base-color);}

<body>
    <h1>First level header</h1><p>Base text</p>
    <aside>
        <h1>FIRST LEVEL HEADER</h1><p>Other text</p>  # With othe color
    </aside>
    <h1>First level header</h1><p>Base text</p>
</body>

# how more uses

html {
        --gutter: 3ch;  # var it is an object for OOP
        --offset: 1;
}

ul li {margin-left: calc(var(--gutter) * var(--offset));}
ul ul li {--offset: 2;}
ul ul ul li {--offset: 3;}

# it equals without users var

ul li {margin-left: 3ch;}
ul ul li {margin-left: 6ch;}
ul ul ul li {margin-left: 9ch;}

# @supports for browsers how not know users variables

@supports (color: var(--custom)) {
        rules with users variables
}

@supports (--custom: value) {
        alt rules
}

#46 Pseudo-classes

article > p:first-child {
        font-style: italic;
}

p.intro:first-child {
        font-style: italic;
        text-indent: 0;
}

article *:first-child

# last-child()

p:last-child {
        margin-bottom: 24px;
}

# nth-child()

p:nth-child(2)  # any p element that's the second child of parrent
p:nth-child(3n)  # third, sixth, ninth...
p:nth-child(3n+2)  # if (n=0) - second, (n=1) - fitth, (n=2) - eight any p element
p:nth-child(even)  # 2,4,6 and so on
p:nth-child(odd)  # 1,3,5 

tr:nth-child(even) {
        background-color: lightgray;  # colored every second row in a table for example
}

# :nth-child(n of list)
:nth-child(even of h1, h2)

# :nth-last-child()

element:nth-last-chld(n [of list]){
        property1: value1;
        property2: value2;
        ...
}

# only-child

section *:only-child {
        color: plum;
}

aside: first-child {
        border: 5px double black;
}

# :first-of-type

aside:first-of-type {
        border: 5px douple black;
}

# last-of-type

p:last-of-type {
        margin-bottom: 24px;
}

# nth-of-type

p:nth-of-type(3n) {
        background-color: gray;
}

# nth-last-of-type

# only-of-type

article div:only-of-type {
        margin: 24px 8px;
}

# state

input[type="text"]:disabled {
        background-color: lightgray;
        color: darkgray;
}

# state: checked

input[type="checkbox"]:checked {
        box-shadow: 0 0 10px 3px red;
}

input[type="checkbox"]:checked + label {
        color: red;
}

# state: default

input[type="radio"]:default {
        box-shadow: 0 0 5px 1px forestgreen;
}

input[type="radio"]:default + label {
        color: forestgreen;
}

# state: dusabled

button:disabled {
        cursor: not-allowed;
        opacity: .5;
}

# state: enabled

button:enabled {
        box-shadow: 0 0 5px 3px seagreen;
        color: seagreen;
}

# state: in-range

input[type="range"]: in range {
        background-color: lawngreen;
}

#state: invalid

input[type="email"]:invalid {
        background: lavenderblush;
}

# state: optional

input[type="text"]:optional {
        background-color: lightgoldenrod yellow;
}

# state: out-of-range

input[type="range"]:out-of-range {
        background-color: tomato;
}

# state: read-only

textarea:read-only {
        border: 0;
        resize: none;
}

# state: read-write

span:read-write {
        background: honeydew;
        caret-color: crimson;
}

# state: required

input[type="text"]:required {
        background-color: yellow;
}

# state: valid

input[type="email"]:valid {
        background: palegreen;
}

# pseudo-class :active  #! :hover:active (true) :active:hover(false)

button {
        background-color: purple;
}
button:active {
        background-color: fuchsia;
}

# pseudo-class :focus or :focus-within

input:focus {
        background-color: lightsteelblue;
}

# pseudo-class :hover

button:hover {
        box-shasow: 10px 5px 5px grey;
}

# Link-Related Pseudo-Classes
# :link < :visited < :hover < :active  # 1< 2< 3, 4

# :any-link

aside a:any-link {
        text-decoration-color: mediumvioletred;
        text-decoration-style: wavy;
}

# :link

a:link {
        color: red,
        text-decoration-color: red;
}

# :target

button: target {
        cursor: not-allowed;
        opacity: .5;
}

# :visited

a:visited {
        color: pink;
        text-decoration-color: pink;
}

# Functional pseudo-classes

# :is()

:is(h1, h2, h3) {
        margin: 20px 16px;
}

p:is(:first-child, :last-child, :only-child) {
        margin: 24px;
}

# :not()

:not(.decorative) {
        font-family: Georgia, serif;
}

p:not(:first-child, :last-child, :only-chld) {
        margin: 24px;
}

img: not(img[alt]) {
        outline: 3px solid red;
}

# :where()

# :has()

aside:has(>p) {
        border: 1px solid black;
}

aside:has(div) {
        margin-top: 20px
}

h1:has(+62) {
        margin-bottom: 24px;
}

h3:has(~backquote) {
        font-style: italic;
}

#47 Pseudo elemets

# ::after

a[href^='http']::after {
        content: url(images/Icon_External_Link.png);
        padding-left: 2px;
}

<label for="user-name">Name:</label>
input id="user-name"
      type="text"
      required>
<span></span>

label for="user-email">Email:</label>
input id="user-email"
      type="email"
      placeholder="e.g., you@domain.com"
      required>
<span></span>

input:invalid + span::after {
        content: '\2717';
        color: red;
}
input:valid + span::after {
        content: '\2717';
        color: green;
}

# ::before

CSS:
.tip::before {
        content: 'TIP';
        display: block;
        color: green;
        font-size: 12px;
}

HTML:
<aside class="tip">
  The content generated by the <code>::before</code> pseudo-element
  is inline, so it flows along with the surrounding elements. If you
  want your generated content to be a block element (to enable you,
  for example, to style the pseudo-element`s width and/or height), add
  either <code>display:block</code> or <code>display: inline-block</code>
  to the pseudo-element`s declaration block.
</aside>

# ::first-letter

CSS:
h2 + p::first-letter {
        color: crimson;
        font-size: 32px;
}

# ::first-line

h2 + p::first-line {
        text-transform: uppercase;
}

#48 Comments in CSS
/* comment */
\* comment */ ???
/*comment*\  ???

#49 text-shadow

text-shadow: offset-x offset-y blur-radius color;

div {
        color: steelblue;
        font-size: 15vw;
        text-shadow: 7px 7px 5px cornflowerblue;
}

text-shadow:
    7px 7px 5px cornflowerblue,
    9px 9px 5px darkblue;

#50 Background image
<body>
  <div>
  </div>
</body>

CSS:
div {
        background-image: url("images/picture01.png");
        border: 1px solid black;
        height: 75vh;
        width: 75vw;
}

body {
        margin: 0;
        font-size: 100%;
        background-image: url("images/picture02.jpg");
        height: 100vh;
        width: 100vw;
}

#
background-position: x y

background-size: width height | keyword
  contain
  cower

background-repeat: horizontal vertical keyword
  repeat
  space
  round
  no-repeat
  repeat-x
  repeat-y

background-clip: keyword

background-origin: keyword

background-attachment: keyword
  local
  scrol
  fixed

background-color

background-image

# linear-gradient

linear-gradient(angle, color1 stop1%, colr2 stop2%, ..., colorN stopN%)

div {
        background: linear-gradient(to bottom right, yellow,
            greenyellow 50%, darkgreen);
        border: 1px solid black;
        height: 50vh;
        width: 50vw;
}

# radial-gradient

radial-gradient(shape, size at position, color1 stop1%, colr2 stip2%, ..., colorN stopN%)
  shape
  size
  single length value as 15rem
  two length value as 15rem 10rem
  closest-side
  farthest-side
  closest-corner
  farthest-corner
  position
  color1, color2
  stop1, stop2

div {
        background: radial-gradient(cosest-corner at 250px 100px,
            yellow, darkgreen);
        border: 1px solid black;
        height: 50vh;
        width: 50vw;
}

# conic gradient

conic-gradient(from angle at x y, color1, color2, ..., colorN)

#color-wheel {
  width: 33vw;
  height:33vw;
  background: conic-gradient(
          from 90deg,
          hsl(0 100% 50%),
          hsl(330 100% 50%),
          hsl(300 100% 50%),
          hsl(270 100% 50%),
          hsl(240 100% 50%),
          hsl(210 100% 50%),
          hsl(180 100% 50%),
          hsl(150 100% 50%),
          hsl(120 100% 50%),
          hsl(90 100% 50%),
          hsl(60 100% 50%),
          hsl(30 100% 50%),
          hsl(0 100% 50%),
  );
  clip-path: circle(50%);
}

#51 Fonts

serif - засечка
sans - (without) from french word

body {font-family: Times, 'Times New Roman', 'New Century Schoolbook', Georgia, 'New York', serif;}
h1, h2, h3, h4 {font-family: Charcoal, sans-serif;}
code, pre, tt, kbd {font-family: monospace;}
p.signature {font-family: cursive;}

<head>
  <meta charset="utf-8">
  <title>Link to a web font family</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?
  family=Roboto:ital, wght@0,400;1,400;1,700&display=swap"
  rel="stylesheet">
  <style>
    <body {
            font-family: Roboto, Tahoma, sans-serif;
    }
  </style>
</head>

# how get downloaded font?

@font-face {
        font-display: swap;
        font-family "SwitzeraADF";
        font-style: normal;
        font-weight: 400;
        src: local("SwitzeraADF-Regular"),
             local("Switzera-Regular"),
             url("/fonts/SwitzeraADF-Regular.otf") format("opentype"),  # Запасной ресурс
             url("SwitzeraADV-Regular.true") format("truetype");
}
@font-face {
        font-family: "SwitzeraADF";                           # Bold font for bold, 
        font-weight: bold;                                    # and other font BoldItalic for bold and italic style
        src: url("SwitzeraADF-Bold.otf") format("opentype");  
}
@font-face {
        font-family: "SwitzeraADF";
        font-weight: normal;
        font-style: italic;
        font-stretch: condensed;
        src: url("SwitzeraADF-CondItalic.otf") format("opentype");  # if need italic font

@font-face {
        font-family: "MyFont";
        src: url("myfont-math.otf" format("opentype");  # Загружать шрифт если
        unicode-range: U+22??;  # from U+2200 to 22FF   # обнаружены символы math

# font chortage
<font-weight> <font-size> <line-height> <font-family>

h1 {font: italic 900 small-caps 20px Verdana, Helvetica, Arial, sans-serif;}
h2 {font: bold normal italic 24px Verdana, Helvetica, Arial, sans-serif;}

body {font-size: 12px;}
h2 {font: bold italic 200%/1.2 Verdana, Helvetica, Arial, sans-serif;}  # Font size 24px/ and string height 28.8px

formats:
    embedded-opentype  .eot  (Embedded OpenType)
    opentype           .otf  (OpenType)
    svg                .svg  (Scalable Vector Graphics)
    truetype           .ttf  (TrueType)
    woff               .woff (Web Open Font Format)

font-weigh:
    normal, bold, bolder, lighter, 100, 200, 300, 400, 500, 600, 700, 800, 900
    normal - 400
    bold   - 600, 700

    "Light" - 100, 200, 300
    "Normal", "Regular", "Romain", "Book" - 400
    "Medium" - 500
    "Extra Bold" = 800, 900  # or "Black" and "UltraBlack"

font-size:
    p.one {font-size: xx-small;}  # 10px
                      x-small     # 12px
                      small       # 14px
                      medium      # 16px
                      large       # 19px
                      x-large     # 24px
                      xx-large    # 32px

# font-size-adjust for diff height fonts if it need shows like one

p {font: 10px Verdana, sans-serif; font-size-adjust: auto;}
p.c12 {font-family: Times, serif;}

# bolder and lighter for inheritance

p {font-weight: normal;}
p em {font-weight: bolder;}  # to 700

h1 {font-weight: bold;}
h1 b {font-weight: bolder;}  # to 800

div {font-weight: 100;}
div strong {font-weight: bolder;}  # to 400

# text decoration

p.one {text-decoration: underline;}  # подчеркнуть
p.two {text-decoration: overline;}  # линия сверху
p.three {text-decoration: line-through;} # зачёркнуто
p.four {text-decoration: blink;}  # мигать  don't supported is old function
p.five {text-decoration: none;}  # no underline links and stop all effects whole
                                 # But! For daltonics NEED link line!

text-decoration-color: hsl(250, 100%, 75%);
text-decoration-style: dotted
text-decoration-thickness: 3px;

text-decoration: line color style thickness;
text-decoration: underline tomato wavy 2px;

# text-align
text-align: keyword;
  left(default)
  right
  center
  justify

# hyphens
hyphens: keyword;
  none(default)
  auto
  manual

# text-indent
text-indent: value
  0(default)

p + p {
        text-indent: 1.5rem;
}

# text-shadow, to heavy to weight of page and speed load

text-shadow: rgb(128,128,255) -5px -0.5em;  # shadow in left with blure

p.c9 {colora; black; text-shadow: gray 2px 2px 4px;}
p.c10 {color: white; text-shadow: 0 0 4px black;}
p.c11 {color: black; text-shadow: 1em 0.5em 5px red, -0.5em -1em
        hsl(100,75%,25%,0.33);)  # full blure shadow in right-down

# White-space  # Запретить переносы, чтобы создать табличку например
# nowrap

td {white-space: nowrap;}

<table><tr>
<td>Text no wrap.</td>
<td>And then no wrap.</td>
<td>And then.</td>
<td>White-space rule.</td>
</tr></table>

# pre-wrap and pre-line for correct view

<p style="whit-space: pre-wrap;">  # browser don't touch whitespaces strictly

<p style="white-space: pre-line;">  # browser use normal lines

Value    WhiteSpaces    break strings    New string
pre-line    yes             no             yes
normal      yes             no             yes
nowrap      yes             no             no
pre         no              yes            no
pre-wrap    no              yes            yes
