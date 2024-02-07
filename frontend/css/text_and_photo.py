"""Positioning with CSS."""

#1 Fixed photo positon on the colored background

HTML

<header>
  <img src="images/img1.jpg" alt="Photo for illustration of text">
  <h1>
    Text smth
  </h1>
</header>
<main>
...
</main>

CSS

header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 4rem;
        border: 1px double black;
        background-color: hsl(101, 38%, 63%);
}

main {
        margin-top: 4rem;
}

#2 Giving absolute positioning a whirl

HTML

<section>
  <img src="images/new.png" alt="photo">
  <h1>
    Header text
  </h1>
  <div>
    <i>n.</i> Blah-blah.
  </div>
  <div>
    Blah
    blah
    blah
  </div>
</section>

CSS

section {
        position: relative;
        border: 1px double black;
}

img {
        position: absolute;
        top: 0;
        right: 0;
}

#3 Relative positioning

HTML

<h1>
  Text header
</h1>
<div>
  <i>n.</i> blah-blah
</div>
<img src="/images/photo01.jpg" alt="photo about it">
<img src="/images/photo02.jpg" alt="other photo" class="offset-image">
<img src="/images/photo03.jpg" alt="photo about it more">

CSS

.offset-image {
        position: relative;
        left: 200px;
}

#4 Making element stick (temporarily)

HTML

<section>
  <h2>Cat ipsum</h2>
  <p><a href="http://www.catipsum.com/">http://www.catipsum.com/</a></p>
  <p>Sample:<p>
  <p class="sample-text">
    Cat ipsum dolor sit
    blah
    blah
    blah.
  </p>
</section>

CSS

h2 {
        position: sticky:
        top: 0;
}

#5 Layering elements with z-index, deep in 3d Z-side

HTML

<body>
  <div id="div1">
    <span>div1</span>
  </div>
  <div id="div2">
    <span>div2</span>
  </div>
</body>

CSS

#div1 {
  position: relative;
  z-index: 2;
}
#div2 {
  position: relative;
  bottom: 100px;
  left: 100px;
  z-index: 1;
}

#6 stacking contexts, aside position

HTML

<body>
  <div id="div1">
    <span>div1</span>
  </div>
  <div id="div2">
    <span>div2</span>
    <aside>
      <span>aside</span>
    </aside>
  </div>
</body>

CSS

#div1 {
  position: relative;
  z-index: 2;
}

#div2 {
  position: relative;
  bottom: 100px;
  left: 100px;
  z-index: 1;
}
aside {
        position: relative;
        top: 25px;
        left: 80px;
        z-index: 3;
}

#7
