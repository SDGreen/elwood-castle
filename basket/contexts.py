def basket_items(request):

    basket_items = []
    total = 0

    basket = request.session.get('basket', {})

    for event_id, event_dates in basket.items():
        for date, ticket_quantity in event_dates["event_dates"].items():
            basket_items.append({
                "event_id": event_id,
                "date": date,
                "ticket_quantity": ticket_quantity,
            })

    context = {
        'basket_items': basket_items,
        'total': total,
    }

    return context
