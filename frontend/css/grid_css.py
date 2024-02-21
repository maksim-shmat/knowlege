"""CSS Grid about."""

#1 Setting up teh grid container

container {
        display: grid;
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
        border: 5px double black;
        display: grid;
        text-align: center;
}
.item {
        font-family: Verdana, sans-serif;
        font-size: 3rem;
}
.item1 {
        background-color:hsl(0, 0%, 94%);
}
.item2 {
        background-color:hsl(0, 0%, 88%);
}
.item3 {
        background-color:hsl(0, 0%, 82%);
}
.item4 {
        background-color:hsl(0, 0%, 76%);
}
.item5 {
        background-color:hsl(0, 0%, 70%);
}
.item6 {
        background-color:hsl(0, 0%, 64%);
}

#2 Setting your own columns and rows the explicit grid

container {
        display: grid;
        grid-template-columns: column-values;
        grid-template-rows: row-values;
}

HTML

<div class="container">
  <div class="item item1"></div>
  <div class="item item2"></div>
  <div class="item item3"></div>
  <div class="item item4"></div>
  <div class="item item5"></div>
  <div class="item item6"></div>
</div>

CSS

.container {
        display: grid;
        grid-template-columns: 100px 300px 200px;
        grid-template-rows: 100px 200px;
}

#3 letting a column or row grow or shrink as needed

fr - fraction

.container {
        display: grid;
        grid-template-columns: 100px 300px 1fr;
        grid-template-rows: 100px 200px;
}

#4 repet() for multiply objects

grid-template-columns: 250px repeat(8, 1fr) 300px;

grid-template-columns: repeat(auto-fill, 100px);

#5 Setting a range of values: the minmax() 

grid-template-columns: 150px 200px minmax(200px, 500px);

grid-template-columns: minmax(250px, 1fr) repeat(5, 10vw);

#6 Sizing with auto keyword

grid-template-columns: repeat(3, auto);
gtid-template-rows: auto auto;

#7 implicit grid

HTML

<div class="container">
  <div class="item item1">1</div>
  <div class="item item2">2</div>
  <div class="item item3">3</div>
  <div class="item item4">4</div>
  <div class="item item5">5</div>
  <div class="item item6">6</div>
  <div class="item item7">7</div>
  <div class="item item8">8</div>
</div>

CSS

.container {
        border: 5px double black;
        display: grid;
        grid-template-columns: 1fr 3fr 2fr;
}

or for leaving out the grid columns template

.container {
        border: 5px double black;
        display: grid;
        grid-template-rows: repeat(8, auto);
}

#8 Specified a size for implicit rews or columns

grid-auto-rows: value
grid-auto-columns: value

.container {
        border: 5px double black;
        display: grid;
        grid-template-columns: 1fr 3fr 2fr;
        grid-auto-rows: 100px;
}

#9 Creating grid gaps

row-gap: row-gap-value;
column-gap: column-gap-value;
gap: row-gap-value [column-gap-value];

.container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-template-rows: 1fr 2fr;
        gap: 1vw;
}

#grid {display: grid; height: 500px;
  grid-template-rows: 100px 1fr 1fr 75px;
  grid-row-gap: 15px;
  grid-template-columns: 15% 1fr 1fr;
  grid-column-gap: 1em;}

#10 Assigning grid items using line numbers

item {
        grid-column-start: column-start-value;
        grid-column-end: column-end-value;
        grid-row-start: row-start-value;
        grid-row-end: row-end-value;
}

HTML

<div class="container">
  <div class="item item1">1</div>
  <div class="item item2">2</div>
  <div class="item item3">3</div>
  <div class="item item4">4</div>
  <div class="item item5">5</div>
  <div class="item item6">6</div>
</div>

CSS

.container {
        display: grid;
        grid-template-columns: 15vw repeat(3, 1fr) 20vw;
        grid-template-rows: 15vh 1fr 1fr;
        height: 100%;
}
.item1 {
        grid-column-start: 1;
        grid-row-start: 1;
}
.item2 {
        grid-column-start: 2;
        grid-column-end: span 4;
        grid-row-start: 1;
}
.item3 {
        grid-column-start: 1;
        grid-row-start: 2;
        grid-row-end: -1;
}
.item4 {
        grid-column-start: 2;
        grid-column-end: 5;
        grid-row-start: 2;
        grid-row-end: -1;
}
.item5 {
        grid-column-start: 5;
        grid-row-start: 2;
}
.item6 {
        grid-column-start: 5;
        grid-row-start: 3;
}

