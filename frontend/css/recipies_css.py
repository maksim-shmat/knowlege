"""Recipies for css."""

#1 List in horizontal

<ul id="rollcall">
  <li>One</li>
  <li>Two</li>
  <li>Three</li>
  <li>Four</li>
  <li>Five</li>
</li>

#rollcall li {display: inline; border-right: 1px solid;
              padding: 0 0.33em;}
#rollcall li:first-child {border-left: 1px solid;}

#2 Z-index 3d positioning

p {background: rgba (255,255,255,0.9); border: 1px solid;}
p#first {position: absolute; top; 0; left: 0; width: 40%;
  height: 10em; z-index: 8;}
p#second {position: absolute; top: -0.75em; left: 15%;
  width: 60%; height: 5.5em; z-index: 4;}
p#third {position: absolute; top: 23%; left: 25%; width: 30%;
  height: 10em; z-index: 1;}
p#fourth {position: absolute; top: 10%; left: 10%; width: 80%;
  height: 10em; z-index: 0;}

#3 Fixed sidebar

body {background: black; color: silver;}

div#header {position: fixed; top: 0; bottom: 80%; left: 20%;
  right: 0; background: gray; margin-bottom: 2px; color: yellow;}
div#siderbar {position: fixed; top: 0; bottom: 0; left: 0;
  right: 80%; background: silver; margin-bottom: 2px; color: yellow;}
div#main {position: absolute; top20%; bottom: 0; left: 20%;
  right: 0; overflow: scroll; background: white; color: black;}

footer {position: fixed; bottom: 0; width: 100%; height: auto;}

#4 glued positioning

#scrollbox {overflow: scroll: width: 15em; height: 18em;}  # glue to uper side
#scrollbox {position: sticky; top: 2em; bottom: auto;
  left: auto; right: auto;}

#scrollbox {oveflow: scroll: position: relative; width: 15em;  # glue to down side
  height: 10em;}
#scrollbox h2 {position: sticky; top: auto; bottom: 0;
  left: auto; right: auto;}


