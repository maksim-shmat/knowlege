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

### ModelAdmin.get_ordering(request)
class PersonAdmin(admin.ModelAdmin):
    def get_ordering(self, request):
        if request.user.is_superuser:
            return ['name', 'rank']
        else:
            return ['name']

### ModelAdmin.get_search_results(request, queryset, search_term)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    search_fields = ('name',)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset,
                search_term)
        try:
            search_term_as_int = int(search_term)
        except ValueError:
            pass
        else:
            queryset |= self.model.objects.filter(age=search_term_as_int)
        return queryset, use_distinct

### ModelAdmin.get_sortable_by(request)
class PersonAdmin(admin.ModelAdmin):
    def get_sortable_by(self, request):
        return {*self.get_list_display(request)} - {'rank'}

### ModelAdmin.get_inline_instances(request, obj=None)
class MyModelAdmin(admin.ModelAdmin):
    inlines = (MyInline,)

    def get_inline_instances(self, request, obj=None):
        return [inline(self.model, self.admin_site) for inline in self.inlines]
    
######### ModelAdmin.get_urls()
from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path

class MyModelAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
                path('my_view/', self.my_view),
        ]
        return my_urls + urls

    def my_view(self, request):
        # ...
        context = dict(
                # Include common variables for rendering the admin template.
                self.admin_site.each_context(request),
                # Anything else you want in the  context...
                key=value,
        )
        return TemplateResponse(request, "sometemplate.html", context)

###
class MyModeAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
                path('my_view/', self.admin_site.admin_view(self.my_view))
        ]
        return my_urls + urls

###
class MyModeAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            kwargs['form'] = MySuperuserForm
        return super().get_form(request, obj, **kwargs)

###
class MuModelAdmin(admin.ModelAdmin):
    inlines = [MyInline, SomeOtherInline]

    def get_formsets_with_inlines(self, request, obj=None):
        form inline in self.get_inline_instances(request, obj):
            # hide MyInline in the add view
            if not isinstance(inline, MyInline) or obj is not None:
                yield inline.get_formset(request, obj), inline

###
class MyModeAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "car":
            kwargs["queryset"] = Car.objects.filter(owner=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

###
class CountryAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['capital'].queryset = self.instance.cities.all()

class CountryAdmin(admin.ModelAdmin):
    form = CountryAdminForm

########### ModelAdmin.formfield_for_manytomany(db_field, requwst, **kwargs)
class MyModelAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "cars":
            kwargs["queryset"] = Car.objects.filter(owner=request.user)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

### ModelAdmin.formfield_form_choice_field(db_field, request, **kwargs)
class MyModelAdmin(admin.ModelAdmin):
    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "status":
            kwargs['choices'] = (
                    ('accepted', 'Accepted'),
                    ('denied', 'Denied'),
            )
            if request.user.is_superuser:
                kwargs['choices'] += (('ready', 'Ready for deployment'),)
        return super().formfield_for_choice_field(db_field, request, **kwargs)

########### Model.Admin.get_changelist_formset(request, **kwargs)
from django.forms import BaseModelFormSet

class MyAdminFormSet(BaseModelFormSet):
    pass

class MyModelAdmin(admin.ModelAdmin):
    def get_changelist_formset(self, request, **kwargs):
        kwargs['formset'] = MyAdminFormSet
        return super().get_changelist_formset(request, **kwargs)

########## InlineModelAdmin objects
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

###
from django.contrib import admin

class BookInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    inlines = [
            BookInline,
    ]

###
class BookInline(admin.TabularInline):
    model = Book
    raw_id_fields = ("pages",)

###
class BinaryTreeAdmin(admin.TabularInline):
    model = BinaryTree

    def get_extra(self, request, obj=None, **kwargs):
        extra = 2
        if obj:
            return extra - obj.binarytree_set.count()
        return extra

###
class BinaryTreeAdmin(admin.TabularInline):
    model = BinaryTree

    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 10
        if obj and obj.parent:
            return max_num - 5
        return max_num

########## two or more foreign keys to the same parent model
from django.db import models

class Friendship(models.Model):
    to_person = models.ForeignKey(Person, on_delete=models.CASCADE,
            related_name="friends")
    from_person = models.ForeignKey(Person, on_delete=models.CASCADE,
            related_name="from_friends")

###
from django.contrib import admin
from myapp.models import Friendship

class FriendshipInline(admin.TabularInline):
    model = Friendship
    fk_name = "to_person"


class PersonAdmin(admin.ModelAdmin):
    inlines = [
            FriendshipInline,
    ]

######## working with many-to-many models

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, related_name='groups')

