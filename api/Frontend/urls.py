from django.urls import path
from .views import EventsAndDishesView

app_name = 'Frontend'

urlpatterns = [
    path('events-and-dishes/', EventsAndDishesView.as_view(), name='events-and-dishes'),
]