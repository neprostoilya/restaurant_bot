from django.urls import path
from Events.views import GetEventsAPIView


app_name = 'Events'

urlpatterns = [
    path('get_events/', GetEventsAPIView.as_view()),
]