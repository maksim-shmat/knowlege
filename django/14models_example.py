""" Models for example 4."""

# Django COUNT queries with aggregate(), annotate() and Count()

from coffeehouse.stores.models import Store
from django.db.models import Count

# Get the number of stores (COUNT(*))
stores_count = Store.objects.all().count()
print(stores_count)

# Get the number of stores that have city 'San Diego' (COUNT(*))
stores_san_diego_count = Store.objects.filter(city='San Diego').count()

# Get the number of emails, NULL values are not counted (COUNT(email))
emails_count = Store.objects.aggregate(Count('email'))
print(email_count)
{'email__count': 4}

# Get the number of emails, NULL values are not counted (COUNT(email) AS "coffeehouse_store_emails_count")
emails_count_custom = Store.objects.aggregate(coffeehouse_store_emails_count=Count('email'))
print(emails_count_custom)
{'coffeehouse_store_emails_count': 4}

# Get number of distinct Amenities in all Stores, NULL values not counted (COUNT(DISTINCT name))
different_amenities_count = Store.objects.aggregate(Count('amenities',distinct=True))
print(emails_count_cutom)
{'coffeehouse_store_emails_count': 4}

# Get number of distinct Amenities in all Stores, NULL values not counted (COUNT(DISTINCT name))
different_amenities_count = Store.objects.aggregate(Count('amenities',distinct=True))
print(different_amenities_count)
{'amenities__count': 5}

# Get number of Amenities per Store with annotate
stores_with_amenities_count = Store.objects.annotate(Count('amenities'))
# Get number of Amenities per Store with annotate and custom name
stores_amenities_count_custom = Store.objects.annotate(amenities_per_store=Count('amenities'))
store_amenities_count_custom[0].amenities_per_store

###### Django MAX,MIN,AVG,VARIANCE and STDDEV queries with Max(),Min(),Sum(),Avg(),Variance() and StdDev() classes

from coffeehouse.items.models import Item
from django.db.models import Avg, Max, Min
from django.db.models import Sum
from django.db.models import Variance, StdDev

# Get the average, maximum and minimum number of stock for all Item records
avg_max_min_stock = Item.objects.aggregate(Avg('stock'), Max('stock'), Min('stock'))

print(avg_max_min_stock)
{'stock__avg': 29.0, 'stock__max': 36, 'stock__min': 27}

# Get the total stock for all Items
item_all_stock = Item.objects.aggregate(all_stock=Sum('stock'))
print(item_all_stock)
{'all_stock': 261}

# Get the variance and standard deviation for all Item records
# NOTE: Variance & StdDev returnd the population variance & standard deviation, respectively.
#    But  it's also possible to return sample variance & standard deviation,
#    using the sample=True argument
item_statistics = Item.objects.aggregate(Variance('stock'), std_dev_stock=StdDev('stock'))
{'std_dev_stock': 5.3748, 'stock__variance': 28.8888}

###### Django F() expression update queries

from coffeehouse.items.models import Item
from django.db.models import F

# Get single item
egg_biscuit = Item.objects.get(id=2)
# Check stock
egg_biscuit.stock
2
# Add 10 to stock value with F() expression
egg_biscuit.stock = F('stock') + 10
# Trigger save() to apply F() expression
egg_biscuit.save()
# Check stock again
egg_biscuit.stock
<CombinedExpression: F(stock) + Value(10)>
# Ups, need to re-read/refresh from DB
egg_biscuit.refresh_from_db()
# Check stock again
egg_biscuit.stock
12

# Decrease stock value by 1 for Item records on the Breakfast menu
breakfast_items = Item.objects.filter(menu__name='Breakfast')
breakfast_items.update(stock=F('stock') - 1)

# Increase all Item records stock by 20
Item.objects.all().update(stock=F('stock') + 20)

###### Django F() expression in read queries and aggregate queries

