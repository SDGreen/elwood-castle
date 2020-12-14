from django.shortcuts import render

from .models import Category, Event


# Create your views here.
def all_events(request):

    events = Event.objects.all()

    template = 'events/events.html'

    context = {
        'events': events
    }

    return render(request, template, context)