"""That is example with asterisk into variable."""

def print_sum(*numbers):
    result = 0
    for x in numbers:
        result += x
        print(result)

print_sum(10,20,30,40) 
# 10, 30, 60, 90