from django.db.models import F, ExpressionWrapper, FloatField
from coffeehouse.items.models import Drink, Item

calories_dbl_caffeine_drinks = Drink.objects.filter(item__calories__gt=F('caffeine')*2)
items_with_assets = Item.objects.annotate(
        assets=ExpressionWrapper(F('stock')*F('price'),
            output_field=FloatField()))

###### Django Func() expressions for SQL functions and Django SQL functions

from django.db.models import F, Func, Value
from django.db.models.functions import Upper, Concat
from coffeehouse.stores.models import Store

# SQL Upper function call via Func expression and F expression
stores_w_upper_names = Store.objects.annotate(name_upper=Func(F('name'), function='Upper'))
stores_w_upper_names[0].name_upper
'CORPORATE'
stores_w_upper_names[0].name
'Corporate'

# Equivalent SQL Upper function call directly with Django SQL Upper function
stores_w_upper_names_function = Store.objects.annotate(name_upper=Upper('name'))
stores_w_upper_name_function[0].name_upper
'CORPORATE'

# SQL Concat function called directly with Django SQL Concat function
stores_w_full_address = Store.objects.annotate(full_address=
        Concat('address',Value(' - '),'city',Value(' , '),'state'))
stores_w_full_address[0].full_address
'624 Broadway - San Diego, CA'
stores_w_full_address[0].city
'San Diego'

###### Django Subquery expression with SQL subquery to get related model data

from django.db.models import OuterRef, Subquery

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    item = models.IntegerField()
    amount = models.IntegerField()
    order = models.ForeignKey(Order)

# Get Items in order number 1
order_items = OrderItem.objects.filter(order__id=1)
# Get item
order_item[0].item
1
# Get item name ?

# OrderItem item field is IntegerField, lacks Item relationship
# Create sub-query to get Item records with id
item_subquery = Item.objects.filter(id=(OuterRef('id')))

# Annotate previous query with sub-query
order_items_w_name = order_items.annotate(item_name=Subquery(item_subquery.values('name')[:1]))
# Output SQL to verify
print(order_items_w_name.query)
SELECT 'online_orderitem'.'id', 'online_orderitem'.'item',
'online_orderitem'.'amount', 'online_orderitem'.'order_id',
(SELECT U0.'name' FROM 'item_item' U0 WHERE U0.'id' = (online_orderitem.'id') LIMIT 1)
AS 'item_name' FROM 'online_orderitem' WHERE 'online_orderitem'.'order_it' = 1
# Access item and item_name
order_item_w_name[0].item
1
order_items_w_name[0].item_name
'Whole-Grain Oatmeal'

###### Django Subquery expression with SQL subquery in WHERE statement

from coffeehouse.online.models import Order
from coffeehouse.items.models import Item
from django.db.models import OuterRef, Subquery

# Get Item records in lastest Order to replenish stock
most_recent_items_on_order = Order.objects.latest('created').orderitem_set.all()

# Get a list of Item records based on recent order using a sub-query
items_to_replenish = Item.objects.filter(id__in=Subquery(
    most_recent_items_on_order.values('item')))

print(items_to_replenish.query)
SELECT 'items_item'.'id', 'items_item'.'menu_id', 'items_item'.'name', 'items_item'.'description', 'items_item'.'size', 'items_item'.'calories', 'items_item'.'price', 'items_item'.'stock' FROM 'items_item' WHERE 'items_item'.'id' IN (SELECT U0.'item' FROM 'online_orderitem' U0 WHERE U0.'order_id' = 1)

###### Django model manager raw() method

from coffeehouse.items.models import Drink, Item

# Get all drink
all_drinks = Drink.objects.raw("SELECT * FROM items_drink")

# Confirm type
type(all_drinks)
# Outputs: <class 'django.db.models.query.RawQuerySet'>

# Get first drink with index 0
first_drink.item.name

# Use parameters to limit a raw SQL query
caffeine_limit = 100

