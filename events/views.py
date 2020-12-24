from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.contrib import messages
from django.db.models import Q, Sum
from django.views.decorators.http import require_POST

from .models import Category, Event
from checkout.models import EventBooking
from basket.contexts import basket_items

import datetime

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
    direction = None

    if request.method == "GET":
        if 'sort' in request.GET:
            sort = request.GET['sort']
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == "desc":
                    sort = f"-{sort}"

            events = events.order_by(sort, "name")

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


def book_event(request, event_id):

    try:
        event = Event.objects.get(pk=event_id)
    except Exception as e:
        messages.error(request, f"""Sorry, that event can't be booked right now:
                                    {e}""")
        return redirect(reverse('events'))

    bookings = EventBooking.objects.filter(event=event).values(
        'date').annotate(Sum('ticket_quantity'))

    sold_out_dates = []
    for booking in bookings:
        if booking['ticket_quantity__sum'] >= event.day_ticket_limit:
            date = booking['date'].strftime("%d/%m/%Y")
            sold_out_dates.append(date)

    template = 'events/book_event.html'
    context = {
        'event': event,
        'sold_out_dates': sold_out_dates
    }
    return render(request, template, context)


@require_POST
def date_checker(request):
    try:

        event = Event.objects.get(pk=request.POST.get('event_id'))

        string_date = request.POST.get('date')
        datetime_date = datetime.datetime.strptime(
            request.POST.get('date'), "%d/%m/%Y")
        basket = basket_items(request)
        basket_events = basket["basket_items"]
        tickets = EventBooking.objects.filter(
            date=datetime_date, event=event).aggregate(Sum('ticket_quantity'))

        booked_tickets = tickets['ticket_quantity__sum']
        if not booked_tickets:
            booked_tickets = 0

        basket_tickets = 0
        print(basket_events)
        if not basket_events:
            pass
        else:
            for basket_event in basket_events:
                if basket_event["event"] == event:
                    if basket_event["date"] == string_date:
                        basket_tickets += basket_event["ticket_quantity"]

        print(basket_tickets)

        avaliable_tickets = event.day_ticket_limit - \
            (booked_tickets + basket_tickets)
        return HttpResponse(
            status=200,
            content=avaliable_tickets
        )

    except Exception as e:

        messages.error(
            request, f"""Something went wrong whilst checking the tickets for
                         this date {e}""")
        return HttpResponse(status=500)
