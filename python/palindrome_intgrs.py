"""From two twogrades integer palindrome equals 9009 = 91 * 99
   Where is thirdgrades integer palindrome?
"""

def polindrom():
    for n in range(999, 99, -1):
        for m in range(999, 99, -1):
            string = str(n * m)
            if string == string[::-1]:
                return string

###### 906
def rev(s):
    t = ''
    t = s[::-1]
    return t
ma = -100000000000
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        if rev(str(i*j)) == str(i * j):
            ma = max(ma, i * j)
print(ma)

###### 906
n = [i * j for i in range(100, 999) for j in range(100, 999)]

biggest = 0

for i in n:
    if str(i) == str(i)[::-1]:
        if i > biggest:
            biggest = i
print(biggest)

###### 906
x = 100
lst = []

while x < 1000:
    for i in range(x, 1000):
        temp = str(i * x)
        if temp[:] == temp[::-1]:
            lst.append(temp)
    x += 1
print(max(int(i) for i in lst))

###### 906
max_pal = max([i*j for i in range(100, 1000) for j in range(100, 1000) if str(i * j) == str(i*j)[::-1]])

print(max_pal)

###### 906
def  is_palindrom(data):
    return data == data[::-1]

max = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        if is_palindrom(str(i * j)) > max:
            max = i * j

###### 580
def is_pallindrom(data):
    return data == data[::-1]

max = 0
def search(max):
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if is_pallindrom(str(i * j)):
                max = i * j
            if is_palindrom(str(i * j)) < max:
                return max
print(search(max))
