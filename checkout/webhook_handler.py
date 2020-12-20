from django.shortcuts import HttpResponse


class Stripe_WH_Handler:

    def __init__(self, request):
        self.request = request

    def handle_payment_succeeded(self, event):
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f"webhook recieved: {event['type']}",
            status=200
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