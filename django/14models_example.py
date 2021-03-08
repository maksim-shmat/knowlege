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

######
