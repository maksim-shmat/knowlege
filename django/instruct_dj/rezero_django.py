"""Django for ReZero."""

python -m pip install Django

django-admin startproject sample_project

cd sample_project

./manage.py startapp receipts

### in sample_project/settings.py
add '127.0.0.1' to ALLOWED_HOSTS
add 'receipts' to INSTALLED_APPS

### in sample_project/urls.py
path('receipts/', include('receipts.urls'))

### receipts/models.py
from decimal import Decimal
from django.db import models

class Receipt(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Receipt(id={self.id})"

    def total(self) -> Decimal:
        return sum(item.cost for itemin
                self.item_set.all())

        class Item(models.Model):
            created = models.DateTimeField(auto_now_add=True)

            description = models.TextField()
            cost = models.DecimalField(max_digits=7,
                    decimal_places=2)
            receipt = models.ForeignKey(Receipt,
                    on_delete=models.CASCADE)

            def __str__(self):
                return f"Item(id={self.id}, description=
                {self.description}, "\
                        f"cost={self.cost})"

### receipts/views.py
from django.http import JsonResponse
from receipts.models import Receipt

def receipt_json(request):
    results = {
            "receipts": [],
    }

    for receipt in Receipt.objects.all():
        line = [str(receipt), []]
        for item in receipt.item_set.all():
            line[1].append(str(item))

        results["receipts"].append(line)

    return JsonResponse(results)

### receipts/admin.py
from django.contrib import admin
from receipts.models import Receipt, Item

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass

### receipts/urls.py
from django.urls import path
from receipts import views

urlpatterns = [
        path("receipt_json/", views.receipt_json),
]

### run ./manage.py makemigrations receipts
$ curl -sS http://127.0.0.1:8000/receipts/receipt_json/ | python3.8 -m json.tool

### receipts/testing.py
from decimal import Decimal
from django.test import TestCase
from receipts.models import Receipt

class ReceiptTest(TestCase):
    fixtures = ["receipts.json", ]

    def test_receipt(self):
        receipt = Reseipt.objects.get(id=1)
        total = receipt.total()

        expected = Decimal("37.55")
        self.assertEqual(expected, total)

# $ ./manage.py test
### boot_django.py
# This file sets up and configures Django. It's used by scripts that
# need to execute as if running in a Django server.

import os
import django
from django.cont import settings

BASE_DIR =
os.path.abspath(os.path.join(os.path.dirname(__file__), "receipts"))

def boot_django():
    settings.configure(
            BASE_DIR=BASE_DIR,
            DEBUG=True,
            DATABASES={
                "default": {

"ENGINE": "django.db.backends.sqlite3",
"NAME": os.path.join(BASE_DIR, "db.sqlite3"),
}
                },
            INSTALLED_APPS=(
                "receipts",
            ),
            TIME_ZONE="UTC",
            USE_TZ=True,
        )
    django.setup()

### running management commands with your installable django app
# !/usr/bin/env python
# makemigrations.py
from django.core.management import call_command
from boot_django import boot_django

boot_django()
call_command("makemigrations", "receipts")

### testing your installable django app
#!/usr/bin/env python
# load_tests.py
import sys
from unittest import TestSuite
from boot_django import boot_django

boot_django()

default_labels = ["receipts.tests", ]

def get_suite(labels=default_labels):
    from django.test.runner import DiscoverRunner
    runner = DiscoverRunner(verbosity=1)
    failures = runner.run_tests(labels)
    if failures:
        sys.exit(failures)

    # In case this is called from setuptools, return a test suite
    return TestSuite()

if __name__ == "__main__":
    labels = default_labels
    if len(sys.argv[1:]) > 0:
        labels = sys.argv[1:]

    get_suite(labels)

###### 
