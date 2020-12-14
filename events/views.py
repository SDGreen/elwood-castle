from django.shortcuts import render


# Create your views here.
def all_events(request):

    print('working')

    template = 'events/events.html'

    context = {
        'sam': 'sam'
    }

    return render(request, template, context)