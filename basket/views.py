from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_basket(request):
    return redirect(reverse('index'))
