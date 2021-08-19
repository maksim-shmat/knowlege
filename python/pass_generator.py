import random
from string import digits
from string import punctuation
from string import ascii_letters

symbols = ascii_letters + digits + punctuation
sequre_random = random.SystemRandom()
password = "".join(sequre_random.choice(symbols) for i in range(20))
print('This information is class Five', password)
x = random.choice(['Propose', 'Endorse', 'Rejected'])
print(x)
petuhani = ['First', 'Second', 'Third']
random.shuffle(petuhani)
print(petuhani)

###### alter

import random
import string

N = 20 # password length

# allowed string constants
allowedChars = string.ascii_letters + string.digits + string.punctuation

# generate password
password = ''.join(random.choice(allowedChars) for _ in range(N))

print(password)

######
