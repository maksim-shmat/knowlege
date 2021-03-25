"""Loops, Iterators, and Generators."""

###### Python implicit iterator behavior

astring = 'coffee'
coffee_types = ['Cappuccino','Latte','Macchiato']
address = {'city':'San Diego','state':'CA','country':'US'}

# Standard for loop, with implicit iterator
for letter in astring:
    print(letter)

# Loop with enumerator (counter)
for counter,letter in enumerate(astring):
    print(counter,letter)

# Standard for loop, with implicit iterator
for coffee in coffee_types:
    print(coffee)

# Loop with enumerator (counter), starting at 1
for counter,coffee in enumerate(coffee_types,start=1):
    print(counter,coffee)

# Standard for loop, with implicit iterator
for key,value in address.items():
    print(key,value)

# Standard for loop, with implicit iterator
for address_key in address.keys():
    print(address_key)

# Standard for loop, with implicit iterator
for address_value in address.values():
    print(address_value)

###### Python explicit iterator behavior

astring = 'coffee'
coffee_types = ['Cappuccino','Latte','Macchiato']

# Create explicit iterators
astring_iter = iter(astring)
coffee_types_iter = iter(coffee_types)

# Print iterator types
print(type(astring_iter))
print(type(coffee_types_iter))

# Call next() to advance over the iterator
# In Python 2 next() works the same (e.g. astring_iter.next())
# In Python 3 __next__() works the same (e.g. astring_iter.__next__())

# >>> next(astring_iter)
# 'c'

# Call next() to advice over the iterator
# In Python 3 __next__() works the same (e.g. coffee_types.__next__())
# >>> next(coffee_types_iter)
# 'Cappuccino'

order_numbers = iter([1,2,3,4,5,6,7,8,9,10])
# Get order number
# next(order_numbers)

###### Python generator behavior

def funky_order_numbers():
    yield 100
    yield 350
    yield 575
    yield 700
    yield 950

order_numbers = funky_order_numbers()
print(type(order_numbers))
# Call next() to advance over the generator
# >>> next(order_numbers)
# 100

def generate_order_numbers(n):
    for i in range(1,n):
        yield i

regular_order_numbers = generate_order_numbers(100)
# Call next() to advance over the generator
# >>> next(regulat_order_numbers)
# 1

def generate_infinite_order_numbers(n):
    while True:
        n += 1
        yield n

infinite_order_numbers = generate_infinite_order_numbers(1000)
# Call next() to advance over the generator
# >>> next(infinite_order_numbers)
# >>> 1001
# next() never reaches end due to infinite 'while True:' statement

###### List Comprehensions, Generator Expressions, Maps, and Filters
# Python list comprehensions

country_codes = ['us','ca','mx','fr','ru']
zipcodes = {90003:'Los Angeles',90802:'Long Beach',91501:'Burbank',92101:'San Diego',92139:'San Diego',90071:'Los Angeles'}

# Regular syntax
country_codes_upper_std = []
for country_code in country_codes:
    country_codes_upper_std.append(country_code.upper())

# Equivalent list comprehension
country_codes_upper_comp = [cc.upper() for cc in country_codes]

# Regular syntax
zip_codes = []
for zipcode in zipcodes.keys():
    zip_codes.append(zipcode)

# Equivalent list comprehension
zip_codes_comp = [zc for zc in zipcodes.keys()]

# Regular syntax
zip_codes_la = []
for zipcode,city in zipcodes.items():
    if city == "Los Angeles":
        zip_codes_la.append(zipcode)

# Equivalent list comprehension
zip_codes_la_comp = [zc for zc,city i zipcodes.items() if city == "Los Angeles"]

# Regular syntax
one_to_onehundred = []
for i in range(1,101):
    one_to_onehundred.append(i)

# Equivalent list comprehension
one_to_onehundred_comp = [i for i in range(1,101)]

### The last example an inefficient because list require more memory to store data

###### Python generator expressions

one_to_onehundred_genexpression = (i for i in range(1,101))
print(type(one_to_onehundred_genexpression))
one_to_onehundred_genexpression.next()
one_to_onehundred_genexpression.next()

first_fifty_even_numbers = (i for i in ange(2, 101, 2))
first_fifty_even_numbers.next()
first_fifty_even_numbers.next()

first_fifty_odd_numbers = (i for i in range(1, 101, 2))
first_fifty_odd_numbers.next()
first_fifty_odd_numbers.next()

###### Python map() and filter() examples

country_codes = ['us', 'ca', 'mx', 'fr', 'ru']
zipcodes = {90003: 'Los Angeles', 90802:'Long Beach', 91501:'Burbank',92101:'San Diego',92139:'San Diego',90071:'Los Angeles'}

# List comprehension
country_codes_upper_comp = [cc.upper() for cc in country_codes]

# Helper function
def country_to_upper(name):
    return name.upper()

# Map function
country_codes_upper_map = map(country_to_upper,country_codes)

# List comprehension
zip_codes_la_comp =[zc for zc,city in zipcodes.items() if city == "Los Angeles"]

# Helper function
def only_la(dict_item):
    if dict_item[1] == "Los Angeles":
        return True

# Filter function
zip_codes_la_filter_dict_items = filter(only_la,zipcodes.items())
print(zip_codes_la_filter_dict_items)
zip_codes_la_filter = [tup[0] for tup in zip_codes_la_filter_dict_items]

###### Python map() and filter() examples

country_codes = ['us','ca','mx','fr','ru']
zipcodes = {90003:'Los Angeles',90802:'Long Beach',91501:'Burbank',92101:'San Diego',92139:'San Diego',90071:'Los Angeles'}

# List comprehension
country_codes_upper_comp = [cc.upper() for cc in country_codes]

# Helper function
def country_to_upper(name):
    return name.upper()

# Map function
country_codes_upper_map = map(country_to_upper,country_codes)

# List comprehension
zip_codes_la_comp = [zc for zc,city in zipcodes.items() if city == "Los Angeles"]

# Helper function
def only_la(dict_item):
    if dict_item[1] == "Los Angeles":
        return True

# Filter function
zip_codes_la_filter_dict_items = filter(only_la,zipcodes.items())
print(zip_codes_la_filter_dict_items)
zip_codes_la_filter = [tup[0] for tup in zip_codes_la_filter_dict_items]

###### Lambda Keyword for Anonymous Methods
# lambda x: <logic_on_x> is sensual equals def anon_method(xa0: <logic_on_x>

# Python lambda examples

country_codes = ['us','ca','mx','fr','ru']
zipcodes = {90003:'Los Angeles',90802:'Long Beach',91501:'Burbank',92101:'San Diego',92139:'San Diego',90071:'Los Angeles'}

# Map function with lambda
country_codes_upper_map = map(lambda x: x.upper(),country_codes)

# Filter function with lambda
zip_codes_la_filter_lambda_dict_items = filter(lambda (zipcode,city): city == "Los Angeles",zipcodes.items())
print(zip_codes_la_filter_lambda_dict_items)
zip_codes_la_filter = [tup[0] for tup in zip_codes_la_filter_lambda_dict_items]

######
