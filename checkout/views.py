from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# Create your views here.
def checkout(request):

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'Your basket is empty')
        return redirect(reverse('view_basket'))

    order_form = OrderForm()

    context = {
        'order_form': order_form,
        'stripe_public_key': '7934729837492782',
        'client_secret': 'Client Secret'
    }

    return render(request, 'checkout/checkout.html', context)
