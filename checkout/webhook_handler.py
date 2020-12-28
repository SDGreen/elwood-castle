from django.shortcuts import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, EventBooking

from events.models import Event
from user_account.models import UserAccount

import time
import datetime
import json


class Stripe_WH_Handler:

    def __init__(self, request):
        self.request = request

    def _send_order_and_booking_emails(self, order):
        """
        This sends an email for the order confirmation and
        separate emails for each booking confirmation
        """

        order = Order.objects.get(order_number=order.order_number)
        customer_email = order.email
        order_email_subject = render_to_string(
            'checkout/emails/order_confirmation_head.txt',
            {'order': order}
        )
        order_email_body = render_to_string(
            'checkout/emails/order_confirmation_body.txt',
            {'order': order, 'elwood_email': settings.DEFAULT_FROM_EMAIL}
        )
        send_mail(
            order_email_subject,
            order_email_body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )
        for booking in order.bookings.all():
            booking_email_subject = render_to_string(
                'checkout/emails/booking_confirmation_head.txt',
                {'booking': booking}
            )
            booking_email_body = render_to_string(
                'checkout/emails/booking_confirmation_body.txt',
                {'booking': booking,
                 'elwood_email': settings.DEFAULT_FROM_EMAIL}
            )
            send_mail(
                booking_email_subject,
                booking_email_body,
                settings.DEFAULT_FROM_EMAIL,
                [customer_email]
            )

    def handle_payment_succeeded(self, event):
        intent = event.data.object
        pid = intent.id
        basket = json.loads(intent.metadata.basket)
        del intent.metadata.basket
        form_data = {}
        for key, value in intent.metadata.items():
            if key != ("integration_check" or "basket"):
                form_data[key] = value.strip()
        if form_data['user_account'] == "AnonymousUser":
            form_data['user_account'] = None
        else:
            try:
                form_data['user_account'] = UserAccount.objects.get(
                    user__username=form_data['user_account']
                )
            except Exception as e:
                print(e)
                form_data['user_account'] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    stripe_id=pid
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(5)
        if order_exists:
            self._send_order_and_booking_emails(order)
            return HttpResponse(

                content=f"""webhook recieved: {event['type']}, Order created in
                            database by views.checkout""",
                status=200
            )
        elif not order_exists:
            try:
                phone_number = None
                if form_data['phone_number']:
                    phone_number = form_data['phone_number']
                order = Order.objects.create(
                    user_account=form_data['user_account'],
                    first_name=form_data['first_name'],
                    last_name=form_data['last_name'],
                    email=form_data['email'],
                    phone_number=phone_number,
                    stripe_id=pid,
                )
                for event_booking in basket['basket_items']:
                    event = Event.objects.get(pk=event_booking['event_id'])
                    date = datetime.datetime.strptime(
                        event_booking['date'], '%d/%m/%Y').strftime('%Y-%m-%d')
                    booking = EventBooking(
                        order=order,
                        event=event,
                        date=date,
                        ticket_quantity=event_booking['ticket_quantity'],
                        booking_total=event_booking['subtotal']
                    )
                    booking.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f"""Issue saving order in webhook {e}, payment still
                                processed, contact customer""",
                    status=500
                )
            self._send_order_and_booking_emails(order)
            return HttpResponse(
                content=f"Order {order.order_number} created in webhook",
                status=200
            )
        else:
            return HttpResponse(
                content=f"""Issue with identifying order in webwook, check to
                            see if order is in database. stripe_id = {pid},
                            payment was successful"""
            )

    def handle_payment_failed(self, event):
        return HttpResponse(
            content=f"webhook recieved: {event['type']}",
            status=200
        )

    def handle_other_event(self, event):
        return HttpResponse(
            content=f"webhook recieved: {event['type']}",
            status=200
        )
