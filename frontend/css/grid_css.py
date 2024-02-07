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

# asigning the items to the are

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

#13
