from django.urls import path
from .views import GetPlacesAPIView, GetReservedPlacesAPIView, \
    UpdatePlaceStatusAPIView


app_name = 'Places'

urlpatterns = [
    path('get_places/', GetPlacesAPIView.as_view()),
    path('get_reserved_places/', GetReservedPlacesAPIView.as_view()),
    path('update_place_status/<place_id>/', UpdatePlaceStatusAPIView.as_view()),
]