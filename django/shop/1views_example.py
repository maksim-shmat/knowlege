""" In views HttpResponse is need. """

from django.http import HttpResponse

def hello_fn(request, name="Word"):
    return HttpResponse("Hello {}!". format(name))

# traditional regular expression syntax for analog 
# In urls.py
    url(r'^hello_fn/(?P<name>\w+)/$', views.hello_fn),
    url(r'^hello-fn/$', views.hello_fn),

# In urls.py for Django 2.0
    path('hello-fn/<str:name>/', views.hello_fn),
    path('hello-fn/', views.hello_fn),

################
from django.views.generic import Views

class HelloView(View):
    def get(self, request, name="World"):
        return HttpResponse("Hello {}!".format(name))

# and urls.py for this
    path('hello-cl/<str:name>/', views.HelloView.as_view()),
    path('hello-cl/', views.HelloView.as_view()),

###############
class GreetView(View):
    greeting = "Hello {}!"
    default_name = "World"
    def get(self, request, **kwargs):
        name = kwargs.pop("name", self.default_name)
        return HttpResponse(self.greeting.format(name))

class SuperVillainView(GreetView):
    greeting = "We are the future, {}. Not them. "
    default_name = "my friend"

# and urls.py
    path('hello-su/<str:name>/', views.SuperVillainView.as_view()),
    path('hello-su/', views.SuperVillainView.as_view()),

###############
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
            return render(request, self.template_name,
                         {'form': form})
###
# analog from DRY
from djnago.urls import reverse_lazy

class GenericFormView(generic.FormView):
    template_name = 'form.html'
    form_class = PersonDetailsForm
    success_url = reverse_lazy("success")

################
class PersonDetailsForm(forms.Form):
    name = form.CharField(max_length=100)
    age = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        upgrade = kwargs.pop("upgrade", False)  # if True - implemented
        super().__init__(*args, **kwargs)

        # Show first class option?
        if upgrade:
            self.fields["first_class"] = forms.BooleanField(
                    label="Fly First Class?")

#####
# with True
class PersonDetailsEdit(generic.FormView):
    ...
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["upgrade"] = True
        return kwargs

###############
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
###############
