"""Shopping list for example."""

# This is my shoplist

shoplist = ['apples', 'mango', 'peacock', 'bananas']

print('I need delt', len(shoplist), 'targets.')

print('Targets:', end=' ')

for item in shoplist:
    print(item, end=' ')

print('\nThen need me buy of rice.')
shoplist.append('rice')

print('Now my shoplist then:', shoplist)
print('Sort it')
shoplist.sort()
print('Sorted shoplist look at that:', shoplist)

print('First, that need me buy, it', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Check', olditem)
print('Then my shoplist then:', shoplist)
