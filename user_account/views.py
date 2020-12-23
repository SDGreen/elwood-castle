from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserAccount
from checkout.models import EventBooking, Order

import datetime


# Create your views here.

@login_required
def user_home(request):

    useraccount = None
    bookings = None
    try:
        useraccount = UserAccount.objects.get(user__username=request.user)
        bookings = EventBooking.objects.filter(order__user_account=useraccount).order_by('-date')
    except UserAccount.DoesNotExist:
        messages.error(request, """Sorry, we couldn't find your account
                                   information, please get in contact so we
                                   can fix this for you""")
        return redirect(reverse('events'))

    no_bookings = False
    if not bookings:
        no_bookings = True

    today = datetime.datetime.today()
    upcoming_bookings = bookings.filter(date__gte=today).order_by("date")
    past_bookings = bookings.filter(date__lt=today)

    orders = useraccount.orders.all().order_by("date")

    context = {
        'useraccount': useraccount,
        'upcoming_bookings': upcoming_bookings,
        'past_bookings': past_bookings,
        'no_bookings': no_bookings,
        'orders': orders
    }

    return render(request, 'user_account/user_home.html', context)


def order_summary(request, order_number):

    try:
        order = Order.objects.get(order_number=order_number)
    except Exception:
        messages.error(request, """Sorry, we can't find this order!\
                                   Please contact us so we can
                                   fix this for you""")
        return redirect(reverse('user_home'))

    context = {
        'order': order
    }
    return render(request, 'user_account/order_summary.html', context)
