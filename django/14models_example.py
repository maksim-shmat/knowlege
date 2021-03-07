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

######