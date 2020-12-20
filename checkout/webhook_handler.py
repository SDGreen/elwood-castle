from django.shortcuts import HttpResponse


class Stripe_WH_Handler:

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f"webhook recieved: {event['type']}",
            status=200
        )