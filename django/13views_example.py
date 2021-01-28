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
# streaming large csv file
import csv

from django.http import StreamingHttpResponse

class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value

def some_streaming_csv_view(request):
    """A view that streams a large csv file."""
    # Generate a sequence of rows. The range is based on the maximum number of
    # rows that can be handled by a single sheet in most spreadsheet
    # application.
    rows = (["Row {}".format(idx), str(idx)] for idx in range(65536))
    pseude_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse((writer.writerow(row) for row in rows),
                                     content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    return response

############
# using the template system
from django.http import HttpResponse
from django.template import loader

def some_view(request):
    # Create the HttpResponse object with the appropriate csv header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    # The data is hard-coded here, but you could load it from a database or
    # some other source.
    csv_data = (
            ('First row', 'Foo', 'Bar', 'Bar'),
            ('Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"),
    )
    t = loader.get_template('my_template_name.txt')
    c = {'data': csv_data}
    response.write(t.render(c))
    return response

### then, create the template my_template_name.txt
{% for row in data %}"{{ row.0|addslashes }}", "{{ row.1|addslashes }}", "{{
row.2|addslashes }}", "{{row.3|addslashes }}", "{{ row.4|addslashes }}"
{% endfor %}

###############


