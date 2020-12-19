from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm

from basket.contexts import basket_items

import stripe


# Create your views here.
def checkout(request):

    basket = basket_items(request)
    stripe_total = int(basket["total"] * 100)


    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency= settings.STRIPE_CURRENCY,
        # Verify your integration in this guide by including this parameter
        metadata={'integration_check': 'accept_a_payment'},
    )
    print(intent)
    
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'Your basket is empty')
        return redirect(reverse('view_basket'))

    order_form = OrderForm()

    context = {
        'order_form': order_form,
        'stripe_public_key': '7934729837492782',
        'client_secret': intent.client_secret
    }

    return render(request, 'checkout/checkout.html', context)
