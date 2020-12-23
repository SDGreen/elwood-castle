from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('visit/', views.visit, name="visit"),
    path('faq/', views.faq, name="faq")
]
