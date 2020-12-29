from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages

from events.models import Event


# Create your views here.
def view_basket(request):
    return render(request, 'basket/view_basket.html')


@require_POST
def add_to_basket(request, event_id):

    event = Event.objects.get(pk=event_id)
    date = request.POST.get('date')
    ticket_quantity = int(request.POST.get('ticket_quantity'))
    event_id = str(event_id)

    basket = request.session.get('basket', {})

    if event_id in basket.keys():
        if date in basket[event_id]['event_dates'].keys():
            basket[event_id]['event_dates'][date] += ticket_quantity
            messages.success(request, f'''Ticket quanty for {event.name} on the
                            {date} updated to
                            {basket[event_id]['event_dates'][date]}''')
        else:
            basket[event_id]['event_dates'][date] = ticket_quantity
            messages.success(request, f'''{ticket_quantity} ticket(s) added for the {event.name}
                                         on {date}''')
    else:
        basket[event_id] = {'event_dates': {date: ticket_quantity}}
        messages.success(request, f'''{ticket_quantity} ticket(s) added for the {event.name}
                                         on {date}''')

    request.session['basket'] = basket

    return redirect(reverse('events'))


@require_POST
def remove_from_basket(request, event_id):

    try:
        event = Event.objects.get(pk=event_id)
        basket = request.session.get('basket', {})
        date = request.POST.get('date')

        if date not in basket[str(event_id)]['event_dates']:
            messages.error(request, f'''You have no tickets for {event.name} on
                                    {date}''')
            return HttpResponse(status=200)

        if date in basket[str(event_id)]['event_dates']:
            del basket[str(event_id)]['event_dates'][date]
            if len(basket[str(event_id)]['event_dates']) == 0:
                del basket[str(event_id)]
            messages.success(request, f'''Ticket(s) for {event.name}
                                         on {date} removed from basket''')
            request.session['basket'] = basket

            return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'''There was a problem removing this event from you bag:
                                    {e}''')
        return HttpResponse(status=500)


@require_POST
def update_basket(request, event_id):
    try:

        basket = request.session.get('basket', {})
        event = Event.objects.get(pk=event_id)
        date = request.POST.get('date')
        ticket_quantity = int(request.POST.get('ticket_quantity'))

        if str(event_id) not in basket.keys():
            messages.error(request, f"""You have no tickets for the
                                        {event.name}""")
            return HttpResponse(status=400)

        if date not in basket[str(event_id)]['event_dates']:
            messages.error(request, f"""You have no tickets for
                                        {event.name} on {date}""")
            return HttpResponse(status=400)

        basket[str(event_id)]['event_dates'][date] = ticket_quantity

        messages.success(request, f'''Ticket quanty for {event.name} on the
                                      {date} updated to {ticket_quantity}''')

        return redirect(reverse('view_basket'))

    except Exception as e:
        messages.error(request, f'''There was a problem updating your tickets to this event:
                                    {e}''')
        return HttpResponse(status=500)
