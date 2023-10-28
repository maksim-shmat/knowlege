"""Forms for Django about."""

#1 crispy forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class PersonDetailsForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('submit', 'Submit'))

#2 view.py for forms

class ClassBasedFormView(generic.View):
    template_name = 'form.html'

    def get(self, request):
        form = PersonDetailsForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PersonDetailsForm(request.POST)
        if form.is_valid():
            # Success! We can use form.cleaned_data now
            return redirect('success')
        else:
            # Invalid form! Reshow the form with error highlighted
            return render(request, self.template_name, {'form': form})

#3 urls?

from django.urls import reverse_lazy


class GenericFormView(generic.FormView):
    template_name = 'form.html'
    form_class = PersonDetailsForm
    success_url = reverse_lazy("success")

#4 Pattern - user-based form

class GenericFormView(generic.FormView):
    template_name = 'cbv-form.html'
    form_class = PersonDetailsForm
    success_url = reverse_lazy("home")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Check if the logged-in user is a member of "VIP" group
        kwargs["vip"] = self.request.user.groups.filter(
                name="VIP").exists()
        return kwargs

#5 Pattern - multiple form actions per view

# form
class SubscribeForm(forms.Form):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('subscribe_butn', 'Subscribe'))

# view

from .forms import SubscribeForm, UnSubscribeForm


class NewsletterView(generic.TemplateView):
    subscribe_form_class = SubscribeForm
    unsubscribe_form_class = UnSubscribeForm
    template_name = "newsletter.html"

    def get(self, request, *args, **kwargs):
        kwargs.setdefault("subscribe_form",
                self.subscribe_form_class())
        kwargs.setdefault("unsubscribe_form",
                self.unsubscribe_form_class())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form_args = {
                'data': self.request.POST,
                'files': self.request.FILES,
        }
        if "subscribe_butn" in request.POST:
            form = self.subscribe_form_class(**form_args)
            if not form.is_valid():
                return self.get(request, subscribe_form=form)
            return redirect("success_form1")
        elif "unsubscribe_butn" in request.POST:
            form = self.unsubscribe_form_class(**form_args)
            if not form.is_valid():
                return self.get(request, unsubscribe_form=form)
            return redirect("success_form2")
        return super().get(request)

#6 Pattern CRUD views
# models.py

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

#7 formchapter/forms.py

from django import forms
from . import models
from crispy_forms.helper import FormHelper
from crispy_form.layout import Submit


class ImportantDateForm(forms.ModelForm):
    class Meta:
        model = models.ImportantDate
        fields = ["date", "desc"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Sabe'))

#8 formchapter/urls.py

path('impdates/<int:pk>/',
        views.ImpDateDetail.as_view(),
        name="impdate_create"),

path('impdates/create/',
        views.ImpDateCreate.as_view(),
        name="impdate_create"),

path('impdates/<int:pk>/edit/',
        views.ImpDateUpdate.as_view(),
        name="impdate_update"),

path('impdates/<int:pk>/delete/',
        views.ImpDateDelete.as_view(),
        name="impdate_delete"),

path('impdates/',
        views.ImpDateList.as_view(),
        name="impdate_list"),

#9
