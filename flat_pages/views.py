from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

from .forms import ContactForm
from user_account.models import UserAccount


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
                send_mail(subject,
                          message,
                          user_email,
                          [settings.DEFAULT_FROM_EMAIL])
                messages.success(request, """Thanks for contacting Elwood
                                             Castle. A member of the team will
                                             be in touch within 48 hours.""")
            except Exception:
                messages.error(request, """There was an issue sending your
                                            message. If your message is urgent
                                            please call (+44) 20 7946 0559""")
                return redirect(reverse('contact'))
            return redirect(reverse('contact'))
    else:
        if request.user.is_authenticated:
            try:
                useraccount = UserAccount.objects.get(user=request.user)
                user_email = useraccount.email
                contact_form = ContactForm({'user_email': user_email})
            except Exception as e:
                contact_form = ContactForm()
        else:
            contact_form = ContactForm()
    context = {
        "contact_form": contact_form
    }
    return render(request, 'flat_pages/contact.html', context)


def under_contruction(request):

    messages.error(request, """The social account you tried to access is currently
                               unavaliable""")

    return redirect(reverse('index'))
