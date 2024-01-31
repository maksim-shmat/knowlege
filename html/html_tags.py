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

