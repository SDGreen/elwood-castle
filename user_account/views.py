from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserAccount
from checkout.models import EventBooking

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

    today = datetime.datetime.today()
    upcoming_bookings = bookings.filter(date__gte=today)
    past_bookings = bookings.filter(date__lt=today)

    context = {
        'useraccount': useraccount,
        'upcoming_bookings': upcoming_bookings,
        'past_bookings': past_bookings,
    }

    return render(request, 'user_account/user_home.html', context)