# shorthands
item {
        grid-column: column-start-value / column-end-value;
        grid-row: row-start-value / row-end-value;
}

#11 assigning grid items to named grid area

.container {
        display: grid;
        grid-template-columns: 15vw repeat(3, 1fr) 20vw;
        grid-template-rows: 15vh 1fr 1fr;
        grid-template-areas:
          "logo header header header header"
          "nav content content content sidebar"
          "nav content content content ad";
}

.item3 {
        grid-column-start: 1;
        grid-row-start: 2;
        grid-row-end: -1;
}

# asigning the items to the area

item {
        grid-area: name;
}

.item1 {
        grid-area: logo;
}
.item2 {
        grid-area: header;
}
.item3 {
        grid-area: nav;
}
.item4 {
        grid-area: content;
}
.item5 {
        grid-area: sidebar;
}
.item6 {
        grid-area: ad;
}

#12 How CSS Grid makes a page fluid, good for desctop and mobile screens

HTML

<header>
  <h1> Blah, blah</h1>
  <p class="subtitle">In which our blah-blah</p>
</header>
<main>
  <p>
  blah blah
  blah
  blah <i>The Mother Tongue</i>
  </p>
</main>

CSS

main {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
        gap: 2rem;
}
main > p:nth-child(even) {
        background: hsl(208deg 50% 80%);
}

#13 naming for rows and columns

# grid {display: grid;
        grid-template-columns:
            [start col-a] 200px [col-b] 50% [col-c] 100px [stop and last];
        grid-template-rows:
            [start masthead] 3em [comment]% calc(100%-5em) [footer] 2em [stop end];
        }

#14 fr дольные части

grid-template-columns: 1fr 1fr 1fr 1fr;
equals
grid-template-columns: 25% 25% 25% 25%;
add one column
grid-template-columns: 1fr 1fr 1fr 1fr 1fr
equals
grid-template-columns: 20% 20% 20% 20% 20%

grid-template-columns: 1fr 2fr 1fr;
equals
grid-template-columns: 0.25 0.5 0.25;
or
grid-template-columns: 1fr 3.14159fr 1fr;

width: 100em; grid-template-columns: 15em 4.5fr 3fr 10%;

grid-template-columns: 15em 4.5fr minmax(5em,3fr) 10%;  # minmax for 3 column

#15 repeat()

#grid {display: grid;
  grid-template-columns: repeat(3, 2em 1fr 1fr) 2em;}  # 3*(2em 1fr 1fr) + 2em

#grid {display: grid;
  grid-template-columns: repeat(4, 10px [col-start] 250px [col-end]) 10px;}

# double-named columns, if lines is in one place

grid-template-rows: repeat(3, [top] 5em [bottom]);
grid-template-rows: [top] 5em [bottom top] 5em [top bottom] 5em [bottom];

#16 grid-template-areas

#grid {display: grid;
  grid-template-areas:
      "h h h h"
      "l c c r"
      "l f f f ";}
equals
# grid {display: grid;
  grid-template-areas:
      "header header header header"
      "leftside content content content rightside"
      "leftside footer footer footer";}

#17 named grid

#grid {display: grid;
  grid-template-rows: repeat(10, (R) 1.5em);
  grid-template-columns: 2em repeat(5, [col-A] 5em [col-B] 5em) 2em;}
.one {
        grid-row: R 3 / 7;
        grid-column: col-B / span 2;}
.two {
        grid-row: R / span R 2;
        grid-column: col-A 3 / span 2 col-A;}
.three {
        grid-row: 9;
        grid-column: col-A -2;}

#18 auto-flow

<ol id="grid">
  <li>1</li>
  <li>2</li>
  <li>3</li>
  <li>4</li>
</ol>

#grid {display: grid; width: 45em; height: 8em;  # in row
  grid-auto-flow: row;}
#grid li {grid-row: auto; grid-column: auto;}

#grid {display: grid; width: 45em; height: 8em;  # in column
  grid-auto-flow: column;}
#grid li {grid-row: auto; grid-column: auto;}

#grid {display: grid; widht: 45em; height: 8em;  # with sizes
  grid-auto-flow: column;}
#grid li {grid-row: auto; grid-column: auto;
  width: 7em; height: 1.5em;}

#19
