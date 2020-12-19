from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .models import EventBooking, Order
from .forms import OrderForm

from basket.contexts import basket_items
from events.models import Event

import stripe
import datetime


# Create your views here.
def checkout(request):

    basket_check = request.session.get('basket', {})
    if not basket_check:
        messages.error(request, "Your basket is empty")
        return redirect(reverse('view_basket'))

    basket = basket_items(request)
    stripe_total = int(basket["total"] * 100)


    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency= settings.STRIPE_CURRENCY,
        # Verify your integration in this guide by including this parameter
        metadata={'integration_check': 'accept_a_payment'},
    )

    if request.method == 'POST':
        form_data = {}
        for key, post_data in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                form_data[key] = post_data
        print(form_data)

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for event in basket['basket_items']:
                date = datetime.datetime.strptime(event["date"], '%d/%m/%Y').strftime('%Y-%m-%d')
                print(date)
                booking = EventBooking(
                    order=order,
                    event=event["event"],
                    date=date,
                    ticket_quantity=event['ticket_quantity'],
                    booking_total=event["subtotal"]
                )
                booking.save()
            messages.success(request, f"{order.order_number} successfully processed")
            return redirect(reverse('checkout_success', args=[order.order_number]))

        else:
            messages.error(request, """Something has gone wrong during
                                       checkout, please contact us as soon as
                                       possible as you may have been
                                       charged""")

    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, 'Your basket is empty')
            return redirect(reverse('view_basket'))

        order_form = OrderForm()

        context = {
            'order_form': order_form,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
            'client_secret': intent.client_secret
        }
        return render(request, 'checkout/checkout.html', context)


@require_POST
def checkout_validator(request):
    """
    This validates the form and basket items before payment takes place
    """
    try:
        basket = basket_items(request)
        form_data = {}
        for key, value in request.POST.items():
            if key != "csrfmiddlewaretoken":
                key = key.split('[')[1].split(']')[0]
                form_data[key] = value
        order = OrderForm(form_data)
        if order.is_valid():
            for item in basket['basket_items']:
                print(item["event_id"])
                try:
                    event = Event.objects.get(pk=item['event_id'])
                except event.DoesNotExist:
                    messages.error(request, """One of the events does not
                                                exist in out database, please
                                                contact us. Your card has not
                                                been charged""")
                    return HttpResponse(status=500)
            return HttpResponse(status=200)
        else:
            messages.error(request, """Please check your form, your card has not
                                       been charged""")
            return HttpResponse(status=500)
    except Exception as e:
        messages.error(request, f"""Something has gone wrong whilst checking
                                   your form, please contact us so we can fix
                                   it for you. {e}""")
        return HttpResponse(status=500)

def checkout_success(request, order_id):

    order = Order.objects.get(pk=order_id)

    context = {
        'order': order
    }
    return render(request, 'checkout/checkout_success.html', context)
