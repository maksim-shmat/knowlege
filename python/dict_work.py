"""Work with a dicts."""

######0 Add items to dictionary

myDictionary = {
        'a': '65',
        'b': '66',
        'c': '67'
}

myDictionary['d'] = '68'
myDictionary['e'] = '69'
myDictionary['f'] = '70'

print(myDictionary)
print('next')

######1 extracting dictionary element using its key

dict_salesid = {'SID1': "Fiat",
                'SID2': "Mersedes",
                'SID3': "Maruti",
                'SID4': "Volkswagen",
                'SID5': "Kia"}

dict_salesinfo = {'SID': "Fiat",
                  'Sales': 20000,
                  'LaunchDay': 'Wed',
                  'Cost': 500000}

print(len(dict_salesid))
print()

### extract

sales_id = 'SID2'
if sales_id in dict_salesid:
    name = dict_salesid[sales_id]
    print('Sales ID is {}, Sales name is {}'. format(sales_id, name))
    print()
else:

    print('Sales ID {} not found'.format(sales_id))
    print()

######2 setting dictionary element using its key

dict_salesinfo['LaunchDay'] = 'Thurs'
dict_salesinfo['Cost'] = 6000000
LaunchDay = dict_salesinfo.get('LaunchDay')
Cost=dict_salesinfo.get('Cost')
print('Launchday is {}, Cost is {}'.format(LaunchDay, Cost))
print()

######!2 Delete items from dictionary using del keyword

myDictionary = {
        'a': '65',
        'b': '66',
        'c': '67'
}
del myDictionary['c']
print(myDictionary)
print('above - delete with del')
print()

### Delete items from dictionary using pop()

myDictionary = {
        'a': '65',
        'b': '66',
        'c': '67'
}
poppedItem = myDictionary.pop('c')
print(poppedItem)
print(myDictionary)
print('above - delete with pop() example')
print()

### Clear all items of a dictionary

myDictionary = {
        "a": 65,
        "b": 66,
        "c": 67
}
print('Dictionary items:\n', myDictionary)
myDictionary.clear()
print('Dictionary items after clear():\n', myDictionary)


######3 looping through a dictionary object

dict_keys = dict_salesinfo.keys()
print(dict_keys)
print(type(dict_keys))
print()

### and more
for var in dict_keys:
    print(var + ": " + str(dict_salesinfo[var]))
    print()

######4 printing dictionary object values in key, value pair

dict_values = dict_salesinfo.values()
print(dict_values)
print()

######5 the item function converts a dictionary item into a tuple

dict_items = dict_salesinfo.items()
print(dict_items)
print(type(dict_items))
print()

######6 looping through the items function

for key, value in dict_salesinfo.items():
    print(key + "-" + str(value))
    print()

######7 copying a dictionary into a new dictionary
dict_salesinfo_new = dict_salesinfo.copy()
print(dict_salesinfo_new)
print()

######8 updating the dictionary object

dict_salesinfo = {'SID': 'Fiat', 'Sales': 20000, 'LaunchDay': 'Wed', 'Cost': 500000}
print(dict_salesinfo)

####
names = dict(hello=1, world=2)
' '.join(names)
# 'hello world'

print()

######9 sort dict for value

d = {'apples':40, 'oranges':80, 'bananas':70}
print(sorted(d, key=d.get))

print()

######10 generator dict and set

S = {i**2 for i in range(10)}
D = {i: i**2 for i in range(10)}
print(S)
print(D)
print()

######11 Python dictionary methods
### clear()

dictionary = {"a": 4, "b": 5, "c": 6}
dictionary.clear()
print(dictionary)

### copy()

dictionary = {"a": 4, "b": 5, "c": 6}
dictionary_1 = dictionary.copy()
dictionary_1["b"] = 2
print(dictionary)
print(dictionary_1)

### fromkeys()

dictionary = {"a": 4, "b": 5, "c": 6}
dictionary_1 = dict.fromkeys(dictionary, 1)
print(dictionary_1)

### get()

dictionary = {"a": 4, "b": 5, "c": 6}
x = dictionary.get("b")
print(x)

