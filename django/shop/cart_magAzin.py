""" Second file from create shop, make a cart."""

### add to settings.py
CART_SESSION_ID = 'cart'

# next
python mangage.py startapp cart

add app to settings.py
INSTALLED_APPS = [
        ...
        'shop.apps.ShopConfig',
        'cart.apps.CartConfig',
]

# next
