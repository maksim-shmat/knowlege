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

#4 
