def basket_items(request):

    basket_items = []
    total = 0

    basket = request.session.get('basket', {})

    context = {
        'basket_items': basket_items,
        'total': total,
    }

    return context
