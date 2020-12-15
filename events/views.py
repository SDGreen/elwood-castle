from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

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
    """
    Returns event details for induvidual events or redirects to
    events page if the event id doesn't exist
    """


    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        messages.error(request, "Sorry, we couldn't find that event")
        return redirect(reverse('events'))

    template = 'events/event_details.html'
    context = {
        'event': event,
    }

    return render(request, template, context)
