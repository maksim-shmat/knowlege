"""HTML tags about."""

#1 Breack line
Hello<br>
World<br>
!

#2 Horizontal line between the paragraphs
Hello<hr>  # named "horizontal rule"
---------
World!

#3 Navigate on the page
...
</header>
<nav>
  <a href="/">Home</a>
  <a href="semantics.html">Semantics</a>
  <a href="contact.html">Contact</a>
  <a href="about.html">About</a>
</nav>

#4 Division
<div>
  Requisite social media links:
</div>
<div>
  <a href="https://twikker.com/">Twikker</a>
  <a href="https://inst.com/">Inst</a>
</div>

#5 Inline element with <span>
<p>
Notice how an <span style="font-variant: small-caps">
inline element</span> flows right along with the
rest of the text.
</p>

#6 Comments
<!--
    something-something
-->

#7 Emphasizing text with italic

You`ll <em>never</em> fit in there with that rdiculous thing on your head!
or <i> never </i>

#8 Bold text

<strong> Hello </strong> World!
or <b> Hello </b>

#9 Quoted strings and Quoted blocks, and Cite

Hello <q>friends</q>

<blockquote>
  Blah
  blah
  blah
</blockquote>

Blah-blah
  <q cite="http://html.spec.whathever.org/#the-q-element">blah-blah
  blah.</q>

#10 Links

<a href="https://webdev.mcfedries.com/wb"> Link text</a>  # remote web page

<a href="rutabagas.html">!!!</a>  # local web page

<a href="/wordplay/puns.html"> click this!</a>  # local web page in a different directory

#11 Anchors

<element id="name">

<section id="section1">

<a href="#name">

<a href="#section1">

<a href="chapter57.html#section1">  # anchors to the same web page

#12 Abbreviation

Why, their life becomes a 
<abbr title="single income, two childern, oppressive mortgage">SITCOM</abbr>, of course.

if you move cursor ont SITCOM, you have info about

#13 Address with italic

<p>
  Having a problem? Please "contact us" here:
</p>
<address>
  The Complaints Department<br>
  0 Black Hole Blvd, Suite -23<br>
  Nowheresville, BC N0N 0N0
</address>

#14 Cite as a link

<p>
  Source: <cite><a href="http://html.spec.whatwg.org/#the-cite-element">The cite
  element</a></cite>, published by CHuchong.
</p>

#15 sample output
<samp>404 Not Found</samp>

#16 dl - description list

<h3>Some insilts Worth Hurling</h3>
<dl>
  <dt>disingenuflect</dt>
  <dd>To act in a servile or worshipful manner insincerely
      or hypocritically.</dd>
</dl>

#16 Yello highlight

<mark> something</mark>

#17 Зачёркнуто strikethrough

<s>Idiot</s>
or
<del>Bimbo</del>

#18 Subscript

<p>
  Feeling up today? Perhaps your brain is taking a dopamine
  (C<sub>8</sub>H<sub>11</sub>NO<sub>2</sub>) bath.
</p>

#19 Superscript

<sup>*</sup>

#20 Image and figcaption for image

</p>
  <figure>
    <img src="images/gurardian_of_blideness.jpg"
    alt="Screenshot of the source code of blah-blah">
    <figcaption>
      <b>Figure 1</b>-A want ad buried in the HTML source
      of <i>The Gugudie</i> newspoper wep page.
    </figcaption>
  </figure>

# Image as a link:

<header>
  <a href="/"><img src="imagesf/list_logo.png" alt="How mane chances?"></a>
  <h1>Welcome to "Lohotrone!"</h1>
  <hr>
</header>

#21 Tables

<tr> - table row
<td> - table divide
<thead> - table header

# Css for n-th elements
td:nth-child(4) {
        text-align: justify;
}

# borders

selector {
        border: width style color;
}

style: dotted, dashed, double, groove, ridge, inset, outset, solid

#22 Forms

<input type="submit" value="Submit Me!">

<input type="textType" name="textName" value="Первое значение" placeholder="Подсказка а поле">

<input type="text" name="company" size="50">

<input type="number" name="points" value="100">

<input type="range" name="transparency" min="0" max="100" value="100">

<input type="email" name="user-email" placeholder="you@yourdomain.com">

<input type="url" name="homepage" placeholder="e.g., http://domain.com/">

<input type="tel" name="mobile" placeholder="(xxx)xxx-xxxx">

<input type="time" name="start-time">

<input type="password" name="userpassword" autocomplete="current-password">

<input type="search" name="q" placeholder="Type a search term">

<input id="userSession" name="user-session" type="hidden" value="jwr274">

<textarea name="messag" rows="5">
Default text goes here.
</textarea>

# method 1 for label
<label>
Email:
    <input type="email" name="user-email" placeholder="you@yourdomani.com">
</label>

# method 2 for label

<label for="useremail">Email:</label>
<input id="useremail" type="email" name="user-email" placeholder="example@email.com">

# checkboxes

<input type="checkbox" name="checkName" value="checkValue" [checked]>  # checked without []

<fieldset>
    <legend>
            What`s your phobia? (Please check all that apply):
    </legend>
    <label>
        <input type="checkbox" name="phobia"
                               value="Ants">Myrmecophobia (Fear of ants)<br>
    </label>
    <label>
        <input type="checkbox" name="phobia"
                               value="Bald">Peladophobia (Fear of becoming bald)
    </label>
</fieldset>

# radio buttons

<input type="radio" name="radioGroup" value="radioValue" [checked]>  # checked withot [] work ?!

<fieldset>
  <legend>
    Select a delivery method
  </legend>
  <div>
    <input type="radio" id="carrier-pigeon" name="delivery"
    value="pigeon" [checked]>
    <label for="carrier-pigeon">Carrier pigeon</label>
  </div>
  <div>
    <input type="radio" id="pony-express" name="delivery"
    value="pony">
    <label for="pony-express">Pony express</label>
  </div>
</fieldset>

# drop-down selection list
<form>
        <div>
                <label for="hair-color">Select your hair color:
                </label><br>
                <select id="hair-color" name="hair-color">
                        <option value="black">Black</option>
                        <option value="blonde">Blonde</opion>
                </select>
        </div>
        <div>
                <label for="hair-style">Select your hair style:
                </label><br>
                <select id="hair-style" name"hair-style">
                        <option value="bouffant">Bouffant</option>
                        <option value="mohawk">Mohawk</option>
                </select>
        </div>
</form>

# field for select of colors

<input type="color" name="br-color" value="#4f5392">

# field choose a date
<input type="date" name="appt-date" value="2024-02-01">

# field for choose file

<input type="file" name="user-photo">

# chose the month

<input type="month" name="birthday-month" value="2023-08">

# chose the week

<input type="week" name="vacation-week" value="2023-W34">

#23 ARIA Accessible Rich Internet Applications

ARIA rolels - HTML Semantic Elements
------------------------------------
banner -------- header
complementary - aside
contentinfo --- footer
form ---------- form
main ---------- main
navigation ---- nav
region -------- section
search -------- N/A

article ------- article
cell ---------- td
definition ---- dfn
figure -------- figure
heading ------- h1 through h6
img ----------- img or picture
list ---------- ol or ul
listitem ------ li
meter --------- meter
row ----------- tr
rowgroup ------ tbody, thead, or tfoot
rowheader ----- th
table --------- table
term ---------- dfn or dt

button -------- button
checkbox ------ input type="checkbox"
link ---------- a

option -------- option
progressbar --- progress
radio --------- input type="radio"
textbox ------- input type="text"

#24
