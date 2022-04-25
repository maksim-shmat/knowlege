"""Examples for backend."""

#1 check list of values

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")
results:
    Adding mushrooms.
    Adding green pappers.
    Adding extra cheese.

    Finished making your pizza!

#2 if for
# green peppers is end at all

if requested_topping == 'green peppers':
    print("Sorry, we are out of green peppers right now.")
else:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

results:
    Adding mushrooms.
    Sorry, we are out of green peppers right now.
    Adding extra cheese.

    Finished making your pizza!

#3 check empty list

requested_toppings = []
if requested_toppings:
    for requested_toppings in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#4 get list of all available items and one not commonly request

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese'] # if it concreet list use touple
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# not commonly request - 'french fries'

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished maiking your pizza!")

results:
    Adding mushrooms.
    Sorry, we don`t have french fries.
    Adding extra cheese.
    
    Finished making your pizza!

#5 Backend work with dicts

alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

resutls:
    You just earned 5 points!

#6 Check changable position

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Alien move fast
    x_increment = 3

# New position equals of sum privious position and increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

#7 work with input and integer values

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

#8 % return end of integer for check even or odd number

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

#9
