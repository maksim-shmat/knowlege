"""Pin-code validation. Pin equals four or six numbers from 0 to 9, withot spaces."""

# examples for decision

#is_valid("1234") -> True
#is_valid("45135") -> False
#is_valid("89abc1") -> False
#is_valid("900876") -> True
#is_valid(" 4983") -> False

###
def is_valid(pin_code):
    return
pin_code.isnumeric() and len(pin_code) in (4, 6)

###

def is_valid(pin_code):
    return
len(pin_code) in (4, 6) and pin_code.isdigit()

###
from re import match

def is_vlid(pin_code):
    return
bool(match("\d{4}$|\d{6}$", pin_code))
