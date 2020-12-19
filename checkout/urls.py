from django.urls import path

from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_validator/', views.checkout_validator,
         name="checkout_validator")
]
