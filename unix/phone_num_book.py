"""Work with dictionries."""

# Make a simle db

people = {
        'Alice': {
            'phone': '2341',
            'addr': 'Foo drive 23'
        },
        'Beth': {
            'phone': '9102',
            'addr': 'Bar street 42'
        },
        'Cecil': {
            'phone': '3158',
            'addr': 'Baz avenue 90'
        }
}

# Descriptive labels for the phone numbers and address. These will be used
# when printing the output.
labels = {
        'phone': 'phone number',
        'addr': 'address'
}

name = input('Name:')

# Are we looking for a phone number or an address?
request = input('Phone number(p) or address(a)?')

# Use the correct key:

key = request # In case the request is neither 'p' not 'a'
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

# Use get to provide default values:

person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')
print("{}'s {} is {}.".format(name, label, result))

# Only try to print information if the name is f valid key in our dictionary
if name in people: print("{}'s {} is {}.".format(name, labels[key],
    people[name][key]))
