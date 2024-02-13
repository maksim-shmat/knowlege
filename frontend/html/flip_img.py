"""Flip image with CSS."""

#1

span {border: 1px solid red; display: inline-block;}
img {vertical-align: bottom;}
img.flip {transform: rotateX(180deg); display: inline-block;}
img#show {backface-visibility: visible;}
img#hide {backface-visibility: hidden;}

<span><img src="card.gif"></span>
<span><img src="card01.gif" class="flip" id="show"></span>
<span><img src="card02.git" class="hide" id="hide"></span>

#2 card with backface description

section {position: relative;}
img, div {position: absolute; top: 0; left: 0;
          backface-visibility: hidden;}
div {transform: rotateY(180deg);}
section:hover {transform: rotateY(180deg);
               transform-style: preserve-3d;}
<section>
  <img src="photo.jpg" alt="">
  <div class="info">(...description...)</div>
</section>

#3 Better realistic.

section {position: relative;}
img, div {position: absolute; top: 0; left: 0;}
div {transform: rotateY(180deg); backface-visibility: hidden;
        background: rgba(255, 255, 255, 0.85);}
section:hover {transform: rotateY(180deg);
        transform-style: preserve-3d;}
