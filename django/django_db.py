"""Django's db CRUD operations."""


#1 CLI

python manage.py shell

#2 Creating db

>>> from rewiews.models import Publisher

>>> publisher = Publisher(name="Pumpkt Pumpkins",
    website = 'https://www.paupau.com',
    email='info@pipa.com')

>>> publisher.save()

#3 using the create() method

>>> from reviews.models import Contributor

>>> contributor = Contributor.objects.create(firss_names="Rowel",
    last_names="Arizona",
    email="RoriArizona@example.com")

#4 many-to-one relationship

>>> from reviews.models import Book, Publisher

>>> publisher = Publisher.objects.get(name="PauPumpkins")

>>> from datetime import date

>>> book = Book.objects.create(title="Advanced Deep Learning with Keka",
    publication_date=date(2023, 10, 31), isbn="9872342235871",
    publisher=publisher)

#5 many-to-many relationships

>>> from reviews.models import Book
>>> from reviews.models import Contributor

>>> contibutor = Contributor.objects.get(first_name='Rori')
>>> book = Book.objects.get(title="Advanced Deep Learning with Keka")

>>> from reviews.models import BookContributor
>>> book_contributor = BookContributor(book=book,
    contributor=contributor, role='AUTHOR')
>>> book_contributor.save()

#6 many-to-many with the add() method

>>> from reviews.models import Book, Contributor
>>> book = Book.objects.get(title="Advanced Deep Learning with Keka")

>>> contributor = Contributor.objects.create(first_names='Packt',
    last_names='Example Editor',
    email='PapanEditor@example.com')

>>> book.contributors.add(contributor, through_defaults={'role': 'EDITOR'})

#7 many-to-many with create() and set()

>>> book.contributors.create(first_names='Papch',
    last_names='Editor Example',
    email='PapchEditor2@example.com',
    through_defaults={'role': 'EDITOR'})

>>> from reviews.models import Publisher

>>> publisher = Publisher.objects.create(name='Popic Books',
    website='http://popicbookssampleurl.com',
    email='popicbook@example.com')

>>> contributor1 = Contributor.objects.create(first_names='Stesha',
    last_names='Susi', email='SteshaSusi@example.com')

>>> contributor2 = Contributor.objects.create(first_names='Peter',
    last_names='Straub', email='PeterStraub@example.com')

>>> book = Book.ojects.crate(title='The Talismanitra',
    publication_date=date(2023, 9, 25),
    isbn='3892387358923', publisher=publisher)


>>> book.contributors.set([contributor1, contributor2],
    through_defaults={'role': 'CO_AUTHOR'})

#8 using the get() method to retrieve an object

>>> from reviews.models import Publisher
>>> publisher = Publisher.objects.get(name='Popic Books')
>>> publisher.name
...
>>> publiser.website
...
>>> publisher.email
...

#9 Returning an object using the get()

>>> Publisher.objects.get(pk=2)
...
>>> Publisher.objects.get(id=2)
...

#10 Using the all() to retrieve a set of objects

>>> from reviews.models import Contributor

>>> Contributor.objects.all()
...

>>> contributors = Contributor.objects.all()
>>> contributors[0]
...
>>> contributors[0].first_names
...
>>> contributors[0].last_names
...

#11 Retrieving objects by filtering with filter()

>>> from reviews.models import Contributor
>>> Contributor.objects.create(first_names='Peter',
    last_name='Watson',
    email='PeterWatson@example.com')

>>> Contributor.objects.filter(first_names='Peter')
...

>>> Contributor.objects.filter(first_names='Rori')
...

>>> Contributor.objects.filter(first_names='Nobody')
...

#12 Filtering by field lookups

>>> from reviews.models import Book
>>> book = Book.objects.filter(publication_date__gt=date(2023, 1, 1))
# gt - greater than, lt - less than, lte - less than or equal to, gte.
>>> book
...
>>> book[0].publication_date
...

#13 Using pattern matching for filtering operations

>>> book = Book.objects.filter(title__contains='Deep learning')
>>> book
...
>>> book[0].title
...

