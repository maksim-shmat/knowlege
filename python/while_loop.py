"""While looping statement."""

# print 1 to n using while loop

n = 4
i = 1
while i<=n:
    print(i)
    i += 1

###### while loop with break statement

a = 4
i = 0
while i<a:
    print(i)
    i+=1
    if i>1:
        break

###### while loop with continue

a = 4
i = 0
while i<a:
    if i==2:
        i+=1
        continue
    print(i)
    i+=1

######
