"""Ternary operator about."""

#1 classic if/else form

order_total = 221  # gil

if order_total > 100:
    discount = 25 # gil
else:
    discount = 0  # gil
print(order_total, discount)

#1.1 ternary operator

discount = 25 if order_total > 100 else 0
print(order_total, discount)

#2
