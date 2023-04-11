"""For Django site borrow something realisation."""

#1 models.py

from django.contrib.auth.models import User
from datetime import date


class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE,
                             null=True,
                             verbose_name='Name of the book')
    inv_nom = models.CharField(max_length=20, null=True,
            help_text="Enter inventar nomber of exemplar",
            verbose_name="Inventar nomber")

    imprint = model.CharField(max_length=200,
            help_text="Enter imprint an year of printed",
            verbose_name="Imprint")

    status = models.ForeignKey('Status', on_delete=models.CASCADE,
            null=True,
            help_text='Change status of exemplar',
            verbose_name="Status of book exemplar")

    due_back = models.DateField(null=True, blank=True,
            help_text="Enter end of status",
            verbose_name="Data of end status")

    borrower = models.ForeignKey(User, on_delete=models.SET_NULL,
            null=True, blank=True,
            verbose_name="Borrower",
            help_text='Check borrower of book')

@property
def is_overdue(self):
    if self.due_back and date_today() > self.due_back:
        return True
    return False

# next: python manage.py makemigration
#       python manage.py migrate

#2 catalog/admin.py

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
            (None, {
                'fields': ('book', 'imprint', 'inf_nom')
            }),
            ('Availability', {
                'filed': ('status', 'due_back', 'borrower')
            }),
    )

#3 catalog/views.py

from django.contrib.auth.mixins import LoginRequiredMixin


class LoanedBooksUserListView(LoginRequiredMixin, generic.ListView):
    """
    Universal class for view list of books,
    how be cureent user.
    """
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter
               borrowed=self.request.user).
               filter(status__exact='2').order_by('due_back')

#4 /catalog/urls.py

urlpatterns += [
        url(r'^mybooks/$', views.LoaneBooksByUserListView.as_view(), name='my-borrowed'),
]

#5 /catalog/templates/catalog/bookinstance_list_borrowed_user.html

{% extends "base_generic.html" %}

{% block content %}
  <h1>Borrowed books</h1>

  {% if bookinstance_list %}
  <ul>

    {% for bookinst in bookinstance_list %}
    <li class="{% if bookinst.is_overdue %}
                text-danger{% endif %}">
      <a href="{% url 'book-detail' bookinst.book.pk %}">
                {{bookinst.book.title}}</a>
                ({{ bookinst.due_back }})
    </li>
    {% endfor %}
  </ul>

  {% else %}
    <p>No many books in your Borrowed list.</p>
  {% endif %}
{% endblock %}

#5
