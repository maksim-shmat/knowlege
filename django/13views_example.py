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
# controlling the order of migrations
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
            ('myapp', '0123_the_previous_migtation'),
    ]

###
class Migration(migrations.Migration):
    ...
    run_before = [
            ('third_party_app', '0001_do_awesome'),
    ]

##############
# migrating data between third-party apps
from django.apps import apps as global_apps
from django.db import migrations

def forwards(apps, schema_editor):
    try:
        OldModel = apps.get_model('old_app', 'OldModel')
    except LookupError:
        # The old app isn't installed.
        return

    NewModel = apps.get_model('new_app', 'NewModel')
    NewModel.objects.bulk_create(
            NewModel(new_attribute=old_object.old_attribute)
            for old_object in OldModel.objects.all()
    )

class Migration(migrations.Migration):
    operations = [
            migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
    dependencies = [
            ('myapp', '0123_the_previous_migration'),
            ('new_app', '0001_initial'),
    ]

    if global_apps.is_installed('old_app'):
        dependencies.append(('old_app', '0001_initial'))

###########
# changing a ManyToManyField to use a through model
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
            ('core', '0001_initial'),
    ]
    operations = [
            migrations.SeparatDatabaseAndState(
                database_operations=[
                    # Old table name from checking with sqlmigrate, new table
                    # name from AuthotBook._meta.db_table.
                    migtations.RunSQL(
                        sql='ALTER TABLE core_book_authors RENAME TO
                        core_authorbook',
                        reverse_sql='ALTER TABLE core_authorbook RENAME TO
                        core_book_authors',
                    ),
                ),
                ],
                state_operations=[
                    migrations.CreateModel(
                        name='AuthorBook',
                        fields=[
                            (
                                'id',
                                models.AutoField(
                                    auto_created=True,
                                    primary_key=True,
                                    serialize=False,
                                    verbose_name='ID',
                                ),
                            ),
                            (
                                'author',
                                model.ForeignKey(
                                    on_delete=django.db.models.deletion.DO_NOTHING,
                                    to='core.Author',
                                ),
                            ),
                            (
                                'book',
                                models.ForeignKey(
                                    on_delete=django.db.models.deletion.DO_NOTHING,
                                    to='core.Book',
                                ),
                            ),
                        ],
                    ),
                    migrations.AddField(
                        model_name='authorbook',
                        name='is_primary',
                        field=models.BooleanField(default=False),
                    ),
                ]

################
# tipycal view and urls.py
from django.http import HttpResponse
from django.views import View

class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

### urls.py
from django.urls import path
from myapp.views import MyView

urlpatterns = [
        path('mine/', MyView.as_view(), name='my-view'),
]
############
# template view
from django.views.generic.base import TemplateView
from articles.models import Article

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context

### urls.py
from django.urls import path
from myapp.views import HomePageView

urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
]

#############
# redirect view
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from articles.models import Article

class ArticleCounteRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'article-detail'

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        article.update_counter()
        return super().get_redirect_url(*args, **kwargs)

### urls.py
from django.urls import path
from django.views.generic.base import RedirectView
from article.views import ArticleCounterRedirectView, ArticleDetail

urlpatterns = [
        path('counter/<int:pk>/', ArticleCounterRedirectView.as_view(),
            name='article-counter'),
        path('details/<int:pk>/', ArticleDetail.as_view(), name_'article-detail'),
RedirectView.as_view(url='https://djangoproject.com'), name='go-to-django'),
]

###############
# detail view
from django.utils import timezone
from django.views.generic.detail import DetailView
from articles.models import Article

class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

### urls.py
from django.urls import path
from article.views import ArticleDetailView

urlpatterns = [
        path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
]

### example myapp/article_detail.html
<h1>{{ object.headline }}</h1>
<p>{{ object.content }}</p>
<p>Reporter: {{ object.reporter }}</p>
<p>Published: {{ object.pub_date|date }}</p>
<p>Date: {{ now|date }}</p>

###############
# list view
from django.utils import timezone
from django.views.generic.list import ListView
from articles.models import Article

class ArticleListView(ListView):
    model = Article
    paginate_by = 100 # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

### myapp/urls.py
from django.urls import path
from aricle.views import ArticleListView

urlpatterns = [
        path('', ArticleListView.as_view(), name='article-list'),
]

### myapp/article_list.html
<h1>Articles</h1>
<ul>
{% for article in object_list %}
    <li>{{ article.pub_date|date }} = {{ article.headline }}</li>
{% empty %}
    <li>No articles yet.</li>
{% endfor %}
</ul>

##############
# model for next examples
from django.db import models
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})

### form view
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

### myapp/views.py
from myapp.forms import ContactForm
from django.views.generic.edit import FormatView

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

### myapp/contact.html
<form method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Send message">
</form>

