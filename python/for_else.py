"""For-if-else vs for-if-if with break."""

my_list = ['some', 'list', 'containing', 'five', 'elements']

min_len = 3

for element in my_list:
    if len(element) < min_len:
        print(f'Caught an element shorter than {min_len} letters')
        break
else:
    print(f'All elements at least {min_len} letters long')

###
my_list = ['some', 'list', 'containing', 'five', 'elements']

min_len = 3

no_break = True
for element in my_list:
    if len(element) < min_len:
        print(f'Caught an element shorter than {min_len} letters')
        no_break = False
        break

if no_break:
    print(f'All elements at least {min_len} letters long')
