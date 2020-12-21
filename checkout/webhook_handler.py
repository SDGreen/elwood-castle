from django.shortcuts import HttpResponse

from .models import Order, EventBooking

import time
import datetime
import json


class Stripe_WH_Handler:

    def __init__(self, request):
        self.request = request

    def handle_payment_succeeded(self, event):
        intent = event.data.object
        pid = intent.id
        basket = json.loads(intent.metadata.basket)
        print(basket)
        del intent.metadata.basket
        form_data = {}
        for key, value in intent.metadata.items():
            if key != ("integration_check" or "basket"):
                form_data[key] = value.strip()
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
                #time.sleep(5)
        if order_exists:
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
                    first_name=form_data['first_name'],
                    last_name=form_data['last_name'],
                    email=form_data['email'],
                    phone_number=phone_number,
                    stripe_id=pid,
                )
                for event in basket:
                    date = datetime.datetime.strptime(date,
                                                      '%d/%m/%Y').strftime(
                                                      '%Y-%m-%d')
                    print('sam')
                    booking = EventBooking(
                        order=order,
                        event=event_id,
                        date=date,
                        ticket_quantity=ticket_quantity,
                        booking_total=event["subtotal"]
                    )
                    booking.save()
            except Exception as e:
                return HttpResponse(
                    content=f"Issue saving order in webhook {e}",
                    status=500
                )
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
