"""How make double break from two cicle or more."""

# Check all pairs of char in a string and stop how find two equels chars.

# bad
s = "something string"
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            print(i, j)
            break # but how outher from two cicles?

###### bad with func and return

def func():
    s = "teste"
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                print(i, j)
                return
func()

###### bad with exception

try:
    s = "teste"
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                print(i, j)
                raise Exception()
except:
    print("the end")

###### bad with bool

exitFlag = False
s = "teste"
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            print(i, j)
            exitFlag = True
            break
    if(exitFlag):
        break

###### bad while 

s = "teste"
i = 0
j = 1
while i <len(s):
    if s[i] == s[j]:
        print(i, j)
        break
    j = j + 1
    i = i + j // len(s)
    j = j % len(s)

###### good

def unique_pairs(n):
    for i in range(n):
        for j in range(i+1, n):
            yield i, j

s = "a string to example"
for i, j in unique_pairs(len(s)):
    if s[i] == s[j]:
        print(i, j)
        break

###### good
itertools.combinations(s, 2)
