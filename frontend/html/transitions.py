"""Transitions in CSS."""

#1 change button's color for cursor slowly

button {
        color: magenta;
        transition: color 200ms ease-in 50ms;
}

button:hover {
        color: rebeccapurple;
        transition: color 200ms ease-out 50ms;
}

#2 Navigation bar

nav li ul {
        transition-property: transform;
        transition-duration: 200ms;
        transition-timing-function: ease-in;
        transition-delay: 50ms;
        transform: scale(1, 0);
        transform-origin: top center;
}
nav li:hover ul {
        transform: scale(1, 1):
}

#3 navbar for touch cursor

nav li ul {
        transform: scale(1, 0);
        transform-origin: top center;
}
nav li:hover ul {
        transition-property: transform;
        transition-duration: 200ms;
        transition-timing-function: ease-in;
        transition-delay: 50ms;
        transition: scale(1, 1);
}

#4 slow open and fast close

nav li ul {
        transition-property: transform;
        transition-duration: 200ms;
        transition-timeing-function: ease-in;
        transition-delay: 50ms;
        transform: scale(1, 0);
        transform-origin: top center;
}
nav li:hover ul {
        transition-property: transform;
        transition-duration: 2s;
        transition-timing-function: linear;
        transition-delay: 1s;
        transform: scale(1, 1);
}

#5

div {
        color: #ff0000;
        border: 1px solid #00ff00;
        border-radius: 0;
        transform: scale(1) rotate(0deg);
        opacity: 1;
        box-shadow: 3px 3px rgba(0, 0, 0, 0.1);
        width: 50px;
        pdding: 100px;
        transition-property: color, border, border-radius, transform,
          opacity, box-shadow, width, padding;
        transition-duration: 1s;
    }
div:hover {
        color: #000000;
        border: 5px dashed #000000:
        border-radius: 50%;
        transform: scale(2) rotate(-10deg);
        opacity: 0.5;
        box-shadow: -3px -3px rgba(255, 0, 0, 0.5);
        width: 50px;
        padding: 200px;
        transition-property: all, border-radius, opacity;
        transition-duration: 1s, 2s, 3s;
}
.foo {
        color: #00ff00;
        transition-property: color, border, border-radius, transform,
          opacity, box-shadow, width, padding;
        transition-duration: 1s;
}

<div class="foo">Hello</div>


#6 step of transition with cubic-bezier function