# Create raw() query with params argument to pass dynamic arguments
drinks_low_caffeine = Drink.object.raw("SELECT * FROM items_drink where caffeine < %s",params=[caffein_limit]);

###### Django model manager raw() method with mapping, deferred fields, and aggregate queries
# Map results from legacy table into Item model
all_legacy_items = Item.objects.raw("SELECT product_name AS name, product_description AS description from coffeehouse_products")

# Access legacy results as if they are standard Item model records
all_legacy_items[0].name

# Use expicit mapping argument instead of 'as' statements in SQL query
legacy_mapping = {'product_name':'name','product_description':'description'}

# Create raw() query with translations argument to map table results
all_legacy_items_with_mapping = Item.objects.raw("SELECT * from coffeehouse_products", translations=legacy_mapping)

# Deferred model field loading, get item one with limited fields
item_one = Item.objects.raw("SELECT id,name from items_item where id=1")
# Access model fields not referenced in the raw query, just like QuerySet defer()
item_one[0].calories
item_one[0].price

# Raw SQL query with aggregate function added as extra model field
items_with_inventory = Item.objects.raw("SELECT *, sum(price*stock) as
        assets from items_item");
# Access extra field directly as part of the model
items_with_inventory[0].assets

###### Django raw SQL queries with connection() and low-level DB API methods

from django.db import connection

# Delete record
target_id = 1
with connection.cursor() as cursor:
    cursor.execute("DELETE from items_item where id = %s", [target_id])

# Select one record
salad_item = None
with connection.cursor() as cursor:
    cursor.execute("SELECT * from items_item where name='Red Fruit Salad'")
    salad_item = cursor.fetchone()

# DB API fetchone produces a tuple, where elements are acessible by index
salad_item[0] # id
salad_item[1] # name
salad_itme[2] # description

# Select multiple records
all_drinks = None
with connection.cursor() as cursor:
    cursor.execute("SELECT * from items_drink")
    all_drinks = cursor.fetchall()

DB API fetchall produces a list of tuple
all_drinks[0][0] # first drink id

###### Django custom model manager with custom manager methods

from django.db import models

# Create custom model manager
class ItemMenuManager(models.Manager):
    def salad_items(self):
        return self.filter(menu__name='Salads')

    def sandwich_items(self):
        return self.filter(menu__name='Sandwiches')

# Option 1) Override default model manager
class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=model.CASCADE)
    name = models.CharField(max_length=30)
    ...
    objects = ItemMenuManager()

# Queries on default custom model manager
Item.objects.all()
Item.objects.salad_items()
Item.objects.sandwich_items()

# Option 2) Create new model manager field and leave default model manager as is
menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
name = models.CharField(max_length=30)
...
objects = models.Manager()
menumgr = ItemMenuManager()

# Queries on default and custom model managers
Item.objects.all()
Item.menumgr.salad_items()
Item.menumgr.sandwich_items()
# ERROR Item.objects.salad_items() # 'Manager' object has no attribute 'salad_items'
# ERROR Item.objects.sandwich_items() # 'Manager' object has no attribute 'sandwich_items'
Item.menumgr.all()

###### Django custom model managers with custom get_queryset() method

class SanDiegoManager(models.Manager):
    def get_queryset(self):
        return super(SanDiegoStoreManager, self).get_queryset().filter(city='San Diego')

class Store(models.Model):
    name = models.CharField(max_length=30)
    ...
    objects = models.Manager()
    sandiego = SanDiegoStoreManager()
    losangeles = LosAngelesStoreManager()

# Call default manager all() query, backed by get_queryset() method
Store.objects.all()
# Call sandiego manager all(), backed by get_queryset() method
Store.sandiego.all()
# Call losangeles manager all(), backed by get_queryset() method
Store.losangeles.all()

###### Django custom model manager with custom QuerySet class and methods

