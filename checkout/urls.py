from django.urls import path

from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_validator/', views.checkout_validator,
         name="checkout_validator"),
    path('webhhookincoming/', webhook, name='webhook'),
    path('success/<order_number>/', views.checkout_success,
         name="checkout_success")
]
