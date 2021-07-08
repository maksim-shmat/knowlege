"""Work with a dicts."""

# extracting dictionary element using its key

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

### setting dictionary element using its key

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

### looping through a dictionary object

dict_keys = dict_salesinfo.keys()
print(dict_keys)
print(type(dict_keys))
print()

### and more
for var in dict_keys:
    print(var + ":" + str(dict_salesinfo[var]))
    print()

### printing dictionary object values in key, value pair

dict_values = dict_salesinfo.values()
print(dict_values)
print()

### the item function converts a dictionary item into a tuple

dict_items = dict_salesinfo.items()
print(dict_items)
print(type(dict_items))
print()

### looping through the items function

for key, value in dict_salesinfo.items():
    print(key + "-" + str(value))
    print()

### converting a list into a dictionary object

sales_infolist = [['SID', 'Fiat'], ['Sales', '20000'], ['LaunchDay', 'Wed'], ['Cost', '5000000']]
print(type(sales_infolist))
print()
sales_infolist_dict = dict(sales_infolist)
print(type(sales_infolist_dict))
print()

### copying a dictionary into a new dictionary
dict_salesinfo_new = dict_salesinfo.copy()
print(dict_salesinfo_new)
print()

### updating the dictionary object

dict_salesinfo = {'SID': 'Fiat', 'Sales': 20000, 'LaunchDay': 'Wed', 'Cost': 500000}
print(dict_salesinfo)