class StoreQuerySet(models.QuerySet):
    def sandiego(self):
        return self.filter(city='San Diego')

    def losangeles(self):
        return self.filter(city='Los Angeles')


class StoreManager(models.Manager):
    def get_queryset(self):
        return StoreQuerySet(self.model, using=self._db)

    def sandiego(self):
        return self.get_queryset().sandiego()

    def losangeles(self):
        return self.get_queryset().losangeles()


class Store(models.Model):
    name = models.CharField(max_length=30)
    ...
    objects = models.Manager()
    shops = StoreManager()

Store.shops.all()
Store.shops.sandiego()
Store.shops.losangeles()

### Django custom model manager with custom QuerySet converted to manager

class StoreQuerySet(models.QuerySet):
    def sandiego(self):
        return self.filter(city='San Diego')

    def losangeles(self):
        return self.filter(city='Los Angeles')


class Store(models.Model):
    name = models.Manager()
    shops = StoreQuerySet.as_manager()

Store.shops.all()
Store.shops.sandiego()
Store.shops.losangeles()

###### Django custom model manager for reverse query operations

from django.db import models

class Item(models.Model):
    ...
    objects = models.Manager() # Default manager for direct queries
    reverseitems = CustomReverseManagerForItems() # Custom Manager for reverse queries

# Get Menu record named Breakfast
breakfast_menu = Menu.objects.get(name='Breakfast')

# Fetch all Item records in the Menu, using Item custom model manager for revrse queries
breakfast_menu.item_set(manager='reverseitems').all()
# Call on_sale_items() custom manager method in CustomReverseManagerForItems
breakfast_menu.item_set(manager='reverseitems').on_sale_items()

###### Django model class and model form

from django import forms

class Contact(models.Model):
    name = models.CharField(max_length=50,blank=True)
    email = models.EmailField()
    comment = models.CharField(max_length=1000)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

###### Django model form processing
# views.py method to process model form

def contact(request):
    if request.method == 'POST':
        # POST, generate bound form with data from the request
        form = ContactForm(request.POST)
        # check if it's valid:
        if form.id_valid():
            # Insert into DB
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/about/contact/thankyou')
    else:
        # GET, generate unbound (blank) form
        form = ContactForm()
    return render(request,'about/contact.html',{'form':form})

###### Django model form with new and custom field

from django import forms

def faq_suggestions(value):
    # Validate value and raise forms.ValidationError for invalid values
    pass


class Contact(models.Model):
    name = models.CharField(max_length=50,blank=True)
    email = models.EmailField()
    comment = models.CharField()


class ContactForm(forms.ModelForm):
    age = forms.IntegerField()
    comment = forms.CharField(widget=forms.Textarea,validators=[faq_suggestions])
    class Meta:
        model = Contact
        fields = '__all__'

###### Django model form with meta options to override default form field behavior

from django import forms

class Contact(models.Model):
    name = models.CharField(max_length=50,blank=True)
    email = models.EmailField()
    comment = models.CharField()


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
                'name': models.CharField(max_length=25),
                'comment': form.Textarea(attrs={'cols': 100, 'rows': 40})
        }
        labels = {
                'name': 'Full name',
                'comment': 'Issue'
        }
        help_texts = {
                'comment': 'Provide a detailed account of the issue to receive a quick answer'
        }
        error_messages = {
                'name': { 'max_length': "Name can only be 25 characters in length"
                }
        }
        field_classes = {
                'email': EmailCoffeehouseFormField
        },
        localized_field = '__all__'

###### Django model form and standard form with custom query for ModelChoiceField and ModelMultipleChoiceField form fields

from django import forms
from coffeehouse.stores.models import Amenity

class Menu(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return "%s" % (self.name)


class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)


class ItemForm(forms.ModelForm):
    menu = forms.ModelChoiceField(queryset=Menu.objects.filter(id=1))
    class Meta:
        model = Item
        fields = '__all__'


class StoreForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()
    amenities = forms.ModelMultipleChoiceField(queryset=None)
    def __init__(self, *args, **kwargs):
        super(StoreForm, self).__init__(*args, **kwargs)
        self.fields['amenities'].queryset = Amenity.objects.filter(name__contains='W')

###### Django custom form field to customize <option> text for ModeChoiceField and ModelMultipleChoiceField form fields

from django import forms
from django.forms import ModelChoiceField

class MenuModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "Menu #%s) %s" % (obj.id,obj.name)

class ItemForm(forms.ModelForm):
    menu = MenuModelChoiceField(queryset=Menu.objects.all())
    class Meta:
        model = Item
        fields = '__all__'

# HTML menu form field output
<select name="menu" id="id_menu" required>
  <option value="" slected>-----------</option>
  <option value="1">Menu #1) Breakfast</option>
  <option value="2">Menu #2) Salads</options>
  <option value="3">Menu #3) Sandwiches</option>
  <option value="4">Menu #4) Drinks</option>
</select>

###### Django model form initialization with initial and instance

from coffeehouse.items.models import Item

preloaded_item = Item.objects.get(id=1)

form = ItemForm(instance=preloaded_item)

# Unbound form set up with instance values
form.as_p()
  <p>
    <label for="id_menu">Menu:</label>
      <select name="menu" required id="id_menu">
        <option value="">----------</option>
        <option value="1" selected>Menu #1) Breakfast</option>
        <option value="2">Menu #2) Salsds</option>
        <option value="3">Menu #3) Sandwiches</option>
        <option value="4">Menu #4) Drinks</option>
    </select>
  </p>

  <p>
    <label for="id_name">Name:</label>
      <input type="text" name="name"
        value="Whole-Grain Oatmeal" required maxlength="30" id="id_name" />
  </p>
  # Remaining fields committed for brevity

# Model form initialize with instance and override with initial
form2 = ItemForm(initial={'menu':3},instance=preloaded_item)

# Unbound form set up with instance values, but overridden with initial form2.as_p()
  <p>
    <label for="id_menu">Menu:</label>
      <select name="menu" required id="id_menu">
        <option value="">-----------</option>
        <option value="1">Menu #1) Breakfast</option>
        <option value="2">Menu #2) Salads</option>
        <option value="3" selected>Menu #3) Sandwiches</option
        <option value="4">Menu #4) Drinks</option>
      </select>
  </p>
  # Remaining fields committed for brevity

###### Django model form with reduced form that requires model update before saving

from django import forms
from django.conf import settings

class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, default=None)
    name = models.CharField(max_length=50,blank=True)
    email = models.EmailField()
    comment = models.CharField()

class ContactForm(form.ModelForm):
    class Meta:
        model = Contact
        exlude = ['user']

# Option 1) Form model processing with missing value assigned with instance
        if form.is_valid():
            # Check if user is available
            if request.user.is_authenticated():
                # Add missing user to model form
                form.instance.user = request.user
            # Insert into DB
            form.save()

# Option 2) Form model processing with missing value assigned after model form sequence
        if form.is_valid():
            # Saveinstance but don't commit until model instance is complete
            # form.save() returns a materialized model instance that has yet to be saved
            pending_contact = form.save(commit=False)
            # Check if user is available
            if request.user.is_authenticated():
                # Add missing user to model form
                pending_contact.user = request.user
            # Insert into DB
            pending_contact.save()

###### Django class-based view with CreateView to create model records
# views.py

from django.views.generic.edit import CreateView
from .models import Item, ItemForm
from django.core.urlresolvers import reverse_lazy

class ItemCreation(CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('items:index')

# models.py
from django import forms
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=30)


class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        field = '__all__'
        widgets = {
                'description': forms.Textarea(),
        }

# urls.py
from django.conf.urls import url
from coffeehouse.items import views as items_views

