"""Third chapter views examples."""

# writing a custom storage system
from django.core.files.storage import Storage

class MyStorage(Storage):
    ...

###
from django.conf import settings
from django.core.files.storage import Storage

class MyStorage(Storage):
    def __init__(self, option=None):
        if not option:
            option = settings.CUSTOM_STORAGE_OPTIONS
        ...

###########
# outputting csv
import csv
from django.http import HttpResponse

def some_view(request):
    # Create the HttpResponse object with the appropriate csv header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    return response

############

