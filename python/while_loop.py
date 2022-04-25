"""While looping statement."""

# print 1 to n using while loop

n = 4
i = 1
while i<=n:
    print(i)
    i += 1

###### while loop with break statement

a = 4
i = 0
while i<a:
    print(i)
    i+=1
    if i>1:
        break

###### while loop with continue

a = 4
i = 0
while i<a:
    if i==2:
        i+=1
        continue
    print(i)
    i+=1

#4 run program while user not wrote 'quit'

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)

#5 use 'Flag' for potentially game over

prompt = "\n Tell me something:"
prompt += "\nEnter 'quit' to game over. "

active = True  # that's a flag
while active: # while is work if variable is true 
    message = input(prompt)
    if message == 'quit':
        active = False  # check the flag
    else:
        print(message)

#6 while Tru3 and break

prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:  # run infinity
    city = input(prompt)
    if city == 'quit':
        break  # stop run
    else:
        print(f"I'd love to go to {city.title()}!")

#7 while and continue

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:  # if odd 
        continue
    print(current_number)

results:
    1
    3
    5
    7
    9

#8 infinite cicle

x = 1
while x <= 5:
    print(x)
    x += 1  # ok, prevent infinite cicle

x = 1
while x <= 5:
    print(x)
results:
    1
    1
    1
    # infinite cicle

#9 Backend problem: verifiying users.

unvonfirmed_users = ['alice', 'brian', 'candice']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

results:
    Verifying user: Candice
    Verifying user: Brian
    Verifying user: Alice

    The following users have been confirmed:
        Candice
        Brian
        Alice

#10 Remove concrete values in a whole list

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

results:
    ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
    ['dog', 'dog', 'goldfish', 'rabbit']

#11 Backend: question list

responses = {}  # save results in the dict

polling_active = True  # run questions more and more

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

results:
    What is your name? Eric
    Which mountain would you like to climb someday? Alpine
    Would you like to let another person respond? (yes/ no) yes

    What is your name? Lynn
    Which mountain would you like to climb someday? Plombire
    Would you like to let another person respond? (yes/ no) no

    --- Poll Results ---
    Lynn would like to climb Plombire.
    Eric would like to climb Alpine.

#12
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print('Printing task is done.')

#13 while else with file reading

f = open("scramble.py", "r")
while True:
    line = f.readline()
    if not line:
        break
    print(line.strip())
else:
    f.close

#14 function in while cicle

def get formatted_name(first_name, last_name):
    """Return formatted full name."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
# !!! INFINITE CICLE..................

while True:
    print("\nPlease tell me your name:")
    print("(Enter 'quit' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'quit':
        break

    l_name = input("Last name: ")
    if f_name == 'quit':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

#15
