"""App orders shop about."""

python manage.py startapp orders

INSTALLED_APPS = [
        ...
        'orders.apps.OrdersConfig',
]

# next
make models.py

# next
python manage.py makemigrations
python manage.py migrate

# next
add models into admin site
orders/admin.py

# next
add orders/forms.py
class OrderCreateForm
    class Meta
    model = Order
    fields =
# next
add handler for forms into orders/views.py

# next
make file orders/urls.py
urlpatterns = [
        path('create/'...)

# next
add path from orders/urls.py into maksimshmat/urls.py

# next
refactor cart/detail.html
<a href ="#"..>
add to "#" <a href="{% urk "orders:order_create" %}" class="button">
  Checkout
</a>

# next
make a structure: templates/orders/order/create.html created.html

# next trubles with Decimal and JSON
python3.8 -m pip install simplejson  # for exit from trumbles Decimal/JSON
or pip3 install simplejson

import simplejson as json
from decimal import Decimal

# next

