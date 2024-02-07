"""CSS tool Flexbox about."""

#1 Setting the flex direction from horizontal to vertical container

HTML

<div class="container">
  <div class="item item1">1</div>
  <div class="item item2">2</div>
  <div class="item item3">3</div>
  <div class="item item4">4</div>
  <div class="item item5">5</div>
</div>

CSS

.container {
        display: flex;          # add it two rows
        flex-direction: row;    # for change horizontal to vertical container
        border: 5px double black;
}
.item {
        font-family: Verdana, sans-serif;
        font-size: 5rem;
        padding: .1rem;
        text-align: center;
}
.item1 {
        background-color: hsl(0, 0%, 94%);
}
.item2 {
        background-color: hsl(0, 0%, 88%);
}
.item3 {
        background-color: hsl(0, 0%, 82%);
}
.item4 {
        background-color: hsl(0, 0%, 76%);
}
.item5 {
        background-color: hsl(0, 0%, 70%);
}

#2 Aligning flex items along the primary axis

container {
        display: flex;
        justify-content: flex-start|flex-end|center|space-around|
        space-between|space-evenly;
}

#3 Aligning flex items along the secondary axis

container {
        display: flex;
        align-items: stretch|flex-start|flex-end|center|baseline;
}

and if you want to set a secondary axis alignment for an individual flex item:

item {
        align-self: stretch|flex-start|flex-end|center|baseline;
}

#4 Centering an element horizontally and vertically

container {
        display: flex;
        justify-content: center;
        align-items: center;
        align-items: center;
}

HTML

<div class="container">
  <div class="item">Look, ma, I`m centered!</div>
</div>

CSS

.container {
        border: 5px double black;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 50vh;
}
.item {
        font-family: Georgia, serif;
        font-size: 2rem;
}

#5 Alowing flex items to wrap

element {
        display: flex;
        flex-wrap: nowrap|wrap|wrap-reverse;
}

HTML

<div class="container">
  <div class="item item1">1</div>
  <div class="item item2">2</div>
  <div class="item item3">3</div>
  <div class="item item4">4</div>
  <div class="item item5">5</div>
</div>
<div><code>wrap</code></div>
<div class="container wrap">
  <div class="item item1">1</div>
  <div class="item item2">2</div>
  <div class="item item3">3</div>
  <div class="item item4">4</div>
  <div class="item item5">5</div>
</div>
<div><code>wrap-reverse</code></div>
<div class="container wrap-reverse">
  <div class="item item1">1</div>
  <div class="item item2">2</div>
  <div class="item item3">3</div>
  <div class="item item4">4</div>
  <div class="item item5">5</div>
</div>

CSS

.container {
        border: 5px double black;
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        height: 40vh;
        width: 85vw;
}
.wrap {
        flex-wrap: wrap;
}
.wrap-reverse {
        flex-wrap: wrap-reverse;
}
.item {
        height: 50%;
        width: 25vw;
}

#6 Aligning rows or columns along the secondary axis

element {
        display: flex;
        align-content: stretch|center|flex-start|flex-end|
        space-around|space-between|space-evenly;
}

#7 Adding gaps between items

row-gap: row-gap-value;
column-gap: column-gap-value;
gap: row-gap-value [column-gap-value];

.container {
        border: 5px double black;
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        gap: 1rem;
        height: 50vh;
        width: 50vw;
}

#8 Allowing glex items to grow

item {
        flex-grow: value;
}

.item1,
.item2,
.item3 {
        flex-grow: 1;  # flex-grow for 3 elements
}

.item1 {
        flex-grow: 1;
}
.item2 {
        flex-grow: 2;
}
.item3 {
        flex-grow: 1;
}

#9 Allowing flex items to shrink

item {
        flex-shrink: value;
}

HTML

<div class="container">
  <div class="item item1">1</div>
  <div class="item item2">2</div>
  <div class="item item3">3</div>
  <div class="item item4">4</div>
  <div class="item item5">5</div>
</div>

CSS

.container {
        display: flex;
        width: 600px;
        border: 5px double black;
}
.item {
        flex-shrink: 0.5;
}

#10 Suggesting a flex item size

item {
        flex-basix: value;
}

.item1 {
        flex-grow: 1;
        flex-shrink: 0;
        flex-basis: 200px;
        min-width: 100px;
        max-width: 400px;
}

#11 Using the flex shorthand property

.item1 {
        flex-shrink: 0;
        flex-basis: 10px;
        flex: 1;
}

.item1 {
        flex-shrink: 0;
        flex-basis: 10rem;
        flex-grow: 1;
        flex-shrink: 1;
        flex-basis: 0;
}

flex-grow:2;
flex-shrink: 1;
flex-basis: 0;  # short: flex: 2;

flex-grow: 1;
flex-shrink: 1;
flex-basis: 10rem;  # short: fles: 10rem;

flex-grow: 2;
flex-shrink: 1;
flex-basis: 12vw;  # short: flex: 2 12vw;

flex-grow: 0;
flex-shrink: 0;
flex-basis: 200px;  # short: flex 0 0 200px;

HTML

<body>
  <header>
    Header
  </header>
  <nav>
    Navigation
  </nav>
  <main>
    <article>
      Article
    </acticle>
    <aside
      Aside
    </aside>
  </main>
  <footer>
    Footer
  </footer>
</body>

CSS

html {
        height: 100%
}
body {
        display: fles;
        flex-direction: column;
        gap: 1rem;
        height: 100%;
        width: 75vw;
}
main {
        flex: 1;
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
}
article {
        flex: 1 0 15rem;
}
aside {
        flex: 0 0 10 rem;
}

#12 Changing the order of flex items

.item1 {
        oreder: 1;
}

#13 Make a page fluid for desctop and mobile is good

HTML

<header>
  ...
</header>
<nav>
  ...
</nav>
<main>
  <article>
    <h2>
      Blah-blah <em>You</em> in Court, Mister!
    </h2>
    <p>
      blah
      blah
      blah
    </p>
  </article>
  <aside>
    <h3>Related Stories</h3>
    <p>
      It`s Official: Blah-blah
    </p>
  </aside>
