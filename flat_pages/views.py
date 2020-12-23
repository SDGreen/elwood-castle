from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'flat_pages/index.html')

def visit(request):
    return render(request, 'flat_pages/visit.html')

def faq(request):
    return render(request, 'flat_pages/faq.html')