###
from django.contrib import admin

class MembershipInline(admin.TabularInline):
    model = Group.members.through


class PersonAdmin(admin.ModelAdmin):
    inlines = [
            MembershipInline,
    ]


class GroupAdmin(admin.ModelAdmin):
    inlines = [
            MembershipInline,
    ]
    exclude = ('members',)

############ working with many-to-many intermediary models

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

###
class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1

###
class PersonAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)

class GroupAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)

### finally, register your Person and Group models with the admin site
admin.site.register(Person, PersonAdmin)
admin.site.register(Group, GroupAdmin)

############### hooking AdminSite instances into your URLconf
# urls.py
from django.dontrib import admin
from django.urls import path

urlpatterns = [
        path('admin/', admin.site.urls),
]

############## customaizing th AdminSite class
# myapp/admin.py
from django.contrib.admin import AdminSite
from .models import MyModel

class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'

admin_site = MyAdminSite(name='myadmin')
admin_site.register(MyModel)

# myproject/urls.py
from django.urls import path
from myapp.admin import admin_site

urlpatterns = [
        path('myadmin/', admin_site.urls),
]

############## multiple admin sites in the same URLconf
# urls.py
from django.urls import path
from myproject.admin import advanced_site, basic_site

urlpatterns = [
        path('basic-admin/', basic_site.urls),
        path('advanced-admin/', advanced_site.urls),
]

########### adding a password reset feature
from django.contrib.auth import views as auth_views

path(
        'admin/password_reset/',
        auth_views.PasswordResetView.as_view(),
        name='admin_password_reset',
),
path(
        'admin/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
),
path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
),
path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
),

############## the staff_member_required decorator
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def my_view(request):
    ...

########## writing action function for admin site
from django.db import models

STATUS_CHOICES = [
        ('d', 'Draft'),
        ('p', 'Published')
        ('w', 'Withdrawn'),
]

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

###
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')


###
for obj in queryset:
    do_something_with(obj)

###
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"

### adding action to the ModelAdmin
from django.contrib import admin
from myapp.models import Article

def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = [make_published]

admin.site.register(Article, ArticleAdmin)

########### for code design better
class ArticleAdmin(admin.ModelAdmin):
    ...
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(status='p')
    make_published.short_description = "Mark selected stories as published"

###
from django.contrib import messages
from djano.utils.translation import ngettext

class ArticleAdmin(admin.ModelAdmin):
    ...
    
    def make_published(self, request, queryset):
        updated = queryset.update(status='p')
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)

############## action that provide intermediate pages
from django.core import serializers
from django.http import HttpResponse

def export_as_json(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)
    return response

###
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect

def export_selected_objects(modeladmim, request, queryset):
    selected = queryset.values_list('pk', flat=True)
    ct = ContentType.objects.get_for_model(queryset.model)
    return HttpResponseRedirect('/export/?ct=%s&ids=%s' % (
        ct.pk,
        ','.join(str(pk) for pk in selected),
    ))

########## disabling actions
# Globally disable delete selected
admin.site.disabe_action('delete_selected')

# This ModeAdmin will not have delete_selected available
class SomeModelAdmin(admin.ModelAdmin):
    actions = ['some_other_action']
    ...

# This one will
class AnotherModelAdmin(admin.ModelAdmin):
    actions = ['delete_selected', 'a_third_action']
    ...

### disabling all actions for a particular ModelAdmin
class MyModelAdmin(admin.ModelAdmin):
    actions = None

### conditionally enabling or disabling actions
class MyModelAdmin(admin.ModelAdmin):
    ...
    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.username[0].upper() != 'J':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions

### setting permissions for actions
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.allowed_permissions = ('change',)

###
from django.contrib import admin
from django.contrib.auth import get_permission_codename

class ArticleAdmin(admin.ModelAdmin):
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(status='p')
    make_published.allowed_permissions = ('publish',)

    def has_publish_permission(self, request):
        """Does the user have the publish permission?"""
        opts = self.opts
        codename = get_permission_codename('publish', opts)
        return request.user.has_perm('%s.%s' % (opts.app_label, codename))

#############


