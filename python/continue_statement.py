"""Python Continue Statement examples."""

i = 1
while i <= 10:
    if i == 4 or i == 7:
        i += 1
        continue
    print(i)
    i += 1

##### continue with loop and range

for x in range(1, 11):
    if x%3 == 0:
        continue
    print(x)

###### break statement with for loop and list

myList = [9, 1, 5, 9, 4, 9, 7, 2, 9]

for x in myList:
    if x == 9:
        continue
    print(x)
