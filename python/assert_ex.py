"""examples with assert."""

x = "hello"
assert x == "hello"
print('Done!')

###### expression is False

x = "hola"
assert x == "hello"
print('Done!')
# Trceback...

###### assert with optional argument

x = "holla"
assert x == "hello", 'The two strings do not match.'
print('Done!')
# Traceback with optional artument only if True
