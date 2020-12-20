from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import stripe

@csrf_exempt
@require_POST
def webhook(request):

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
    print('success')
    return HttpResponse(status=200)
