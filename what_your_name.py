""" Docs. """

name_age = {}
for i in range(3):
    name = input("Name? ")
    age = int(input("Age? "))
    name_age[name] = age
name_choice = input("Name to find? ")
print(name_age[name_choice])
