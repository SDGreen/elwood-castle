from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .webhook_handler import Stripe_WH_Handler

import stripe


@csrf_exempt
@require_POST
def webhook(request):
    """
    Listens for webhooks from stripe and makes sure the appropriate
    method is activated
    """

    # required webhook settings
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY
    # Stripe WH setup (taken from the docs)
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # invalid payload
        return HttpResponse(
            content=e,
            status=400
            )
    except stripe.error.SignatureVerificationError as e:
        # invalid signature
        return HttpResponse(
            content=e,
            status=400
            )
    except Exception as e:
        # other error
        return HttpResponse(
            content=e,
            status=400
            )

    handler = Stripe_WH_Handler(request)

    event_map = {
             'payment_intent.succeeded': handler.handle_payment_succeeded,
             'payment_intent.payment_failed': handler.handle_payment_failed,
             }
    event_type = event['type']
    event_handler = event_map.get(event_type, handler.handle_other_event)
    response = event_handler(event)

    return response
