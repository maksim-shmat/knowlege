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
# generating pdf dynamically with ReportLab API
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

def some_view(request):
    # Create a file-like buffer to receive pdf data.
    buffer = io.BytesIO()

    # Create the pdf object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

##########
# writing database migrations
from django.db import migrations

def forwards(apps, schema_editor):
    if schema_editor.connection.alias != 'default':
        return
    # Your migration code goes here

class Migration(migrations.Migration):
    
    dependencies = [
            # Dependencies to other migrations
    ]

    operations = [
            migrations.RunPython(forwards),
    ]

###
class MyRouter:
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if 'target_db' in hints:
            return db == hints['target_db']
        return True

###
from django.db import migrations

def forwards(apps, schema_editor):
    # Your migration code goes here
    ...

class Migration(migrations.Migration):

    dependencies = [
            # Dependencies to other migrations
    ]

    operations = [
            migrations.RunPython(forwards, hints={'target_db': 'default'}),
    ]

### migrations that add unique fields
from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
            ('myapp', '0005_populate_uuid_values'),
    ]

    operations = [
            migrations.AlterField(
                model_name='mymodel',
                name='uuid',
                field=models.UUIDField(default=uuid.uuid4, unique=True),
            ),
    ]

###
class Migration(migrations.Migration):

    dependencies = [
            ('myapp', '0003_auto_20150129_1705'),
    ]
    operations = [
            migrations.AddField(
                model_name='mymodel',
                name='uuid',
                field=models.UUIDField(default=uuid.uuid4, unique=True),
            ),
    ]

###
from django.db import migrations
import uuid

def get_uuid(apps, schema_editor):
    MyModel = apps.get_model('myapp', 'MyModel')
    for row in MyModel.objects.all():
        row.uuid = uuid.uuid4()
        row.save(update_fields=['uuid'])

class Migration(migrations.Migration):
    dependencies = [
            ('myapp', '0004_app_uuid_field'),
    ]
    operations = [
            # omit reverse_code=... if you don't want the migration to be 
            # reversible.
            migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]

### not atomic migrations
from django.db import migrations

class Migration(migrations.Migration):
    atomic = False

###
import uuid
from django.db import migrations, transaction

def gen_uuid(apps, schema_editor):
    MyModel = apps.get_model('myapp', 'MyModel')
    while MyModel.objects.filter(uuid__isnull=True).exists():
        with transaction.atomic():
            for row in MyModel.objects.filter(uuid__isnull=True)[:1000]:
                row.uuid = uuid.uuid4()
                row.save()

class Migration(migrations.Migration):
    atomic = False

    operations = [
            migrations.RunPython(gen_uuid),
    ]

##############

