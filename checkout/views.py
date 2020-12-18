from django.shortcuts import render

from .forms import OrderForm


# Create your views here.
def checkout(request):

    order_form = OrderForm()

    context = {
        'order_form': order_form
    }

    return render(request, 'checkout/checkout.html', context)
