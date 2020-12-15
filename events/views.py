from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Category, Event


# Create your views here.
def all_events(request):
    """
    View for returning all or filtered events to the user
    """

    events = Event.objects.all()
    categories = Category.objects.all()
    selected_category = None
    query = None
    sort = None

    if request.method == "GET":
        if sort in request.GET:
            sort = request.GET['sort']

            events = events.order_by('price')

        if "category" in request.GET:
            selected_category = request.GET['category']
            events = events.filter(category__name=selected_category)
            try:
                selected_category = get_object_or_404(Category,
                                                      name=selected_category)
            except Exception:
                pass

        if "q" in request.GET:
            query = request.GET['q']
            print(query)
            filters = (Q(name__icontains=query) |
                       Q(description__icontains=query) |
                       Q(category__friendly_name__icontains=query))
            events = events.filter(filters)



    template = 'events/events.html'

    context = {
        'events': events,
        'categories': categories,
        'query': query,
        'selected_category': selected_category,
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
