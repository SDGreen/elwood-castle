from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_POST
from django.contrib import messages

from events.models import Event

# Create your views here.
def view_basket(request):
    return redirect(reverse('index'))


@require_POST
def add_to_basket(request, event_id):

    event = Event.objects.get(pk=event_id)
    date = request.POST.get('date')
    ticket_quantity = int(request.POST.get('ticket_quantity'))

    basket = request.session.get('basket', {})

    if event_id in basket.keys():
        if date in basket[event_id]['event_dates']:
            basket[event_id]['event_dates'][date] += ticket_quantity
            messages.success(request, f'''Ticket quanty for {event.name} on the
                            {date} updated to
                            {basket[event_id]['event_dates'][date]}''')
        else:
            basket[event_id]['event_dates'][date] = ticket_quantity
            messages.success(request, f'''{ticket_quantity} tickets added for the {event.name}
                                         on {date}''')
    else:
        basket[event_id] = {'event_dates': {date: ticket_quantity}}
        messages.success(request, f'''{ticket_quantity} tickets added for the {event.name}
                                         on {date}''')
    
    request.session['basket'] = basket

    return redirect(reverse('events'))


    print(date, ticket_quantity)

    return redirect(reverse('events'))
    


