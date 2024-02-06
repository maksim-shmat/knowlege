"""JavaScript about."""

#1 Connect other file.js to html

<script src="srcipts/myscript.js">

<script src="http://www.host.com/myscript.js">

#2 Declare variable

let interestRate;  // Annual interest rate for loan calculation

interestRate = 0.06;

interestRate = iterestRate / 12  # interestRate = 0.06 / 12
document.write(interestRate);

#
const milesToKilometers = 1.06934;

#
let firsName;
firstName = prompt("Please tell me your first name:");
document.write("Welcome to my website, " + firstName);

#2 Decrement with --

let thisVariable = 1;
thisVariable = thisVariable -1;  # 1-1=0
thisVariable--;  # 1-1=0
thisVariable -= 1;  # 1-1=0

#3 Underwater stones

const preTipTotal = 10.00;
const tipAmount = preTipTotal * 0.15;
const message1 = "Your tip is ";
const message2 = "<br>Your total bill is ";
document.write(message1 + tipAmount + message2 + preTipTotal + tipAmount);

RESULTS: Your tip is 1.5
         Your total bill is 101.5  # Wrong! Not obvious view concatenation 10 + 1.5 = 101.5 (OMG! JS we are make a fortune!)

const preTipTotal = 10.00;
const tipAmount = preTipTotal * 0.15;
const totalBill = preTipTotal + tipAmount;
const message1 = "Your tip is ";
const message2 = "<br>Your total bill is ";
document.write(message1 + tipAmount + message2 + totalBill);

RESULTS: Your tip is 1.5
         Your total bill is 11.5  # Looks like true

# AND(??) and OR(&&) operators

if (taxRate >= 0 && taxtRate < 1) {
        const retailPrice = totalPrice / (1 + taxRate);
        document.write(retailPrice);
} else {
        document.write("Please enter a tax rate between 0 and 1.");
}

#1 js events
# click event

HTML:

<div id="my-div"></div>
<button id="my-button">Click to add some text, above</button>

JavaScript:

    const myButton = document.getElementById('my-button');
    myButton.addEventListener('click', function() {
        const myDiv = document.getElementById('my-div');
        myDiv-innerHTML = '<h1>Hello Click World!</h1>';
});

# if you want to run some code after the web page document has loaded
# add an event handler
document.addEventListener('DOMContentLoaded', function() {
    console.log('We are loaded!');
});

# keypress event

HTML:

<div>
  Type a key:
</div>
<input id="key-input" type="text">
<div>
  Here`s the code of the key you pressed:
</div>
<div id="key-output">
</div>

JavaScript:

const keyInput = document.getElementById('key-input');
keyInput.addEventListener('keypress', function(e) {
    const keyOutput = document.getElementById('key-output');
    keyOutput.innerHTML = e.which;
});

# event prevent link

HTML

<a href="https://yandex.ru/">Yandex</a><br>
<a href="https://wikipedia.org/">Wiki</a>
<a href="https://myfin.by">MyFin</a>

<div id="output">
Link URL:
</div>

JavaScript

const links = document.getElementsByTagName('a')
for (const link of links) {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            strURL = e.target.href;
            document.getElementById('output').innerHTML = 'Link URL:' + strURL;
    })
}

# Iteration through the array

// Declare the array
const dogPhotos= ["dog-1", "dog-2", "dog-3", "dog-4", "dog-5"];

// Iterate through the array
dogPhotos.forEach((value, index) => {
    console.log("Element " + index + " has the value " + value);
});

# Iterate  with for

// Declare the array
const dogPhotos= ["dog-1", "dog-2", "dog-3", "dog-4", "dog-5"];

// Iterate through the array
for (const currentPhoto of dogPhotos) {
        console.log("The current element has the value " + currentPhoto);
}

#2 Extracting information about a time

HTML

<div id="output"></div>

JavaScript

const timeNow = new Date();
const hoursNow = timeNow.getHours();
const minutesNow = timeNow.getMinutes();
let message = "It's";
let hoursText;

if (minutesNow <= 30) {
        message += minutesNow + (minutesNow === 1 ? " minute past "
            : " minutes past ");
        hoursText = hoursNow;
} else {
        message += (60 - minutesNow) + ((60 - minutesNow) === 1 ? "
        minute before " : "minutes before ");
        hoursText = hoursNow + 1;
}
if (hoursNow == 0 && minutesNow <= 30) {
        message += "midnight.";
} else if (hoursNow == 11 && minutesNow > 30) {
        message += hoursText + " noon.";
} else if (hoursNow < 12) {
        message += hoursText + " in the morning.";
} else if (hoursNow == 12 && minutesNow <= 30) {
        message += "noon.";
} else if (hoursNow < 18) {
        message += parseInt(hoursText - 12) + " in the afternoon.";
} else if (hourNow == 23 && minutesNow > 30) {
        message += "midnight.";
} else {
        message += parseInt(hoursText - 12) + " in the evening.";
}
document.getElementById("output").innerHTML = message;

#3 Extracting month name from a date

HTML

<div id="output"></div>

JavaScript

const dateNow = newDate();
document.getElementById("output").innerHTML = 
`The date is ${dateNow}<br>
The month name is ${dateNow.toLocaleDateString('default', {
    month: 'long' })}`;

#4 Extracting the day name from a date

HTML

<div id="output"></div>

JavaScript

const dateNow = new Date();
document.getElementById("output").innerHTML = 
`The date is ${dateNow}<br>
The month name is ${dateNow.toLocalDateString('default', {
    weekday: 'long' })}`;

#5 const with UPPERCASE is count

const ONESECOND = 1000;  # 1 sec == 1000 msec
const ONEMINUTE = ONESECOND * 60;
const ONEHOUR = ONEMINUTE * 60;
const ONEDAY = ONEHOUR * 24;
const ONEWEEK = ONEDAY * 7;

#6 Quick conversation a string to a number

const numOfShois = '2';
const numOfSocks = 4;
const totalItems = +numOfShoes + numOfSocks;

RESULTS:
6

#7 
