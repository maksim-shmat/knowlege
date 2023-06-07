"""string about."""

#1 Quick way of makeing a copy

>>> s[:]

#2 slicing, start, stop and step

>>> s[2:11:3]

#3 string formating

greet_old = 'Hello %s!'
greet_old % 'Fernando'
'Hello Feranndo!'

greet_positional = 'Hello {} {}!'
greet_positional.format('Fernando', 'Romeo')
'Hello Fernando Romeo!'

greet_positional_idx = 'This is {0}! {1} loves {0}!'
greet_positional_idx.format('Blohai', 'Fernando')
'This is Blohai! Fernando loves Blohai!'

keyword = 'Hello, my name is {name} {last_name{'
keyword.format(name='Comprendo', last_name='Ruri')
'Hello, my name is Comprendo Ruri'

