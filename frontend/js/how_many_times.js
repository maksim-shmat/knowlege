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
