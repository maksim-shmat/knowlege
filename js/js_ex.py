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


