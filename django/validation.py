"""Validation forms."""

# URL: /person/<id>/children/add/

def add_relative(request, **kwargs):
    if form.is_valid:
        new_person = form.save()
        return HttpResponseRedirect(new_person.get_absolute_url())
    else:
        relative = get_object_or_404(Person, pk=kwargs['id'])
        form = PersonForm(initial={'last': relative.last})

    return render_to_response('person/form.html', {'form': form})
