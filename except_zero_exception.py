x = int(input("Please enter an integer: "))
y = int(input("Please enter another integer: "))

try:
    z = x/y
except ZeroDevisionError as e:
    print("Can't divide by zero.")

