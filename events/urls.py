from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_events, name='events'),
    path('<int:event_id>/', views.event_info, name="event_info"),
    path('book/<int:event_id>/', views.book_event, name="book_event")
]