#14 Retrieving objects by using the exlude()

>>> Contributor.objects.all()
...
>>> Contributor.objects.exclude(first_names='Peter')

#15 order_by()

>>> books = Book.objects.order_by("publication_date")
>>> books
...
>>> books[0].publication_date
...
>>> books[1].publication_date
...


>>> books = Book.objects.order_by("-publication_date")
>>> books
...
>>> books[0].publication_date
...
>>> books[1].publication_date
...


>>> books = Book.objects.order_by('id')  # ('-id')
>>> books[0].id
...

>>> books = Books.objects.order_by('title')  # ('-title')

>>> publishers = Publisher.objects.all().values()
>>> publishers
...
>>> publishers[0]

#16  Querying using foreign keys

>>> Book.objects.filter(publisher__name='Pak Pucpuc')
...

#17 Querying using the model name

>>> Publisher.objects.get(book__title='Advanced Deep Learning with Kek')
...

#18 Querying across foreign key relationships using the object instance

>>> book = Book.objects.get(title='The Talismanium')
>>> book.publisher
...

>>> publisher = Publisher.objects.get(name='Pocket Books')
>>> publisher.book_set.all()
...

>>> Book.objects.filter(publisher__name='Pocket
    Books').filter(title='The Talismanium')
...

#19 querying across a many-to-many relationship using the field lookup

>>> from reviews.models import Contributor
>>> Contributor.objects.filter(book__title='The Talismanium')

#20 many-to-many query using objects

>>> from reviews.models import Book

>>> book = Book.objects.get(title='The Talismanium')
>>> book.contributors.all()
...

#21 many-to-many query using set()

>>> from reviews.models import Contributor
>>> contributor = Contributor.objects.get(first_names='Rowel')
>>> contributor.book_set.all()
...

#22 using the update()

>>> from reviews.models import Contributor
>>> Contributor.objects.filter(last_names='Tyrrell').
    update(first_names='Mike')
>>> Contributor.objects.get(last_names='Tyrrell').
    first_names
...

#23 Using the delete()

>>> from reviews.models import Contributor
>>> Contributor.objects.get(last_names='Watson').delete()
...

>>> Contributor.objects.get(last_names='Watson')
Traceback... error

#24 Bulk create and bulk update operations

Person.objects.bulk_create([
    Person(name='Robert', address='5, Byron bay, NSW'),
    Person(name='Mark', address="Unit 12, New town, NSW 2000"),
])

person[0].address = '8, Byron bay, NSW'
person[1].address = '15, New town, NSW'
Person.objects.bulk_update(persons, ['address'])

#25 Creating multiple records using bulk_create

>>> from reviews.models import Publisher

>>> Publisher.objects.bulk_create([
    Publisher(name="New Town Publisher",
    website="www.newtownexample.com",
    email='newtown@email.com'),
    Publisher(name="Byron Bay Press",
    website='www.byronbayexample.com',
    email='byronbayexample@email.com'),
    Publisher(name='Katahita Publisher',
    website="www.katahitaexample.com",
    email='katahitaexample@email.com')
])
...

#26 updating multiple records using bulk_update

>>> from reviews.models import Publisher

>>> publisher = [Publisher.objects.get(name='New Town Publisher'),
    Publisher.objects.get(name='Byron Bay Press')]
>>> publishers[0].website = 'www.newsouthwalespublisher.com'
>>> publishers[1].website = 'www.newsouthwalespublisher.com'

>>> Publisher.objects.bulk_update(publishers, ["website"])
...

#27 lookups with Q objects

Person.objects.get(Q(name__startswith='Rob'), | Q(name__startswith='Bob'))

#28 performing a complex query using a Q object

>>> from django.db.models import Q
>>> from reviews.models import Publisher

>>> Publisher.objects.filter(Q(name__startswith="New")
        | Q(name__startswith="Idea"))
...

>>> Publisher.objects.filter(Q(name__startswits="New") &
        Q(name__endswith="Publisher"))
...

#29 Verifying whether a queryset contains a given object
