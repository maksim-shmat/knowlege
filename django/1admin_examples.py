""" Examples for admin."""

# Exposing multiple databases in Django's admin interface.

class MultiDBModelAdmin(admin.ModelAdmin):
    # A handly constant for the name of the alternate database.
    using = 'other'

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widget using a query
        # on the 'other' database.
        return super().formfield_for_foreignkey(db_field, request,
                using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super().formfield_for_manytomany(db_field, request,
                using=self.using, **kwargs)

############
# InlineModelAdmin objects can be handled in a similar fashion. They require
# three customized methods:
class MultiDMTabularInline(admin.TabularInline):
    using = 'other'

    def get_queryset(self, request):
        # Tell Django to look for inline objects on the 'other' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super().formfield_for_foreignkey(db_field, request,
                using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super().formfield_for_manytomany(db_field, request,
                using=self.using, **kwargs)

#############
# Once you've written your model admin definitions, they can be registered
# with any Admin instance:
from django.contrib import admin

# Specialize the multi-db admin objects for use with specific models.
class BookInline(MultiDBTabularInline):
    model = Book

class PublisherAdmin(MultiDBModelAdmin):
    inlines = [BookInline]

admin.site.register(Author, MultiDBModelAdmin)
admin.site.register(Publisher, PublisherAdmin)

othersite = admin.AdminSite('othersite')
othersite.register(Publisher, MultiDBModelAdmin)

###########
# ModelAdmin object
from django.contrib import admin
from myproject.myapp.models import Author

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author, AuthorAdmin)

### but if you are happy with the default admin interface
from django.contrib import admin
from myproject.myapp.models import Author

admin.site.register(Author)

### the register decorator
from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

###
from django.contrib import admin
from .models import Author, Editor, Reader
from myproject.admin_site import custom_admin_site

@admin.register(Author, Reader, Editor, site=custom_admim_site)
class PersonAdmin(admin.ModelAdmin):
    pass

######### model admin options
from django.contrib import admin

class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'

### ModelAdmin.empty_value_display
from django.contrib import admin

class AuthorAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'

###
from django.contrib import admin

class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'title', 'view_birth_date')

    def view_birth_date(self, obj):
        return obj.birth_date

    view_birth_date.empty_value_display = '???'

########## ModelAdmin.exclude
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3)
    birth_date = models.DateField(blank=True, null=True)

###
from django.contrib import admin

class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'title')

class AuthorAdmin(admin.ModelAdmin):
    exclude = ('birth_date',)

############ ModelAdmin.fields
class FlatPageAdmin(admin.ModelAdmin):
    fields = ('url', 'title', 'content')

########### ModelAdmin.fieldsets
from django.contrib import admin

class FlatPageAdmin(admin.ModelAdmin):
    fieldsets = (
            (None, {
                'fields': ('url', 'title', 'content', 'sites')
            }),
            ('Advanced options', {
                'classes': ('collapse',),
                'fields': ('registration_required', 'template_name'),
            }),
    )

############# ModelAdmin.formfield_overrides
from django.contrib import admin
from django.db import models

# Import out custom widget and out model from where they're defined
from myapp.models import MyModel
from myapp.widgets import RichTextEditorWidget

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': RichTextEditorWidget},
    }

############ ModelAdmin.list_display
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

###
def upper_case_name(obj):
    return ("%s %s" % (obj.first_name, obj.last_name)).upper()
upper_case_name.short_description = 'Name'

class PersonAdmin(admin.ModelAdmin):
    list_display = (upper_case_name,)

###
class PersonAdmin(admin.ModelAdmin):
    list_display = ('upper_case_name',)

    def upper_case_name(self, obj):
        return ("%s %s" % (obj.first_name, obj.last_name)).upper()
    upper_case_name.short_description = 'Name'

###
from django.contrib import admin
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()

    def decade_born_in(self):
        return '%d`s' % (self.birthday.year // 10 * 10)
    decade_born_in.short_description = 'Birth decade'

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'decade_born_in')

###
from django.contrib import admin
from django.db import models
from django.utils.html import format_html

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    color_code = models.CharField(max_length=6)

    def colored_name(self):
        return format_html(
                '<span style="color: %{}:">{} {}</span>',
                self.color_code,
                self.first_name,
                self.last_name,
        )

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'colored_name')

###
from django.contrib import admin

admin.site.empty_value_display = '(None)'

###
class PersonAdmin(admin.ModelAdmin):
    empty_value_display = 'unknown'

###
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date_view')

    def birth_date_view(self, obj):
        return obj.birth_date

    birth_date_view.empty_value_display = 'unknown'

