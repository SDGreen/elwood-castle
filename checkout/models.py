from django.db import models
from django.db.models import Sum

from events.models import Event
from user_account.models import UserAccount

import uuid


# Creates random numbers for order number and booking confirmation number
def generate_random_number():
    return uuid.uuid4().hex.upper()


# Create your models here.
class Order(models.Model):

    user_account = models.ForeignKey(UserAccount, null=True, blank=True,
                                     on_delete=models.SET_NULL,
                                     related_name='orders')
    order_number = models.CharField(max_length=32, null=False, editable=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    stripe_id = models.CharField(max_length=27, null=False, blank=False)
    total = models.DecimalField(max_digits=7, decimal_places=2,
                                null=True, blank=False, default=0)

    def save(self, *args, **kwargs):

        if not self.order_number:
            self.order_number = generate_random_number()
        super().save(*args, **kwargs)

    def update_total(self):
        self.total = self.bookings.aggregate(
                                             Sum('booking_total')
                                             )['booking_total__sum']
        self.save()

    def __str__(self):
        return f'{self.order_number}: {self.date}'


class EventBooking(models.Model):

    confirmation_number = models.CharField(max_length=32, null=False,
                                           editable=False)
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='bookings')
    event = models.ForeignKey(Event, null=False, blank=False,
                              on_delete=models.CASCADE,)
    date = models.DateField(auto_now=False, auto_now_add=False,
                            null=False, blank=False)
    ticket_quantity = models.IntegerField()
    booking_total = models.DecimalField(max_digits=7, decimal_places=2,
                                        null=False, blank=False,
                                        editable=False, default=0)

    def save(self, *args, **kwargs):

        if not self.confirmation_number:
            self.confirmation_number = generate_random_number()
        self.booking_total = self.ticket_quantity * (self.event.price)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.event.name} on {self.date} - {self.order.order_number}'