urlpatterns = [
        url(r'^new/$', items_views.ItemCreation.as_view(), name='new'),
]

# templates/items/item_form.html
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary">Create</button>
  </form>

###### Django class-based view with CreateView with template_name, content_type, and get_context_data()
#views.py

from django.views.generic.edit import CreateView
from .models import Item, ItemForm, Menu

class ItemCreation(CreateView):
    template_name = "items/item_form.html"
    context_type = "text/html"
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('items:index')
    def get_context_data(self,**kwargs):
        kwargs['special_context_variable'] = 'My special context variable!!!'
        context = super(ItemCreation, self).get_context_data(**kwargs)
        return context

###### Django class-based view with CreateView with initial and get_initial()
# views.py

from django.views.generic.edit import CreateView
from .models import Item, ItemForm, Menu

class ItemCreation(CreateView):
    initial = {'size':'L'}
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('items:index')
    def get_initial(self):
        initial_base = super(ItemCreation, self).get_initial()
        initial_base['menu'] = Menu.objects.get(id=1)
        return initial_base

###### Django class-based view with CreateView with get_form()
# view.py
from django.views.generic.edit import CreateView
from .models import Item, ItemForm, Menu

class ItemCreation(CreateView):
    initial = {'size':'L'}
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('items:index')
    
    def get_form(self):
        form = surer(ItemCreation, self).get_form()
        initial_base = self.get_initial()
        initial_base['menu'] = Menu.objects.get(id=1)
        form.initial = initial_base
        form.fields['name'].widget = forms.wiegets.Textarea()
        return form

####### Django class-based view with CreateView with form_valid() and form_invalid()
# views.py

from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Item, ItemForm, Menu

class ItemCreation(CreateView):
    initial = {'size':'L'}
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('items:index')
    
    def form_valid(self,form):
        super(ItemCreation,self).form_valid(form)
        # Add action to valid form phase
        messages.success(self.request, 'Item created successfully!')
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self,form):
        # Add action to invalid form phase
        return self.render_to_response(self.get_context_data(form=form))

###### Django class-based view with CreateView with get() and post()
# views.py

from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.contrib import messages

class ItemCreation(CreateView):
    initial = {'size':'L'}
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('items:index')
    template_name = "items/item_form.html"

    def get(self,request, *args,**kwargs):
        form = super(ItemCreation, self).get_form()
        # Set initial values and custom widget
        initial_base = self.get_initial()
        initial_base['menu'] = Menu.objects.get(id=1)
        form.initial = initial_base
        form.fields['name'].widget = forms.widgets.Textarea()
        # return response using standard render() method
        return render(request,self.template_name,
                {'form':form,
                 'special_context_variable':'My special context variable!'})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        # Verify form is valid
        if form.is_valid():
            # Call parent form_valid to create model record object
            super(ItemCreation,self).form_valid(form)
            # Add custom success message
            messages.success(request, 'Item created successfully!')
            # Redirect to success page
            return HttpResponseRedirect(self.get_success_url())
        # Form is invalid
        # Set object to None, since class-based view expects model record object
        self.object = None
        # Return class-based view form_invalid to generate form with errors
        return self.form_invalid(form)

###### Django class-based view with ListView to read list of records
# views.py

from django.views.generic.list import ListView
from .models import Item

class ItemList(ListView):
    model = Item

# urls.py
from django.conf.urls import url
from coffeehouse.items import views as items_views

urlpatterns = [
        url(r'^$',items_views.ItemList.as_view(),name="index"),
]

# templates/items/item_list.html
  {% regroup object_list by menu as item_menu_list %}
  {% for menu_selection in item_menu_list %}
    <li>{{ menu_section.grouper }}
      <ul>
        {% for item in menu_section.list %}
        <li>{{item.name|title}}</li>
        {% endfor %}
      </ul>
      </li>
  {% endfor %}

###### Django class-based view with DetailView to read model record
# views.py

