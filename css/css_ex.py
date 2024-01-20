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
