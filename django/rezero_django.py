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

###