from django.views.generic import DetailView
from .models import Item

class ItemDetail(DetailView):
    model = Item

# urls.py
from django.conf.urls import url
from coffeehouse.items import views as items_views

urlpatterns = [
        url(r'^(?P<pk>\d+)/$',items_views.ItemDetail.as_view(),name="detail"),
]

# templates/items/item_detail.html
<h4> {{item.name|title}}</h4>
<p>{{item.description}}</p>
<p>${{item.price}}</p>
<p>For {{item.get_size_display}} size: Only {{item.calories}} calories
{% if item.drink %}
and {{item.drink.caffeine}} mg of caffeine.</p>
{% endif %}
</p>

###### Django class-based view with ListView to reduce record list with queryset
# views.py

from django.views.generic.list import ListView
from .models import Item

class ItemList(ListView):
    model = Item
    queryset = Item.objects.filter(menu_id=1)
    ordering = ['name']

###### Django class-based view with ListView to read list of records with pagination
# views.py

from django.views.generic.list import ListView
from .models import Item

class ItemList(ListView):
    model = Item
    paginate_by = 5

# urls.py
from django.conf.urls import url
from coffeehouse.item import views as items_views

urlpatterns = [
        url(r'^$',items_views.ItemList.as_view(),name="index"),
        url(r'^page/(?P<page>\d+)/$',items_views.ItemList.as_view(),name="page"),
]

# templates/items/item_list.html
  {% regroup object_list by menu as item_menu_list %}
{% for menu_section in item_menu_list %}
  <li>{{ menu_section.grouper }}
    <ul>
      {% for item in menu_section.list %}
      <li>{{item.name|title}}</li>
      {% endfor %}
    </ul>
    </li>
{% endfor %}

  {% if is_paginated %}
    {{page_obj}}
  {% endif %}

###### Django class-based view with DetailView and slug_field option
# views.py

from django.views.genric import DetailView
from .models import Item

class ItemDetail(DetailView):
    model = Item
    slug_field = 'name__iexact'

# urls.py
from django.conf.urls import url
from coffeehouse.items import views as items_views

urlpatterns = [
        url(r'^(?P<slug>\w+)/$',items_views.ItemDetail.as_view(),name="detail"),
]

###### Django class-based view with UpdateView to edit a record
# views.py

from django.views.generic import UpdateView
from .models import Item

class ItemUpdate(UpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('items:index')

# urls.py
from django.conf.urls import url
from coffeehouse.items import views as items_views

urlpatterns = [
        url(r'^edit/(?P<pk>\d+)/$', items_views.ItemUpdate.as_view(), name='edit'),
]

# templates/items/item_form.html
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit" class="btn btn-primary">
    {% if object == None %}Create{% else %}Update{% endif %}
  </button>
</form>

###### Django class-based view with DeleteView to delete record
# views.py

from django.views.generic.edit import DeleteView
from .models import Item

class ItemDelete(UpdateView):
    model = Item
    success_url = reverse_lazy('items:index')

# urls.py
from django.conf.urls import url
from coffeehouse.items import views as items_views

urlpatterns = [
        url(r'^delete/(?P<pk>\d+)/$', items_views.ItemDelete.as_view(), name='delete'),
]

# templates/items/item_confirm_delete.html
  <form method="post">
    {% csrf_token %}
    Do you really want to delete "{{ object }}"?
    <button class="btn btn-primary" type="submit">Yes, remove it!</button>
  </form>

###### Django class-based view with CreateView and mixin class
# views.py

from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Item, ItemForm

class ItemCreation(SuccessMessageMixin,CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('items:index')
    success_message = "Item %(name)s created successfully"

###### Customize a Django model's permissions with default_permissions and permissions

class Store(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30,unique=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    class Meta:
        default_permissions = ('add',)
        permissions = (('give_refund','Can refund customers'),('can_hire', 'Can hire employees'))

######
