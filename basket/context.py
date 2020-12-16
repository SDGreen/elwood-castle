from decimal import Decimal


def basket_items(request):
    basket_items = []
    if not basket_items:
        items_count = 0
    else:
        items_count = basket_items.count()
    total = 0

    context = {
        'basket_items': basket_items,
        'items_count': items_count,
        'total': total,
    }

    return context
