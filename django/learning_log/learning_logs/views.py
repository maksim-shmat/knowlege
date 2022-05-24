from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """Home page of app Learining Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show list of themes."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Show one theme and all binded notes."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
