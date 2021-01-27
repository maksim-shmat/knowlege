""" Check subscribe/subcribe. """

class SubscribeForm(form.Form):
    email = forms.EmailField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('subscribe_butn', 'Subscribe'))

from .forms import SubscribeForm, UnSubscribeForm

class NewsletterView(generic.TemplateView):
    subcribe_form_class = SubscribeForm
    unsubcribe_form_class = UnSubscribeForm
    template_name = "newsletter.html"

    def get(self, request, *args, **kwargs):
        kwargs.setdefault("subscribe_form", self.subcribe_form_class())
        kwargs.setdefault("unsubscribe_form", self.unsubcribe_form_class())
        return super().get(request, *args, **kwargs)

def post(self, request, *args, **kwargs):
    form_args = {
            'data': self.request.POST,
            'files': self.request.FILES,
    }
    if "subscribe_butn" in request.POST:
        form = self.subcribe_form_class(**form_args)
        if not form.is_valid():
            return self.get(request,
                            subscribe_form=form)
        elif "unsubscribe_butn" in request.POST:
            form = self.unsubcribe_form_class(**form_args)
            if not form.is_valid():
                return self.get(request,
                                unsubscribe_form=form)
            return redirect("success_form2")
        return super().get(request)

#######
class ImportantDate(models.Model):
    date = models.DateField()
    desc = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('impdate_detail', args=[str(self.pk)])

###
class ImpDateDetail(generic.DetailView):
    model = models.ImportantDate

class ImpDateCreate(generic.CreateView):
    model = models.ImportantDate
    form_class = ImportantDateForm

class ImpDateUpdate(generic.UpdateView):
    model = models.ImportantDate
    form_class = ImportantDateForm

class ImpDateDelete(generic.DeleteView):
    model = models.ImportantDate
    success_url = reverse_lazy("formschapter:impdate_list")

# but he is talking about forms.py
from django import forms
from . import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ImportantDateForm(forms.ModelForm):
    class Meta:
        model = models.ImportantDate
        fields = ["date", "desc"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Save'))

###############
# views for polls site
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

###############
# show the latest 5 poll question
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_liat])
    rerurn HttpResponse(output)

################
# First add template index.html to templates/ and after add this to views.py
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
            'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

##############
# Http404 and after add detail.html
from django.http import Http404
from django.shortcuts import render
from .models import Question
# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

############
# A shortcut: get_object_or_404()
from django.shortcuts import get_object_or_404, render
from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

###########
# make a voted with radiobuttons
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question
# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=
            (question.id,)))
##########
from django.shortcuts import get_object_or_404, render

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

