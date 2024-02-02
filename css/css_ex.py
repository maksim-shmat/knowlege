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

#49 calc() +, -, *, / and ()

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


