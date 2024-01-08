from django.urls import path
from Dishes.views import GetDishesAPIView

app_name = 'Dishes'

urlpatterns = [
    path('get_dishes/', GetDishesAPIView.as_view()),
]