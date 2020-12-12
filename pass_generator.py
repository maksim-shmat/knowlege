import random
from string import digits
from string import punctuation
from string import ascii_letters

symbols = ascii_letters + digits + punctuation
sequre_random = random.SystemRandom()
password = "".join(sequre_random.choice(symbols) for i in range(20))
print('This information is class Five', password)
x = random.choice(['Petrusha', 'Dundik', 'Hitrojopus'])
print(x)
petuhani = ['Dimon', 'Shkurionka', 'Jidopolus']
random.shuffle(petuhani)
print(petuhani)