### items()

dictionary = {"a": 4, "b": 5, "c": 6}
for key, value in dictionary.items():
    print(key, '-', value)  # or print(key)

### keys()

dictionary = {"a": 4, "b": 5, "c": 6}
for key in dictionary.keys():
    print(key)

### values()

dictonary = {"a": 4, "b": 5, "c": 6}
for value in dictionary.values():
    print(value)

### pop() removes the key-value pair

dictionary = {"a": 4, "b": 5, "c": 6}
x = dictionary.pop("b")
print(x)
print(dictionary)

### popitem() removes the last inserted key-value pair

dictionary = {"a": 4, "b": 5, "c": 6}
x = dictionary.popitem()
print(x)
print(dictionary)

### setdefault()

dictionary = {"a": 4, "b": 5, "c": 6}
x = dictionary.setdefault("b")
print(x)
y = dictionary.setdefault("m", 0)
print(y)
print(dictionary)

### update()

dictionary = {"a": 4, "b": 5, "c": 6}
dictionary_1 = {"a": 8, "m": 2, "v": 7}
dictionary.update(dictionary_1)
print(dictionary)
print('next')

######12 Create dictionary using dict comprehencion

def someThing(x):
    x = x**3
    return x

myDict = {x: someThing(x) for x in (5, 8, 9, 12)}
print(type(myDict))
print(myDict)

### create dictionary with keyword argument to dict()

myDict = dict(a='foo', b='bar', c='moo')
print(type(myDict))
print(myDict)

### create dictionary using dict() constructor

myDict = dict([(1, 'foo'), (2, 'bar'), (3, 'moo')])
print(type(myDict))
print(myDict)
print('next')

######13 check if dictionary is empty using not operator

myDict = {}
if not myDict:
    print('The dictionary is empty.')
else:
    print('The dictionary is not empty.')

### check if dictionary is empty using len()

myDict = {}
if (len(myDict)) == 0:
    print('The dictionary is empty.')
else:
    print('The dictionary is not empty.')
print('    next')

######14 Check if key is present in dictionary

myDictionary = {
        "name": "Luna",
        "year": 1989,
        "expertise": "data expeliarmos"}
isPresent = 'expertise' in myDictionary
print(isPresent)
print('    next')

######15 Get length of dictionary

myDictionary = {
        "name": "Lini",
        "year": 1989,
        "expertise": "data analytics"}
length = len(myDictionary)
print('Length of dictionary is: ', length)
print('    next')

######16 List of dictionaries
### Create

myList = [
        {
            'foo': 12,
            'bar': 14
        },
        {
            'moo': 52,
            'car': 642
        },
        {
            'doo': 6,
            'tar': 84
        }
]
print(myList)
print(myList[0])
print(myList[0]['bar'])

### Update

myList = [
        {
            'foo': 12,
            'bar': 14,
        },
        {
            'moo': 52,
            'car': 642
        },
        {
            'doo': 6,
            'tar': 84
        }
]
# update value for 'bar in first dict
myList[0]['bar'] = 52

# add a new key: value pair to second dict
myList[1]['gar'] = 38

# delete a key: value pair from third dict
del myList[2]['doo']
print(myList)

### Append a dict to list of dict
myList.append({'joo': 48, 'par': 28})
print(myList)
print('next')

######17 Dictionary keys to list
### using dict.keys()

myDict = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
keysList = list(myDict.keys())
print(keysList)

### using list comprehension

myDict1 = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
keysList1 = [key for key in myDict1]
print(keysList)

### using for loop

myDict2 = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
keysList2 = []
for key in myDict2:
    keysList2.append(key)
print(keysList2)
print('   ^ above dict keys to list')

######18 Dictionary values to list
### Using dict.values()

myDict3 = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
valuesList = list(myDict3.values())
print(valuesList)

### using list comprehension

myDict4 = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
valuesList1 = [myDict4[key] for key in myDict4]
print(valuesList1)

### using for loop

myDict5 = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
valuesList2 = []
for key in myDict5:
    valuesList2.append(myDict5[key])
print(valuesList2)
print('   ^ above dict values to list')

######19
