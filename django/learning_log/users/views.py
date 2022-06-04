from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Registered a new user."""
    if request.method != 'POST':
        # Show empty registration form.
        form = UserCreationForm()
    else:
        # Handling for data of form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Enter and redirect on the home page.
            login(request, new_user)
            return redirect('learning_logs:index')

    # Return empty or not valid form.
    context = {'form': form}
    return render(request, 'register.html', context)