##########
# And now True version 
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the last five published questions (not including
        those set to be published in the future).
        """
        return Question.objects.filter(
                pub_date__lte=timezone.now()
                ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    ... # same as above, no changes needed.

############
# polls/views.py for testing class DetailView
class DetailView(generic.DetailView):
    ...
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

#########
# transactions
from django.db import transaction

@transaction.non_atomic_requests
def my_view(request):
    do_stuff()

@transaction.non_atomic_requests(using='other')
def my_other_view(request):
    do_stuff_on_the_other_database()

###
# Atomicity transactions
from django.db import transaction

@transaction.atomic
def viewfunc(request):
    # This code executes inside a transaction.
    do_stuff()

# And as a context manager
from django.db import transaction

def viewfunc(request):
    # This code executes in autocommit mode (Django's default).
    do_stuff()
    with transaction.atomic():
        # This code executes inside a transaction.
        do_more_stuff()
        
# Wrapping atomic in a try/except block allows for natural handling of 
# integrity errors:
from django.db import IntegrityError, transaction

@transaction.atomic
def viewfunc(request):
    create_parent()
    try:
        with transaction.atomic():
            generate_relationships()
    except IntegrityError:
        handle_exception()
    add_children()

##########
#
# Atomicity transactions
from django.db import transaction

@transaction.atomic
def viewfunc(request):
    # This code executes inside a transaction.
    do_stuff()

# And as a context manager
from django.db import transaction

def viewfunc(request):
    # This code executes in autocommit mode (Django's default).
    do_stuff()
    with transaction.atomic():
        # This code executes inside a transaction.
        do_more_stuff()
        
# Wrapping atomic in a try/except block allows for natural handling of 
# integrity errors:
from django.db import IntegrityError, transaction

@transaction.atomic
def viewfunc(request):
    create_parent()
    try:
        with transaction.atomic():
            generate_relationships()
    except IntegrityError:
        handle_exception()
    add_children()

##########
#
# Atomicity transactions
from django.db import transaction

@transaction.atomic
def viewfunc(request):
    # This code executes inside a transaction.
    do_stuff()

# And as a context manager
from django.db import transaction

def viewfunc(request):
    # This code executes in autocommit mode (Django's default).
    do_stuff()
    with transaction.atomic():
        # This code executes inside a transaction.
        do_more_stuff()
        
# Wrapping atomic in a try/except block allows for natural handling of 
# integrity errors:
from django.db import IntegrityError, transaction

@transaction.atomic
def viewfunc(request):
    create_parent()
    try:
        with transaction.atomic():
            generate_relationships()
    except IntegrityError:
        handle_exception()
    add_children()

###
# You may need to manually revert model state when rolling back a transaction
from django.db import DatabaseError, transaction

obj = MyModel(active=False)
obj.active = True
try:
    with transaction.atomic():
        obj.save()
except DatabaseError:
    obj.active = False

if obj.active:
    ...
##########
# Savepoints
from django.db inport transaction

# open a transaction
@transaction.atomic
def viewfunc(request):
    a.save()
    # transaction now contains a.save()
    sid = transaction.savepoint()
    b.save()
    # transaction now contains a.save() and b.save()
    if want_to_keep_b:
        transaction.savepoint_commit(sid)
        # open transaction still contains a.save() and b.save()
    else:
        transaction.savepoint_rollback(sid)
        # open transaction now contains only a.save()

###########
# Specifying defaults for view arguments
# URL conf
from django.urls import path
from . import views

urlpatterns = [
        path('blog/', views.page),
        path('blog/page<int:num>/', views.page),
]
# View (in blog/views.py)
def page(request, num=1):
    # Output the appropriate page of blog entries, according to num.
    ...

##########
# language prefix in URL patterns
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path

from about import views as about_views
from news import views as news_views
from sitemap.views import sitemap

urlpatterns = [
        path('sitemap.xml', sitemap, name='sitemap-xml'),
]

news_patterns = ([
    path('', news_views.index, name='index'),
    path('category/<slug:slug>/', news_views.category, name='category'),
    path('<slug:slug>/', news_views.details, name='detail'),
], 'news')

urlpatterns += i18n_patterns(
        path('about/', about_views.main, name='about'),
        path('news/', include(news_patterns, namespace='news')),
)

#############
# translating URL patterns
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path
from django.utils.translation import gettext_lazy as _

from about import views as about_views
from news import views as news_views
from sitemaps.views import sitemap

urlpatterns = [
        path('sitemap.xml', sitemap, name='sitemap-xml'),
]

news_patterns = ([
    path('', news_views.index, name='index'),
    path(_('category/<slug:slug>/'), news_views.category, name='category'),
    path('<slug:slug>/', news_views.details, name='detail'),
], 'news')

urlpatterns += i18n_patterns(
        path(_('about/'), about_views.main, name='about'),
        path(_('news/'), include(news_patterns, namespace='news')),
)
##############
# customazing the makemessages command
from django.core.management.commands import makemessages

class Command(makemessages.Command):
    xgettext_options = makemessages.Command.xgettext_options + ['--
    keyword=mytrans']

###
from django.core.management.commands import makemessages

class Command(makemessages.Command):

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
                '--extra-keyword',
                dest='xgettext_keywords',
                action='append',
        )

    def handle(self, *args, **options):
        xgettext_keywords = options.pop('xgettext_keywords')
        if xgettext_keywords:
            self.xgettext_options = (
                    makemessages.Command.xgettext_options[:] +
                    ['--keyword=%s' % kwd for kwd in xgettext_keywords]
            )
        super().handle(*args, **options)

###########
# using translations outside views and templates
from django.utils import translation

def welcome_translated(language):
    cur_language = translation.get_language()
    try:
        translation.activate(language)
        text = translation.gettext('welcome')
    finally:
        translation.activate(cur_language)
    return text

###
from django.utils import translation

def welcome_translated(language):
    with translation.override(language):
        return translation.gettext('welcome')

############
# selecting the current time zone
import pytz

from django.utils import timezone

class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
        return self.get_response(request)

### create a view that can set the current timezone

from django.shortcuts import redirect, render

def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'template.html', {'timezones':
            pytz.common_timezones})

### include a form in template.html that will POST to this view
{% load tz %}
{% get_current_timezone as TIME_ZONE %}
<form action="{% url 'set_timezone' %}" method="POST">
    {% csrf_token %}
    <label for="timezone">Time zone:</label>
    <select name="timezone">
        {% for tz in timezones %}
        <option value="{{ tz }}"{% if tz == TIME_ZONE %} selected{% endif %}>{{ tz }}</option>
        {% endfor %}
    </select>
    <input type="submit" value="Set">
</form>

##############
# using logging
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def my_view(request, arg1, arg):
    ...
    if bad_mojo:
        # Log an error message
        logger.error('Something went wrong!')

###########
# add filter UnreadablePostError
from djngo.http import UnreadablePostError

def skip_unreadable_post(record):
    if record.exc_info:
        exc_type, exc_value = record.exc_info[:2]
        if isinstance(exc_value, UnreadablePostError):
            return False
    return True

#######
# paginating a ListView
from django.view.generic import ListView
from myapp.models import Contact

class ContactList(ListView):
    paginate_by = 2
    model = Contact

###
{% for cantact in page_obj %}
  {{ contact.full_name|upper }}<br>
  ...
{% endfor %}

<div class="pagination">
  <span class="step-links">
    {% if page_obj.has_previous %}
      <a href="?page=1">&laquo; first</a>
      <a href="?page={{ page_obj.previous_page_number }}">previous</a>
    {% endif %}

    <span class="current">
      Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
    </span>

    {% if page_obj.has_next %}
      <a href="?page={{ page_obj.next_page_number }}">next</a>
      <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
    {% endif %}
  </span>
</div>

###########
# using paginator in a view function
from django.core.paginator import Paginator
from django.shortcuts import render

from myapp.models import Contact

def listing(request):
    contact_list = Contact.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list.html', {'page_obj': page_obj})

###########
# serializing data
from django.core import serializers
data = serializers.serialize("xml", SomeModel.objects.all())

###
with open("file.xml", "w") as out:
    xml_serializer.serialize(SomeModel.objects.all(), stream=out)

### subset of fields
from django.core import serializers
data = serializers.serialize('xml', SomeModel.objects.all(), fields=
        ('name', 'size'))

###########
# custom json encoder
from django.core.serializers.json import DjangoJSONEncoder

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, YourCustomType):
            return str(obj)
        return super().default(obj)

###
from django.core.serializers import serialize

serialize('json', SomeModel.objects.all(), cls=LazyEncoder)

############
# deserialization of natural keys
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    birthdate = models.DateField()

    class Meta:
        unique_together = [['first_name', 'last_name']]

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)

###
from django.db import models

class PersonManager(models.Manager):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()

    objects = PersonManager()

    class Meta:
        unique_together = [['first_name', 'last_name']]

###########
# serialization of natural keys
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()

    objects = PersonManager()

    class Meta:
        unique_together = [['first_name', 'last_name']]

    def natural_key(self):
        return (self.first_name, self.last_name)

### natural keys and forward references
objs_with_deferred_fields = []

for obj in serializers.deserialize('xml', data, handle_forward_references=True):
    obj.save()
    if obj.deferred_fields is not None:
        objs_with_deferred_fields.append(obj)

for obj in objs_with_deferred_fields:
    obj.save_deferred_fields()

##############
# dependecies durring serialization

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)

    def natural_key(self):
        return (self.name,) + self.author.natural_key()

###
def natural_key(self):
    return (self.name,) + self.author.natural_key()
natural_key.dependencies = ['example_app.person']

#############
# connecting receiver functions
from django.core.signals import request_finished

request_finished.connect(my_callback)

### use receiver() decorator
from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")

############
# connecting to signals sent by specific senders
from django.db.models.signals import pre_save
from django.dispatch import receiver
from myapp.models import MyModel

@receiver(pre_save, sender=MyModel)
def my_handler(sender, **kwargs):
    ...

############
# preventing duplicate signals
from django.core.signals import request_finished

request_finished.connect(my_callback, dispatch_uid="my_unique_identifier")

############
# custom lookups
from django.db.models import Lookup

class NotEqual(Lookup):
    lookup_name = 'ne'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return '%s <> %s' % (lhs, rhs), params

###
from django.db.models import Field
Field.register_lookup(NotEqual)

###
from django.db.models import Field

@Field.register_lookup
class NotEqualLookup(Lookup):
    # ...

### writing an efficient abs__lt lookup
from django.db.models import Lookup

class AbsoluteValueLessThan(Lookup):
    lookup_name = 'lt'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = compiler.compile(self.lhs.lhs)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params + lhs_params + rhs_params
        return '%s < %s AND %s > -%s' % (lhs, rhs, lhs, rhs), params

AbsoluteValue.register_lookup(AbsoluteValueLessThan)

#############
# custom template backend
from django.template import TemplateDoesNotExist, TemplateSyntaxError
from django.template.backends.base import BaseEngine
from django.template.backends.utils import csrf_input_lazy, csrf_token_lazy

import foobar

class FooBar(BaseEngine):
    # Name of the subdirectory containing the templates for this engine
    # inside an installed application.
    app_dirname = 'foobar'

    def __init__(self, params):
        params = params.copy()
        options = params.pop('OPTIONS').copy()
        super().__init__(params)

        self.engine = foobar.Engine(**options)

    def from_string(self, template_code):
        try:
            return Template(self.engine.from_string(template_code))
        except foobar.TemplateCompilationFailed as exc:
            raise TemplateSyntaxError(exc.args)

    def get_template(self, template_name):
        try:
            return Template(self.engine.get_template(template_name))
        except foobar.TemplateNotFound as exc:
            raise TemplateDoesNotExist(exc.args, backend=self)
        except foobar.TemplateCompilationFailed as exc:
            raise TemplateSyntaxError(exc.args)


class Tamplate:
    
    def __init__(self, template):
        self.template = template

    def render(self, context=None, request=None):
        if context is None:
            context = {}
        if request is not None:
            context['request'] = request
            context['csrf_input'] = csrf_input_lazy(request)
            context['csrf_token'] = csrf_token_lazy(request)
        return self.template.render(context)

###############
# filters and auto-escaping
from django.utils.safestring import SafeString

if isinstance(value, SafeString):
    # Do something with the "safe" string.
    ...

###
@register.filter(is_safe=True)
def myfilter(value):
    return value

###
@register.filter(is_safe=True)
def add_xx(value):
    return '%sxx' % value

###
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(needs_autoescape=True)
def initial_letter_filter(text, autoescape=True):
    first, other = text[0], text[1:]
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = '<strong>%s</strong>%s' % (esc(first), esc(other))
    return mark_safe(result)

###
from django.template.defaultfilters import linebreaksbr, urlize

@register.filter(needs_autoescape=True)
def urlize_and_linebreaks(text, autoescape=True):
    return linebreaksbr(
            urlize(text, autoescape=autoescape),
            autoescape=autoescape
    )
############
# writing the compilation function
<p>The time is {% current_time "%Y-%m-%d %I:%M %p" %}.</p>

###
from django import template

def do_current_time(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
                "%r tag requires a single argument" % token.contents.split()[0]
        )
    if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
        raise template.TemplateSyntaxError(
                "%r tag's argument should be in quotes" % tag_name
        )
    return CurrentTimeNode(format_string[1:-1])

##########


