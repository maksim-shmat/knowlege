"""For my store may be."""

from datetime import date, timedelta

today = date.today()
tomorrow = today + timedelta(days=1)  # today + 1 day is tomorrow
products = [
        {'sku': '1', 'expiration_date': today, 'price': 100.0},
        {'sku': '2', 'expiration_date': tomorrow, 'price': 50},
        {'sku': '3', 'expiration_date': today, 'price': 20},
]

for product in products:
    if product['expiration_date'] != today:
        continue
    product['price'] *= 0.8  # equivalient to applying 20% discont
    print(
            'Price for sku', product['sku'],
            'is now', product['price'])

#2 coupons

customers = [
        dict(id=1, total=200, coupon_code='F20'),  # F20: fixed, $20
        dict(id=2, total=150, coupon_code='P30'),  # P30: percent, 30%
        dict(id=3, total=100, coupon_code='P50'),  # P50: percent, 50%
        dict(id=4, total=110, coupon_code='F15'),  # F15: fixed, $15
]

for customer in customers:
    code = customer['coupon_code']
    if code == 'F20':
        customer['discount'] = 20.0
    elif code == 'F15':
        customer['discount'] = 15.0
    elif code == 'P30':
        customer['discount'] = customer['total'] * 0.3
    elif code == 'P50':
        customer['discount'] = customer['total'] * 0.5
    else:
        customer['discount'] = 0.0

for customer in customers:
    print(customer['id'], customer['total'], customer['discount'])

#2.1 coupons.dict

customers = [
        dict(id=1, total=200, coupon_code='F20'),  # F20: fixed, $20
        dict(id=2, total=150, coupon_code='P30'),  # P30: percent, 30%
        dict(id=3, total=100, coupon_code='P50'),  # P50: percent, 50%
        dict(id=4, total=110, coupon_code='F15'),  # F15: fixed, $15
]

discounts = {
        'F20': (0.0, 20.0),  # each value is (percent, fixed)
        'P30': (0.3, 0.0),
        'P50': (0.5, 0.0),
        'F15': (0.0, 15.0),
}

for customer in customers:
    code = customer['coupon_code']
    percent, fixed = discounts.get(code, (0.0, 0.0))
    customer['discount'] = percent * customer['total'] + fixed

for customer in customers:
    print(customer['id'], customer['total'], customer['discount'])

#3 dicscount with Class

class Price:
    def final_price(self, vat, discount=0):
        """Return price after applying vat and fixe discount."""
        return(self.net_price * (100 + vat) / 100) - discount

p1 = Price()
p1.net_price = 100
print(Price.final_price(p1, 20, 10))  # 110 (100 * 1.2 - 10)
print(p1.final_price(20, 10))  # equivalent
