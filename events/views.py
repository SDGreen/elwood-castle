from django.shortcuts import render, get_object_or_404

from .models import Category, Event


# Create your views here.
def all_events(request):

    events = Event.objects.all()

    template = 'events/events.html'

    context = {
        'events': events
    }

    return render(request, template, context)


def event_info(request, event_id):

    print("triggered")
    event = get_object_or_404(Event, pk=event_id)

    template = 'events/event_details.html'
    context = {
        'event': event,
    }

    return render(request, template, context)
