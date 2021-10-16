"""Work with a dicts."""

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

### delete
# del dict_salesinfo

### delete a specific item
# del dict_salesinfo['SID']

### delete with pop()
# print(dict_salesinfo.pop('SID'))

### delete with clear()
# print(dict_salesinfo.clear())

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

######
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
    print(key, '-', value)

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

######12