###
from django.contrib import admin
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_lenght=50)
    birthday = models.DateField()

    def born_in_fifties(self):
        return 1950 <= self.birthday.year < 1960
    born_in_fifties.boolean = True

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'born_in_fifties')

###
from django.contrib import admin
from django.db import models
from django.utils.html import format_html

class Person(models.Model):
    first_name = models.CharField(max_lenght=50)
    color_code = models.CharField(max_lenght=6)

    def colored_first_name(self):
        return format_html(
                '<span style="color: #{};">{}</span>',
                self.color_code,
                self.first_name,
        )

    colored_first_name.admin_order_field = 'first_name'

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'colored_first_name')

###
class Blog(model.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'author_first_name')

    def author_first_name(self, obj):
        return obj.author.first_name

    author_first_name.admin_order_field = 'author__first_name'

###
from django.db.models import Value
from django.db.models.functions import Concat

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def full_name(self):
        return self.first_name + ' ' + self.last_name
    full_name.admin_order_field = Concat('first_name', Value(' '),
            'last_name')

###
class Person(model.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def my_property(self):
        return self.first_name + ' ' + self.last_name
    my_property.short_description = "Full name of the person"
    my_property.admin_order_field = 'last_name'

    full_name = property(my_property)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

############# ModelAdmin.list_display_links
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthday')
    list_display_links = ('first_name', 'last_name')

###
class AuditEntryAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'message')
    list_display_links = None

############# ModelAdmin.list_filter
class PersonAdmin(admin.ModelAdmin):
    list_filter = ('is_staff', 'company')

###
class PersonAdmin(admin.UserAdmin):
    list_filter = ('company__name',)

###
from datetime import date
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class DecadeBornListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('decade born')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'decade'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
                ('80s', _('in the eighties')),
                ('90s', _('in the nineties')),
        )

    def queryset(self, request, queryset):
        """
        Return the filtered queryset based on the value
        provided in the query string and retrievable via
        'self.value()'.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '80s':
            return queryset.filter(birthday__gte=date(1980, 1, 1),
                                   birthday__lte=date(1989, 12, 31))
        if self.value() == '90s':
            return queryset.filter(birthday__gte=date(1990, 1, 1),
                                   birthday__lte=date(1999, 12, 31))

class PersonAdmin(admin.ModelAdmin):
    list_filter = (DecadeBornListFilter,)

###
class AuthDecadeBornListFilter(DecadeBornListFilter):
    
    def lookups(self, request, model_admin):
        if request.user.is_superuser:
            return super().lookups(request, model_admin)

    def queryset(self, request, queryset):
        if request.user.is_superuser:
            return super().queryset(request, queryset)

###
class AdvancedDecadeBornListFilter(DecadeBornListFilter):
    def lookups(self, request, model_admin):
        """
        Only show the lookups if there actually is
        anyone born in the corresponding decades.
        """
        qs = model_admin.get_queryset(request)
        if qs.filter(birthday__gte=date(1980, 1, 1),
                birthday__lte=date(1980, 12, 31)).exists():
            yield ('80s', _('in the eighties'))
        if qs.filter(birthday__gte=date(1990, 1, 1),
                birthday__lte=date(1999, 12, 31)).exists():
            yield ('90s', _('in the nineties'))

###
class PersonAdmin(admin.ModelAdmin):
    list_filter = (
            ('is_staff', admin.BooleanFieldListFilter),
    )

###
class BookAdmin(admin.ModelAdmin):
    list_filter = (
            ('author', admin.RelatedOnlyFieldFilter),
    )

###
class BookAdmin(admin.ModelAdmin):
    list_filter = (
            ('title', admin.EmptyFieldListFilter),
    )

###
class FilterWithCustomTemplate(admin.SimpleListFilter):
    template = "custom_template.html"

########### ModelAdmin.readonly_fields
from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ('address_report',)

    def address_report(self, instance):
        # assuming get_full_address() returns a list of strings
        # for each line of the address and you want to separate each
        # line by a linebreak
        return format_html_join(
                mark_safe("<br>"),
                '{}',
                ((line,) for line in instance.get_full_address()),
                ) or mark_safe("<span class='errors'>I can't determine this
                address.
                </span>")
        # short_description functions like a model field's verbose_name
        address_report.short_description = "Address"

############# ModelAdmin.save_model
from django.contrib import admin

class ArticleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

### ModelAdmin.save_formset(request, form, formset, change)
class ArticleAdmin(admin.ModelAdmin):
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.user = request.user
            instance.save()
        formset.save_m2m()

###
