from decimal import Decimal
from events.models import Event


def basket_items(request):
    """
    Creates an array of basket items from the users session basket
    which is avaliable to all the templates
    """
    basket_items = []
    total = 0

    basket = request.session.get('basket', {})

    for event_id, event_dates in basket.items():
        event = Event.objects.get(pk=event_id)
        for date, ticket_quantity in event_dates["event_dates"].items():

            total += ticket_quantity * Decimal(event.price)
            subtotal = ticket_quantity * Decimal(event.price)
            basket_items.append({
                "event": event,
                "event_id": event_id,
                "date": date,
                "ticket_quantity": ticket_quantity,
                "subtotal": subtotal
            })

    context = {
        'basket_items': basket_items,
        'total': total,
    }

    return context
