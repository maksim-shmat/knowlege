""" Second file from create shop, make a cart."""

### add to settings.py
CART_SESSION_ID = 'cart'

# next
python manage.py startapp cart

add app to settings.py
INSTALLED_APPS = [
        ...
        'shop.apps.ShopConfig',
        'cart.apps.CartConfig',
]

# next
add cart.py to cart/
add class Cart
def __init__(self, request)
def add(self, product, quantity=1, update_quantity=False)
def save(self)
def remove(self, product)
def __iter__(self)
def __len__(self)
def get_total_price(self)
def clear(self)

# next
add forms.py to cart/
class CartAddProductForm(forms.Form)

# next
add to cart/views.py
@require_POST
def cart_add(request, product_id)
def cart_remove(request, product_id)
def cart_detail(request)

# next
add urls.py/cart

# next
add path('cart/'...) to urls.py/maksimshmat

# next
add templates/cart/detail.html

# next
add "Add to cart" button into product page
views.py/shop
add cart_product_form

# next
add to templates/shop/product/detail.html "csrf_token"

# next
add update button and quantity form into the detail.py
<td>
  <form action="{% url "cart:cart_add" product.id..."

# next
create context_processors.py/cart

add 'cart.context_processors.cart' into settings.py

add to shop/base.html
<div class="cart">
{% with total_items=cart...}

# next
add to .gitignore --- .env ---