###############
# create view
from django.views.generic.edit import CreateView
from myapp.models import Author

class AuthorCreate(CreateView):
    model = Author
    fields = ['name']

### myapp/author_form.html
<form method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save">
</form>

##############
# update view
from django.views.generic.edit import UpdateView
from myapp.models import Author

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']
    template_name_suffix = '_update_form'

### myapp/author_update_form.html
<form method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Update">
</form>

##############
# delete view
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from myapp.models import Author

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')

### myapp/author_confirm_delete.html
<form method="post">{% csrf_token %}
    <p>Are you sure you want to delete "{{ object }}"?</p>
    <input type="submit" value="Confirm">
</form>

############
# model for next examples
from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})

### ArchiveIndexView
# myapp/urls.py
from django.urls import path
from django.views.generic.dates import ArchiveIndexView
from myapp.models import Article

urlpatterns = [
        path('archive/',
            ArchiveIndexView.as_view(model=Article, date_field="pub_date"),
            name="article_archive"),
]

### myapp/article_archive.html
<ul>
    {% for article in latest %}
        <li>{{ article.pub_date }}: {{ article.title }}</li>
    {% endfor %}
</ul>

############## YearArchiveView
# myapp/view.py
from django.viws.generic.dates import YearArchiveView
from myapp.models import Article

class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True

### myapp/urls.py
from django.urls import path
from myapp.views import ArticleYearArchiveView

urlpatterns = [
        path('<int:year>/',
            ArticleYearArchiveView.as_view(),
            name="article_year_archive"),
]

### myapp/article_archive_year.html
<ul>
    {% for date in date_list %}
        <li>{{ date|date }}</li>
    {% endfor %}
</ul>

<div>
    <h1>All Articles for {{ year|date:"Y" }}</h1>
    {% for obj in object_list %}
        <p>
            {{ obj.title }} - {{ obj.pub_date|date:"F j, Y" }}
        </p>
    {% endfor %}
</div>

############## MonthArchiveView
# myapp/views.py
from django.views.generic.dates import MonthArchiveView
from myapp.models import Article

class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    allow_future = True

### myapp/urls.py
from django.urls import path
from myapp.views import ArticleMonthArchiveView

urlpatterns = [
        # Example: /2012/08/
        path('<int:year>/<int:month>/',
            ArticleMonthArchiveView.as_view(month_format='%m'),
            name="archive_month_numeric"),
        # Example: /2012/aug/
        path('<int:year>/<srt:month>/',
            ArticleMonthArchiveView.as_view(),
            name='archive_month'),
]

### myapp/article_archive_month.html
<ul>
    {% for article in object_list %}
        <li>{{ article.pub_date|date:"F j, Y" }}: {{ article.title }}</li>
    {% endfor %}
</ul>

<p> 
    {% if previous_month %}
        Previous Month: {{ previous_month|date:"F Y" }}
    {% endif %}
    {% if next_month %}
        Next Month: {{ next_month|date:"F Y" }}
    {% endif %}
</p>

###############
# WeekArchiveView
# myapp/views.py
from django.views.generic.dates import WeekArchiveView
from myapp.models import Article