</main>

CSS

body {
        max-width: 60rem;
}
main {
        display: flex;
        flex-wrap: wrap;
}
article {
        flex: 3;
        min-width: 22rem;
}
aside {
        flex: 1;
        min-width: 16rem;
}

#14 Making typography fluid

font-size: 1.5vmax;

font-size: calc(0.75rem + 1vmax);  # better
font-size: calc(0.75rem + 2vmax);  # try it

#15 best fluid friend clamp()

font-size: clamp(1.25rem, 0.75rem + 1vmax, 1.75rem);

#16 Interrogating the screen with media queries

@media (max-width: value) {
        declarations
}

@media (min-width: value) {
        declarations
}

HTML

<header>
  <img src="images/notw.png" alt="News of the World logl"
  class="site-logo">
  <h1>News of the Word</h1>
  <p class="subtitle">Language news you won blah</p>
</header>

CSS

@media (max-width: 40rem) {
        .site-logo {
            display: none;
        }
}

# count multiple expressions

@media (expression1) and (expression2) {  # <and> or <or>
        declarations
}

@media (min_width: 40rem) and (max-width: 60rem) {
        declarations
}

# range syntax for media queries

@media (40rem <= width <= 60rem) {
        declarations
}

#17 Setting up the query container

HTML

<div class="card-container">
  <div class="card-wrapper">
    <img class="card-image" src="images/inflatable-dartboar.png alt="Inflatable Durboard</h3>
    <div>
      <h3 class="card-title">Inflatable Burbone</h3>
      <p class="card-description">
      Blah
      blah
      blah
      </p>
      <div class="card-actions">
        <button class="card-button learn-more">Learn more</button>
        <button class="card-button add-to-card">Add to card</button>
      </div>
    </div>
  </div>
</div>

CSS

.card-container {
        container-type: inline-size;
}
.card-wrapper {
        display: grid;
        gap: 1.5rem;
        grid-template-columns: auto auto;
        grid-template-rows: auto;
}
.card-image {
        min-width: auto;
        height: auto;
        object-fit: cover;
        object-position: center;
        overflow: hidden;
}
.card-title {
        text-align: left;
}
.card-actions {
        display: flex;
        gap: 1rem;
        justify-content: flex-start;
}

# for multiple query containers need to name each container

element {
        container-type: value;
        container-name: name;
}

#18 Quering the container

@container (expression) {
        declarations
}

@container (width < 25rem) {
        .card-wrapper {
            align-items: center;
            display: block;
            padding: 1rem;
        }
        .card-image {
            display: none;
        }
        .card-title {
            margin-top: 0;
        }
}

@container (width > 25rem) and (width < 35rem) {
        .card-wrapper {
            grid-template-columns: auto;
            grid-template-rows: auto auto;
        }
        .card-image {
            width: 100%;
            height: 10rem;
        }
        .card-title {
            text-aligh: center;
        }
        .card-actions {
            justify-content: center;
        }
}

#19 User preference queries, dark theme

@media (preference: value) {
        declarations
}

@media (prefers-color-scheme: dark) {
        /* Dark color scheme colors go here */
}

hsl(180deg 50% 80%)  # light color
hsl(180deg 50% 20%)  # dark mode color

@media (prefers-contrast: more) {
        /* Higher-contrast colors go here */
}

@media (prefers-reduced-motion: reduce) {
        *,
        ::after
        ::before{
            animation-duration: 0.01ms;
            animation-iteration-count: 1;
            transition-duration: 0.01ms;
            scroll-behavior: auto;
        }
}

#20
