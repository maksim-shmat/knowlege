""" Puch coin 1000 ones and tel how eagles up."""

import random
print("I have push one coin 1000 ones. Tell me how many ones eagle up? Push the button Enter thats start.")
input()
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0, 1) == 1:
        heads = heads + 1
    flips = flips + 1
    if  flips == 900:
        print('900 up`s and "Eagle" down in ' + str(heads) + 'ones.')
    if flips == 100:
        print('For 100 up`s, "Eagle" down in ' + str(heads) + 'ones.')
    if flips == 500:
        print('Halfpath is going and "Eagle" down in ' + str(heads)
                + 'ones.j')

print()
print('From 1000 up`s coin is "Eagle" down in' + str(heads) + 'ones!')
print('How you doing?')
