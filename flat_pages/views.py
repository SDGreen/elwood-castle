from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.contrib import messages

from .forms import ContactForm


# Create your views here.
def index(request):
    return render(request, 'flat_pages/index.html')


def visit(request):
    return render(request, 'flat_pages/visit.html')


def faq(request):
    return render(request, 'flat_pages/faq.html')


def contact(request):

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            user_email = contact_form.cleaned_data['user_email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(subject, message, user_email, ['admin@example.com'])
                messages.success(request, """Thanks for contacting Elwood
                                             Castle. A member of the team will
                                             be in touch within 48 hours.""")
            except Exception:
                messages.error(request, """There was an issue sending your
                                            message. If your message is urgent
                                            please call (+44) 20 7946 0559""")
                return redirect(reverse('contact'))
            return redirect(reverse('events'))
    else:
        contact_form = ContactForm()

    context = {
        "contact_form": contact_form
    }
    return render(request, 'flat_pages/contact.html', context)