class ArticleWeekArchiveView(WeekArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    week_format = "%W"
    allow_future = True

### myapp/urls.py
from django.urls import path
from myapp.views import ArticleWeekArchiveView

urlpatterns = [
        # Example: /2012/week/23/
        path('<int:year>/week/<int:week>/'
            ArticleWeekArchiveView.as_view(),
            name="archive_week"),
]

### myapp/article_archive_week.html
<h1>Week {{ week|date:'W' }}</h1>
<ul>
    {% for article in object_list %}
        <li>{{ article.pub_date|date:"F j, Y" }}: {{ article.title }}</li>
    {% endfor %}
</ul>

<p>
    {% if previous_week %}
        Previous Week: {{ previous_week|date:"W" }} of year {{
            previous_week|date:"Y" }}
    {% endif %}
    {% if previous_week and next_week %}--{% endif %}
    {% if next_week %}
        Next week: {{ next_week|date:"W" }} of year {{ next_week|date:"Y" }}
    {% endif %}
</p>
############
# DayArchiveView
# myapp/views.py
from django.views.generic.dates import DayArchiveView
from myapp.models import Article

class ArticleDayArchiveView(DayArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    allow_future = True

### myapp/urls.py
from django.urls import path
from myapp.views import ArticleDayArchiveView

urlpatterns = [
        # Example: /2012/nov/10/
        path('<int:year>/<str:month>/<int:day>/',
            ArticleDayArchiveView.as_view(),
            name="archive_day"),
]

### myapp/article_archive_day.html
<h1>{{ day }}</h1>

<ul>
    {% for article in object_list %}
        <li>{{ article.pub_date|date:"F j, Y" }}: {{ article.title }}</li>
    {% endfor %}
</ul>

<p>
    {% if previous_day %}
        Previous Day: {{ previous_day }}
    {% endif %}
    {% if previous_day and next_day %}--{% endif %}
    {% if next_day %}
        Next Day: {{ next_day }}
    {% endif %}
</p>

###############
# TodayArchiveView
# myapp/views.py
from django.views.generic.dates import TodayArchiveView
from myapp.models import Article

class ArticleTodayArchiveView(TodayArchiveView):
    queryset = Article.object.all()
    date_field = "pub_date"
    allow_future = True

### myapp/urls.py
from django.urls import path
from myapp.views import ArticleTodayArchiveView

urlpatterns = [
        path('today/',
            ArticleTodayArchiveView.as_view(),
            name="archive_today"),
]

###################
# DateDetailView
# myapp/urls.py
from django.urls import path
from django.views.generic.dates import DateDetailView

urlpatterns = [
        path('<int:year>/<str:month>/<int:day>/<int:pk>/',
            DateDetailView.as_view(model=Article, date_field="pub_date"),
            name="archive_detail"),
]

### myapp/article_detail.html
<h1>{{ object.title }}</h1>

#############
# ContextMixin
from django.views.generic import TemplateView
TemplateView.as_view(extra_context={'title': 'Custom Title'})

###
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['number'] = random.randrange(1, 100)
    return context

#############
# clickjacking protection
# setting X-Frame-Options for all responses
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("This page is safe to load in a frame on any site.")

### setting X-Frame-Options per view

from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin

@xframe_options_deny
def view_one(request):
    return HttpResponse("I won't display in any frame!")

@xframe_options_sameorigin
def view_two(request):
    return HttpResponse("Display in a frame if it's from the same origin as me.")

############ generic relations
from django.contrib.contenttypes.field import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class TaggedItem(models.Model):
    tag = models.SlugField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.tag

############ associating content with multiple sites
from django.contrib.sites.models import Site
from django.db import models

class Article(models.Model):
    headline = models.CharField(max_length=200)
    # ...
    sites = models.ManyToManyField(Site)

###
from django.contrib.sites.shortcuts import get_current_site

def article_detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id,
                sites__id=get_current_site(request).id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist on this site")
    # ...

### associating content with a single site
from django.contrib.sites.models import Site
from django.db import models

class Article(models.Model):
    headline = models.CharField(max_length=200)
    # ...
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

### hooking into the current site from views
from django.conf import settings

def my_view(request):
    if settings.SITE_ID == 3:
        # Do something.
        pass
    else:
        # Do something else.
        pass

###
from django.contrib.sites.shortcuts import get_current_site

def my_view(request):
    current_site = get_current_site(request)
    if current_site.domain == 'foo.com':
        # Do something
        pass
    else:
        # Do something else.
        pass
### equivalent previous one
from django.contrib.sites.models import Site

def my_function_without_request():
    current_site = Site.objects.get_current()
    if current_site.domain == 'foo.com':
        # Do something
        pass
    else:
        # Do something else.
        pass

############ getting the current domain for display
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail

def register_for_newsletter(request):
    # Check form values, etc., and subscribe the user.
    # ...

    current_site = get_current_site(request)
    send_mail(
            'Thanks for subscribing to %s alerts' % current_site.name,
            'Thanks for your subscription. We appreciate it. \n\n-The %s team.' % ( current_site.name,),
            'editor@%s' % current_site.domain,
            [user.email],
    )
    # ...

###
from django.core.mail import send_mail
from django.template import loader

def register_for_newsletter(request):
    # Check form values, etc., and subscribe the user.
    # ...
    subject = loader.get_template('alerts/subject.txt').render({})
    message = loader.get_template('alerts/message.txt').render({})
    send_mail(subject, message, 'editor@ljworld.com', [user.email])

    # ...

########### the CurrentSiteManager
from django.contrib.sites.models import Site
from django.contrib.sites.manager import CurrentSiteManager
from django.db import models

class Photo(models.Model):
    photo = models.FileField(upload_to='photos')
    photographer_name = models.CharField(max_lenght=100)
    pub_date = models.DateField()
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    objects = models.Manager()
    on_site = CurrentSiteManager()

###
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.db import models

class Photo(models.Model):
    photo = models.FileField(upload_to='photos')
    photographer_name = models.CharField(max_length=100)
    pub_date = models.DateField()
    publish_on = models.ForeignKey(Site, on_delete=models.CASCADE)
    objects = models.Manager()
    on_site = CurrentSiteManager('publish_on')

############# validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
                _('%(value)s is not an even number'),
                params={'value': value},
        )

###
from django.db import models

class MyModel(models.Model):
    even_field = models.IntegerField(validators=[validate_even])

###
from django import forms

class MyForm(forms.Form):
    even_field = forms.IntegerField(validators=[validate_even])

############
