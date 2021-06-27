"""Change types."""

# integer
n = 100

# float
f = float(n)
print(f)
print(type(f))

# string
s = str(n)
print(s)
print(type(s))

######
# float
f = 100.05

# integer
n = int(f)
print(n)
print(type(n))

# string
s = str(f)
print(s)
print(type(s))

###### don't right
# string
s = '132.65'

# typecase to integer
n = int(s)
print(n)
print(type(n))

# typecast to float
f = float(s)
print(f)
print(type(f))

### first change it in float
# string
s = '132.564'

# typecast to integer
n = int(float(s))
